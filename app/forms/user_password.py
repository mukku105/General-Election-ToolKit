from flask_admin.form import SecureForm
from wtforms import StringField

class UserPasswordForm(SecureForm):
    full_name = StringField('Full Name')
    password = StringField('Password')