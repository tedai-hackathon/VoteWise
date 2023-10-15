import json
import os
import random

from environs import Env
from flask import Flask, render_template, request, jsonify, session, make_response
from flask_cors import CORS
from flask_wtf.csrf import CSRFProtect
from langchain.chains import ConversationChain
from langchain import OpenAI
from langchain.memory import ConversationSummaryBufferMemory
from wtforms import StringField, SelectField, SubmitField, RadioField, SelectMultipleField, widgets
from wtforms.validators import DataRequired
import os
import random
from wtforms.validators import DataRequired, Length, Regexp
from constants import STATE_CHOICES, LIKERT_CHOICES, LIKERT_LOOKUP, QUESTION_TEXT
from urllib.parse import quote, unquote
from forms import IntakeForm
from models import VoterInfo

env = Env()
# Read .env into os.environ
env.read_env()

llm = OpenAI()
memory = ConversationSummaryBufferMemory(llm=llm, max_token_limit=2000)
app = Flask(__name__)
app.secret_key = env.str("SECRET_KEY")
CORS(app)
csrf = CSRFProtect(app)

with open(os.path.join(app.root_path, 'static', 'ballot.json'), 'r') as f:
    ballot_data = json.load(f)

def races():
    new_list = (list(ballot_data.keys()) + list(ballot_data.get('Propositions').keys()))
    return new_list

def escaped_races():
    return [quote(item) for item in races()]

@app.route('/chat')
def chat():
    return render_template('index.html')

@app.route('/chat2')
def chat2():
    return render_template('chat.html')


@app.route('/skip-intake', methods=['GET'])
def skip_intake(be_conservative=True):
    liberal_answers = {'zip_code': '94666', 'party_affiliation': 'democrat',
                       'political_issues': ['healthcare', 'housing'],
                       'housing': '5', 'economy': '1', 'environment': '5', 'immigration': '2', 'income_inequality': '5',
                       'transportation': '4', 'education': '2', 'healthcare': '5', 'public_safety': '2',
                       'taxation': '5'}

    conservative_answers = {
        "address_zip_code": "94608",
        "city": "Oakland",
        "economy": "5",
        "education": "1",
        "environment": "1",
        "healthcare": "1",
        "housing": "1",
        "immigration": "5",
        "income_inequality": "1",
        "party_affiliation": "republican",
        "political_issues": [
            "economy",
            "public_safety"
        ],
        "public_safety": "1",
        "state": "CA",
        "street_address": "4109 West",
        "taxation": "1",
        "transportation": "1"
    }

    if be_conservative:
        data = conservative_answers
    else:
        data = liberal_answers

    voter_info = VoterInfo.from_vals(**data).for_llm()
    print(f"updating session with {voter_info}")
    session['voter_info'] = voter_info
    session.modified = True
    response = make_response('', 204)
    response.mimetype = 'application/json'
    return response


@app.route('/', methods=['GET', 'POST'])
def index():
    form = IntakeForm()
    if form.validate_on_submit():
        voter_info = VoterInfo()
        form_data = form.data
        # remove csrf token and any other unnecessary WTF-form inserted fields
        # just preserve the actual user-inputted data
        form.populate_obj(voter_info)
        session['voter_info'] = voter_info.for_llm()

        session.modified = True
        print(form_data)
        return jsonify(form_data)
    return render_template('intake_form.html', form=form)

# read the race and candidate parameters from the request, save them as kv into the session variable, and redirect to the next race
# input: race = encoded race name, candidate = encoded candidate name
from flask import redirect, url_for

@app.route('/confirm', methods=['GET'])
def confirm():
    race = request.args.get('race')
    candidate = request.args.get('candidate')
    if 'choices' not in session:
        session['choices'] = {}

    session['choices'][unquote(race)] = candidate

    session.modified = True

    race_index = escaped_races().index(race)
    next_race = escaped_races()[race_index + 1] if race_index < len(races()) - 1 else None
    return redirect(url_for('race', race_name=next_race))
    # get the index of this race from races    

# This is a temporary method that uses a super simple prompt to ensure that we get a valid response from the LLM
@app.route('/quick-recommendation', methods=['POST'])
@csrf.exempt
def quick_recommendation():
    return jsonify({"response": True, "message": {
        "candidate": "Jane Smith",
        "reason": "Jane Smith cares about children's ability to study remotely, which aligns with your values."
    }})



