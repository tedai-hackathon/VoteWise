from flask import Flask, render_template, jsonify, request, session
from flask_cors import CORS
from flask_wtf.csrf import CSRFProtect
import requests, openai, os
from dotenv.main import load_dotenv
from langchain.llms import OpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain.memory import ConversationSummaryBufferMemory

from flask import Flask, render_template, request, jsonify, session
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, RadioField, SelectMultipleField, widgets
from wtforms.validators import DataRequired
from flask_wtf.csrf import CSRFProtect

from environs import Env

env = Env()
# Read .env into os.environ
env.read_env()

llm = OpenAI()
memory = ConversationSummaryBufferMemory(llm=llm, max_token_limit=100)
app = Flask(__name__)
app.secret_key = "your_secret_key_here"
CORS(app)
csrf = CSRFProtect(app)


@app.route('/chat')
def chat():
    return render_template('index.html')


@app.route('/form')
def form():
    return render_template('intake_form.html')


# define a VoterInfo class to capture demographic and values information about the voter
# and then a FlaskForm that uses VoterInfo as a model and captures those fields

class VoterInfo:
    def __init__(self):
        self.zip_code = None
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


import json


class VoterInfoEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, VoterInfo):
            return obj.__dict__
        return super().default(obj)


class VoterInfoDecoder(json.JSONDecoder):
    def decode(self, json_str):
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


# create a form to

class IntakeForm(FlaskForm):
    zip_code = StringField('Zip Code', validators=[DataRequired()])
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

    housing = RadioField(
        "Government intervention is necessary for affordable housing.",
        choices=LIKERT_CHOICES, validators=[DataRequired()])
    economy = RadioField(
        "Job creation is more important than wealth redistribution in California.",
        choices=LIKERT_CHOICES, validators=[DataRequired()])
    environment = RadioField(
        "Environmental protection is worth slowing economic growth in California.",
        choices=LIKERT_CHOICES, validators=[DataRequired()])
    immigration = RadioField(
        "California's resources should primarily serve its citizens, not undocumented immigrants.",
        choices=LIKERT_CHOICES, validators=[DataRequired()])
    income_inequality = RadioField(
        "Reducing income inequality is more important than promoting business growth in California.",
        choices=LIKERT_CHOICES, validators=[DataRequired()])
    transportation = RadioField(
        "Public transportation is more important than private vehicle infrastructure in California.",
        choices=LIKERT_CHOICES, validators=[DataRequired()])
    education = RadioField(
        "Public education funding is more important than tax cuts in California.",
        choices=LIKERT_CHOICES, validators=[DataRequired()])
    healthcare = RadioField(
        "A single-payer healthcare system is preferable to private healthcare in California.",
        choices=LIKERT_CHOICES, validators=[DataRequired()])
    public_safety = RadioField(
        "Community programs are more effective than traditional law enforcement in California.",
        choices=LIKERT_CHOICES, validators=[DataRequired()])
    taxation = RadioField(
        "Progressive taxation is more beneficial than lower taxes for all in California.",
        choices=LIKERT_CHOICES, validators=[DataRequired()])

    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = IntakeForm()
    if form.validate_on_submit():
        voter_info = VoterInfo()
        form_data = form.data
        # remove csrf token and any other unnecessary WTF-form inserted fields
        # just preserve the actual user-inputted data
        form.populate_obj(voter_info)
        session['form_data'] = json.dumps(voter_info.__dict__)

        session.modified = True
        print(form_data)
        return jsonify(form_data)
    return render_template('intake_form.html', form=form)


@app.route('/data', methods=['POST'])
@csrf.exempt
def get_data():
    data = request.get_json()
    text = data.get('data')
    voter_info = VoterInfoDecoder().decode(session.get('form_data'))

    user_input = str(voter_info) + text

    try:
        conversation = ConversationChain(llm=llm, memory=memory)
        output = conversation.predict(input=user_input)
        memory.save_context({"input": user_input}, {"output": output})
        return jsonify({"response": True, "message": output})
    except Exception as e:
        print(e)
        error_message = f'Error: {str(e)}'
        return jsonify({"message": error_message, "response": False})


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
