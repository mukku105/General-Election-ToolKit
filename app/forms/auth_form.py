from flask_security.forms import LoginForm
from wtforms import StringField
from wtforms.validators import DataRequired

class CustomLoginForm(LoginForm):
    username = StringField('Username', [DataRequired()])
    