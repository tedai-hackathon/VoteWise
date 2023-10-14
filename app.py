import json

from environs import Env
from flask import Flask, render_template, request, jsonify, session, make_response
from flask_cors import CORS
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
from langchain.chains import ConversationChain
from langchain.llms import OpenAI
from langchain.memory import ConversationSummaryBufferMemory
from wtforms import StringField, SelectField, SubmitField, RadioField, SelectMultipleField, widgets
from wtforms.validators import DataRequired
import os
import random
from wtforms.validators import DataRequired, Length, Regexp
from constants import STATE_CHOICES, LIKERT_CHOICES, LIKERT_LOOKUP, QUESTION_TEXT

env = Env()
# Read .env into os.environ
env.read_env()

llm = OpenAI()
memory = ConversationSummaryBufferMemory(llm=llm, max_token_limit=100)
app = Flask(__name__)
app.secret_key = "your_secret_key_here"
CORS(app)
csrf = CSRFProtect(app)

with open(os.path.join(app.root_path, 'static', 'ballot.json'), 'r') as f:
    ballot_data = json.load(f)


@app.route('/chat')
def chat():
    return render_template('index.html')


class VoterInfo:
    """
    define a VoterInfo class to capture demographic and values information about the voter
    and then a FlaskForm that uses VoterInfo as a model and captures those fields

    """
    likert_choices = [
        "housing",
        "economy",
        "environment",
        "immigration",
        "income_inequality",
        "transportation",
        "education",
        "healthcare",
        "public_safety",
        "taxation",
    ]

    def __init__(self):
        self.street_address = None
        self.city = None
        self.state = None
        self.address_zip_code = None
        self.party_affiliation = None
        self.political_issues = None
        self.housing = None
        self.economy = None
        self.environment = None
        self.immigration = None
        self.income_inequality = None
        self.transportation = None
        self.education = None
        self.healthcare = None
        self.public_safety = None
        self.taxation = None

    @classmethod
    def from_vals(cls, **kwargs):
        """
        alternative constructor that can take a dict of values and populate the fields

        :param kwargs:
        :return:
        """
        instance = cls()
        for k, v in kwargs.items():
            setattr(instance, k, v)
        return instance

    def for_llm(self):
        """
        output contents as a json-structured string we can feed to the llm.

        for all the likert fields, convert the numeric value to the corresponding string value,
        based on the LIKERT_CHOICES mapping.
        :return: str
        """
        fields = self.__dict__
        for likert_val in self.likert_choices:
            numeric_val = fields[likert_val]
            if numeric_val in LIKERT_LOOKUP:
                fields[likert_val] = {
                    'question': QUESTION_TEXT[likert_val],
                    'response': LIKERT_LOOKUP[numeric_val]
                }
        return json.dumps(fields)


class VoterInfoEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, VoterInfo):
            return obj.__dict__
        return super().default(obj)


class VoterInfoDecoder(json.JSONDecoder):
    def decode(self, json_str, **kwargs):
        data = json.loads(json_str)
        voter_info = VoterInfo()
        voter_info.__dict__.update(data)
        return voter_info

LIKERT_CHOICES = [
    ('1', 'Strongly Disagree'),
    ('2', 'Disagree'),
    ('3', 'Neutral'),
    ('4', 'Agree'),
    ('5', 'Strongly Agree')
]

# make a dict to look up the string for a given likert numeric value
LIKERT_LOOKUP = dict(LIKERT_CHOICES)

QUESTION_TEXT = {
    'housing': "Government intervention is necessary for affordable housing.",
    'economy': "Job creation is more important than wealth redistribution in California.",
    'environment': "Environmental protection is worth slowing economic growth in California.",
    'immigration': "California's resources should primarily serve its citizens, not undocumented immigrants.",
    'income_inequality': "Reducing income inequality is more important than promoting business growth in California.",
    'transportation': "Public transportation is more important than private vehicle infrastructure in California.",
    'education': "Public education funding is more important than tax cuts in California.",
    'healthcare': "A single-payer healthcare system is preferable to private healthcare in California.",
    'public_safety': "Community programs are more effective than traditional law enforcement in California.",
    'taxation': "Progressive taxation is more beneficial than lower taxes for all in California."
}


# TODO: return the values of the proposition keys as well
def races():
    return list(ballot_data.keys())


class IntakeForm(FlaskForm):
    # New fields for address
    street_address = StringField('Street Address', validators=[DataRequired(), Length(max=100)])
    city = StringField('City', validators=[DataRequired(), Length(max=50)])
    state = SelectField('State', choices=[('', 'Select State')] + STATE_CHOICES, validators=[DataRequired()])
    address_zip_code = StringField('ZIP Code', validators=[DataRequired(),
                                                           Length(min=5, max=5), Regexp(r'^\d{5}$')])

    # voting preference information
    party_affiliation = SelectField('Party Affiliation', choices=[
        ('democrat', 'Democrat'),
        ('republican', 'Republican'),
        ('independent', 'Independent'),
        ('other', 'Other')
    ], validators=[DataRequired()])
    political_issues = SelectMultipleField('Which of the following issues do you consider particularly important when '
                                           'deciding how to vote?', choices=[
        ('education', 'Education'),
        ('healthcare', 'Healthcare'),
        ('environment', 'Environment'),
        ('economy', 'Economy'),
        ('public_safety', 'Public Safety'),
        ('housing', 'Housing')

    ], option_widget=widgets.CheckboxInput(),
                                           widget=widgets.ListWidget(prefix_label=False),
                                           validators=[DataRequired()])

    # Dynamically create the Likert scale fields
    for likert_choice in VoterInfo.likert_choices:
        vars()[likert_choice] = RadioField(
            QUESTION_TEXT[likert_choice],
            choices=LIKERT_CHOICES,
            validators=[DataRequired()]
        )

    submit = SubmitField('Submit')


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
    
@app.route('/template')
def template():
    recommended_candidate_data = {
        "name": "Jane Smith",
        "reason": "Jane Smith cares about children's ability to study remotely, which aligns with your values."
    }

    # pick a random element of the races list
    current_race = random.choice(races())

    return render_template('layout.html', races=ballot_data, recommended_candidate=recommended_candidate_data, current_race=current_race, ballot_data=races)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
