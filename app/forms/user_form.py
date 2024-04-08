from flask_admin.form import SecureForm
from wtforms import StringField, BooleanField
from wtforms_sqlalchemy.fields import QuerySelectMultipleField
from app.models.user import Role

class UserForm(SecureForm):
    # username = StringField('Username')
    email = StringField('Email')
    phone_no = StringField('Phone Number')
    full_name = StringField('Full Name')
    # password = StringField('Password')
    roles = QuerySelectMultipleField(query_factory=lambda: Role.query.all(), get_label='name')
    active = BooleanField('Active')
    # confirmed_at = StringField('Confirmed At')