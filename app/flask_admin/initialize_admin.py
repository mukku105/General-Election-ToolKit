import datetime

from flask import redirect, url_for, request
from flask_admin import Admin, AdminIndexView, expose, helpers as admin_helpers
from flask_admin.contrib.sqla import ModelView

from flask_login import login_required
from flask_security import current_user

from app.forms.user_password import UserPasswordForm
from app.models.polling_station import PollingStation
from app.models.post import Post
from app.models.user import User, Role
from app.models.assembly_const import AssemblyConst
from app.models.question import Question
from app.extensions import db

from app.forms.user_form import UserForm
from app.extensions import security

class AdminProtectedModelView(ModelView):
    # pass
    def is_accessible(self):
       return current_user.is_authenticated and current_user.has_role('admin')

    def inaccessible_callback(self, name, **kwargs):
       return redirect(url_for('security.login', next=request.url))
    
class FlaskAdminIndexView(AdminIndexView):
    @expose('/')
    def index(self):
        return super().index()
    
    def is_accessible(self):
        return current_user.is_authenticated and current_user.has_role('admin')
    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('security.login', next=request.url))

class UserPasswordAdmin(AdminProtectedModelView):
    form = UserPasswordForm
    column_list = ('full_name', 'password')
    column_searchable_list = ('full_name', 'password')
    column_filters = ('full_name', 'password')

    def on_model_change(self, form, User, is_created):
        User.set_password(form.password.data)

class UserAdmin(AdminProtectedModelView):
    form = UserForm
    column_list = ( 'email', 'phone_no',
                   'full_name', 'active', 'confirmed_at', 'fs_uniquifier', 'roles')
    column_searchable_list = ( 'email', 'phone_no' , 'full_name')
    column_filters = ('full_name',  'email', 'phone_no', 'active')
    
    def _role_formatter(view, context, model, name):
        return model.role.name
    
    column_formatters = {
        'role_id': _role_formatter
    }

    def on_model_change(self, form, User, is_created):
        # User.set_password(form.password.data)
        if form.roles.data:
            User.roles = form.roles.data
        else:
            User.roles = []
    
        if is_created:
            User.set_password('test')
            User.set_uuid()
            User.confirmed_at = datetime.datetime.now()

class RoleAdmin(AdminProtectedModelView):
    column_list = ('id', 'name', 'description')
    form_columns = ('name', 'description')
    column_searchable_list = ('id', 'name',)
    column_filters = ('id', 'name',)

class PostAdmin(AdminProtectedModelView):
    column_list = ('id', 'title', 'content')
    form_columns = ('title', 'content')
    column_searchable_list = ('title', 'content')
    column_filters = ('title', 'content')

class PollingStationAdmin(AdminProtectedModelView):
    column_list = ('id', 'ac_no', 'part_no', 'part_name', 
                   'ps_no', 'ps_name', 'ps_type', 'ps_category', 'location_type', 
                   'electors_male', 'electors_female', 'electors_other', 'electors_total',
                   'last_updated', 'created_at')
    form_columns = ('ac_no', 'part_no', 'part_name', 
                   'ps_no', 'ps_name', 'ps_type', 'ps_category', 'location_type', 
                   'electors_male', 'electors_female', 'electors_other', 'electors_total',
                   'last_updated', 'created_at')
    column_searchable_list = ('part_name', 'ps_name', 'ps_type', 'ps_category', 'location_type')
    column_filters = ('part_name', 'ps_name', 'ps_type', 'ps_category', 'location_type')

class AssemblyConstAdmin(AdminProtectedModelView):
    column_list = ('id', 'ac_no', 'ac_name', 'ac_category', 'remarks', 'state', 'district', 'last_updated', 'created_at')
    form_columns = ('ac_no', 'ac_name', 'ac_category', 'remarks', 'state', 'district')
    column_searchable_list = ('ac_name', 'ac_category', 'remarks', 'state', 'district')

    def on_model_change(self, form, model, is_created):
        if is_created:
            User.confirmed_at = datetime.datetime.now()



def create_flask_admin(app, db):
    flask_admin = Admin(app, name='Gen. Election ToolKit Admin', index_view=FlaskAdminIndexView(), template_mode='bootstrap3')
    
    # @security.context_processor
    # def security_context_processor():
    #     return dict(
    #         admin_base_template=flask_admin.base_template,
    #         admin_view=flask_admin.index_view,
    #         h=admin_helpers,
    #         get_url=url_for
    #     )
    
    # flask_admin.add_view(ModelView(Post, db.session))
    flask_admin.add_view(UserAdmin(User, db.session))
    flask_admin.add_view(UserPasswordAdmin(User, db.session, endpoint='UserPassword', name='User Password'))
    flask_admin.add_view(RoleAdmin(Role, db.session))
    flask_admin.add_view(PostAdmin(Post, db.session))
    flask_admin.add_view(PollingStationAdmin(PollingStation, db.session))
    flask_admin.add_view(AssemblyConstAdmin(AssemblyConst, db.session))
    flask_admin.add_view(ModelView(Question, db.session))