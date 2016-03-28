from flask.ext.wtf import Form
from wtforms import StringField, TextField, IntegerField, validators
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

class CreateSessionForm(Form):
    title = StringField('Title', validators=[DataRequired()])
    start_time = StringField('Time', validators=[DataRequired()])
    length = IntegerField('Length', validators=[DataRequired(), 
        validators.NumberRange(min=0, max=999)])
    location = StringField('Location', validators=[DataRequired()])
    description = StringField('Description')

class PostForm(Form):
    post = TextField('Post', validators=[DataRequired()])

class CommentForm(Form):
    comment = TextField('Comment', validators=[DataRequired()])
