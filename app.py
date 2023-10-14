from flask import Flask, render_template,jsonify,request, session
from flask_cors import CORS
import requests,openai,os
from dotenv.main import load_dotenv
from langchain.llms import OpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain.memory import ConversationSummaryBufferMemory


from flask import Flask, render_template, request, jsonify, session
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.csrf import CSRFProtect


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
    return render_template('form.html')


class SurveyForm(FlaskForm):
    zip_code = StringField('Zip Code', validators=[DataRequired()])
    sanctuary_city = SelectField('Do you support the current sanctuary city policies in California?', choices=[('Yes', 'Yes'), ('No', 'No')])
    tax_rates = SelectField('How do you feel about the current tax rates in California?', choices=[
        ('Much too low', 'Much too low'),
        ('Slightly too low', 'Slightly too low'),
        ('About right', 'About right'),
        ('Slightly too high', 'Slightly too high'),
        ('Much too high', 'Much too high')
    ])
    # ... Add the other form fields here in the same pattern ...
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = SurveyForm()
    if form.validate_on_submit():
        form_data = form.data
        session['form_data'] = form_data
        print(form_data)
        return jsonify(form_data)
    return render_template('form2.html', form=form)


@app.route('/data', methods=['POST'])
def get_data():
    data = request.get_json()
    text=data.get('data')
    user_input = text
    try:
        conversation = ConversationChain(llm=llm,memory=memory)
        output = conversation.predict(input=user_input)
        memory.save_context({"input": user_input}, {"output": output})
        return jsonify({"response":True,"message":output})
    except Exception as e:
        print(e)
        error_message = f'Error: {str(e)}'
        return jsonify({"message":error_message,"response":False})
    
if __name__ == '__main__':
    app.run(debug=True)
