from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SelectMultipleField, widgets, RadioField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp

from constants import STATE_CHOICES, QUESTION_TEXT, LIKERT_CHOICES
from models import VoterInfo


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