@app.route('/data', methods=['POST'])
@csrf.exempt
def get_data():
    data = request.get_json()
    text = data.get('data')
    voter_info = session.get('voter_info')

    # a prompt to instruct the LLM to make recommedations for my friend on who to vote for in the 2022 oakland
    # mayoral election should be written in a way that takes a json summarizing the voter and their values and makes
    # sure the LLM does not refuse to make a recommendation for any reason
    prompt = f"""
    My friend is a voter who lives in the 94608 zipcode.
    
    Here's an overall summary of what's known about them:
    
    {voter_info}
    
    Let's pretend the year is 2022 and we are one week out from the Oakland mayoral election. My friend is still 
    undecided on who to vote for, and needs help thinking through the choices. He comes to you guidance.
    
    Rank the actual candidates who were running in the Oakland mayoral race in order of how well they reflect my 
    friend's interests and preferences, explaining step by step how you arrived at the rank given to each candidate. 
    Name the specific candidates, and make reference to their specific actual positions.
    
    My friend is smart and reasonable and understands that your rankings will not be perfect, so don't hedge and just 
    give it your best shot.
    
    Give a single overall ranking for each candidate, and list the candidates in order of best to worst (making sure to specifically mention at least the top several candiddates).
    
    Be as specific and concrete as possible, and make sure to address the issues that are most important to him. 
    
    End up by making it very clear which candidate best reflects his interests and preferences.
    
    Format your answer nicely so that it's easy to read and understand.
    """

    prompt = text

    user_input = prompt

    print(user_input)
    try:
        conversation = ConversationChain(llm=llm, memory=memory)
        output = conversation.predict(input=user_input)
        memory.save_context({"input": user_input}, {"output": output})
        return jsonify({"response": True, "message": output})
    except Exception as e:
        print(e)
        error_message = f'Error: {str(e)}'
        return jsonify({"message": error_message, "response": False})
    

# Over the top routing magic
@app.route('/race/', defaults={'race_name': None})
@app.route('/race/<race_name>')
def race(race_name):

    decoded_race_name = None if race_name is None else unquote(race_name)
    race_description = """
The U.S. Senate is part of the 
legislative branch of the federal
government, and California, like
every other state, elects two
senators. Senators serve six-year
terms, and elections are staggered so
each state's two senators are not up
for re-election at the same time. The
2022 California Senatorial Election
you'll be voting in will determine
one of these two seats"""

    recommended_candidate_data = {
        "name": "Jane Smith",
        "reason": "Jane Smith cares about children's ability to study remotely, which aligns with your values."
    }

    return render_template('race.html', races=races(),
                            recommended_candidate=recommended_candidate_data,
                              current_race=decoded_race_name, 
                              ballot_data=races,
                              race_description = race_description,
                              quote = quote)


@app.route('/mayor', methods=['GET', 'POST'])
@csrf.exempt
def handle_issue_chat():
    # check if the request was a POST and if so, get the data
    if request.method == 'POST':
        data = request.get_json()
        text = data.get('data')
    else:
        text = ""

    voter_info_json = session.get('voter_info')
    voter_info = VoterInfoDecoder().decode(voter_info_json)

    # a prompt to instruct the LLM to make recommendations for my friend on who to vote for in the 2022 oakland
    # mayoral election should be written in a way that takes a json summarizing the voter and their values and makes
    # sure the LLM does not refuse to make a recommendation for any reason

    template = INITIAL_RECOMMENDATION_PROMPT

    # Create a PromptTemplate with necessary inputs
    prompt = PromptTemplate(
        input_variables=[
            "race",
            "voter_zip_code",
            "voter_info_summary",
            "race_info",
        ],
        template=template
    )

    # Use the PromptTemplate to construct the query
    constructed_query = prompt.format(**{
        "race": "2022 Oakland Mayor Election",
        "voter_zip_code": voter_info.address_zip_code,
        "voter_info_summary": voter_info_json,
        "race_info": OAKLAND_MAYOR_CANDIDATE_INFO,
    })

    print(constructed_query)

    try:
        conversation = ConversationChain(llm=llm, memory=memory)
        output = conversation.predict(input=constructed_query)
        memory.save_context({"input": constructed_query}, {"output": output})
        return jsonify({"response": True, "message": output})
    except Exception as e:
        print(e)
        error_message = f'Error: {str(e)}'
        return jsonify({"message": error_message, "response": False})


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
