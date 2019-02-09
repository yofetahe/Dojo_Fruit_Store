from flask_wtf import Form
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length

class PersonalInfo(Form):
    name = StringField('Name: ', validators=[DataRequired("Name is required")])
    yourid = StringField('Your Student ID: ', validators=[DataRequired("Your ID is required")])
    straw = SelectField('Strawberry', choices=[('0','0'), ('1', '1')])
    ras = SelectField('Raspberry', choices=[('0','0'), ('1', '1')])
    app = SelectField('Apple', choices=[('0','0'), ('1', '1')])
    submit = SubmitField('Buy Me Stuff')