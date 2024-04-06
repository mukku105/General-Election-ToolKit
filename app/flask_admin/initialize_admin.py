import datetime
# from flask_jwt_extended import current_user, jwt_required

from flask import redirect, url_for, request
from flask_admin import Admin, AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from flask_admin.form import SecureForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField

from flask_security import current_user

from app.models.post import Post
from app.models.user import User, Role
from app.models.question import Question

from wtforms_sqlalchemy.fields import QuerySelectMultipleField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired

# Add the missing import statement

class FlaskAdminIndexView(AdminIndexView):
    @expose('/')
    # @jwt_required()
    def index(self):
        return super().index()

class UserForm(SecureForm):
    username = StringField('Username')
    phone_no = StringField('Phone Number')
    full_name = StringField('Full Name')
    password = StringField('Password')
    roles = QuerySelectMultipleField(query_factory=lambda: Role.query.all(), get_label='name')
    active = BooleanField('Active')
    # confirmed_at = StringField('Confirmed At')

class UserAdmin(ModelView):
    form = UserForm
    column_list = ('username', 'phone_no', 
                   'full_name', 'active', 'confirmed_at', 'fs_uniquifier', 'roles')
    column_searchable_list = ('username', 'phone_no', 'full_name')
    column_filters = ('username', 'full_name', 'phone_no', 'active')
    
    def _role_formatter(view, context, model, name):
        return model.role.name
    
    column_formatters = {
        'role_id': _role_formatter
    }

    def on_model_change(self, form, User, is_created):
        User.set_password(form.password.data)
        if form.roles.data:
            User.roles = form.roles.data
        else:
            User.roles = []

        if is_created:
            User.set_uuid()
            User.confirmed_at = datetime.datetime.now()
            
    # def is_accessible(self):
    #     return current_user.is_active and current_user.has_role('admin')

    # def inaccessible_callback(self, name, **kwargs):
    #     # redirect to login page if user doesn't have access
    #     return redirect(url_for('security.login', next=request.url))

class RoleAdmin(ModelView):
    column_list = ('id', 'name', 'description')
    form_columns = ('name', 'description')
    column_searchable_list = ('id', 'name',)
    column_filters = ('id', 'name',)


def create_flask_admin(app, db):
    flask_admin = Admin(app, name='Flask Admin Test', index_view=FlaskAdminIndexView(), template_mode='bootstrap3')
    flask_admin.add_view(ModelView(Post, db.session))
    flask_admin.add_view(UserAdmin(User, db.session))
    flask_admin.add_view(RoleAdmin(Role, db.session))
    flask_admin.add_view(ModelView(Question, db.session))