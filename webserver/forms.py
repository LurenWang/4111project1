from flask.ext.wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

class CreateAccountForm(Form):
    username = StringField('Username', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])
    contact_info = StringField('Contact')
    description = StringField('description')

class LoginForm(Form):
    username = StringField('Username', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])
