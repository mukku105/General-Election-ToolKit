import datetime

from flask import redirect, url_for, request
from flask_admin import Admin, AdminIndexView, expose, helpers as admin_helpers
from flask_admin.contrib.sqla import ModelView

from flask_login import login_required
from flask_security import current_user

from app.forms.user_password import UserPasswordForm
from app.models.polling_station import PollingStation
from app.models.ac_election_officer import AcElectionOfficer
from app.models.ps_election_officer import PsElectionOfficer
from app.models.voters_turnout import VotersTurnout
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
    column_list = ('id', 'assembly_const_no', 'part_no', 'part_name', 
                   'ps_no', 'ps_code', 'ps_name', 'ps_type', 'ps_category', 'location_type', 
                   'electors_male', 'electors_female', 'electors_other', 'electors_total',
                   'is_sangha',
                   'electors_male_sangha', 'electors_female_sangha', 'electors_other_sangha', 'electors_total_sangha',)
    # form = PollingStationForm
    form_columns = ('assembly_const_no', 'part_no', 'part_name', 
                   'ps_no', 'ps_name', 'ps_type', 'ps_category', 'location_type', 
                   'electors_male', 'electors_female', 'electors_other', 'electors_total',
                   'is_sangha',
                   'electors_male_sangha', 'electors_female_sangha', 'electors_other_sangha', 'electors_total_sangha',
                   'last_updated', 'created_at')
    column_searchable_list = ('part_name', 'ps_code', 'ps_name', 'ps_type', 'ps_category', 'location_type')
    column_filters = ('part_name', 'ps_code', 'ps_name', 'ps_type', 'ps_category', 'location_type')

    # def _ac_formatter(view, context, model, name):
    #     return model.assembly_const.ac_name

    def on_model_change(self, form, model, is_created):
        PollingStation.ps_code = f"{(model.assembly_const_no if int(model.assembly_const_no) > 9 else '0' + str(model.assembly_const_no))}/{model.part_no}"

    # column_formatters = {
    #     'assembly_const_no': _ac_formatter
    # }

class AssemblyConstAdmin(AdminProtectedModelView):
    column_list = ('ac_no', 'ac_name', 'ac_category', 'remarks', 'state', 'district', 'last_updated', 'created_at')
    form_columns = ('ac_no', 'ac_name', 'ac_category', 'remarks', 'state', 'district')
    column_searchable_list = ('ac_name', 'ac_category', 'remarks', 'state', 'district')

    form_choices = {
        'state': [
            ('Sikkim', 'Sikkim'),
        ],
        'district': [
            ('Gangtok', 'Gangtok'),
            ('Mangan', 'Mangan'),
            ('Namchi', 'Namchi'),
            ('Gyalshing', 'Gyalshing'),
            ('Pakyong', 'Pakyong'),
            ('Soreng', 'Soreng'),
        ],
    }

    def on_model_change(self, form, model, is_created):
        if is_created:
            User.confirmed_at = datetime.datetime.now()

class AcElectionOfficerAdmin(AdminProtectedModelView):
    column_list = ('id','assembly_const_no', 'designation', 'designation_full', 'name', 'office', 'phone_no', 'remarks', 'last_updated', 'created_at')
    form_columns = ('assembly_const_no', 'designation', 'designation_full', 'name', 'office', 'phone_no', 'remarks')
    column_searchable_list = ('designation', 'designation_full', 'name', 'office', 'phone_no', 'remarks')

    # form_choices = {
    #     'designation': [
    #         ('RO', 'RO'),
    #         ('ARO', 'ADM'),
    #         ('SM', 'DC'),
    #         ('SPO', 'SPO')
    #         ]
    # }

    def on_model_change(self, form, model, is_created):
        if is_created:
            User.confirmed_at = datetime.datetime.now()

class PsElectionOfficerAdmin(AdminProtectedModelView):
    column_list = ('id', 'polling_station_code', 'presiding_officer', 'polling_officer_1', 'micro_observers', 'block_level_officer', 'remarks', 'last_updated', 'created_at')
    form_columns = ('polling_station_code', 'presiding_officer', 'polling_officer_1', 'micro_observers', 'block_level_officer', 'remarks')
    column_searchable_list = ('presiding_officer', 'polling_officer_1', 'micro_observers', 'block_level_officer', 'remarks')

    def on_model_change(self, form, model, is_created):
        if is_created:
            User.confirmed_at = datetime.datetime.now()

# class VotersTurnoutAdmin(AdminProtectedModelView):
#     column_list = ('id', 'polling_station_code', 
#                    'turnout_male_1', 'turnout_female_1', 'turnout_other_1',
#                    'turnout_male_2', 'turnout_female_2', 'turnout_other_2',
#                    'turnout_male_3', 'turnout_female_3', 'turnout_other_3',
#                    'turnout_male_4', 'turnout_female_4', 'turnout_other_4',
#                    'turnout_male_5', 'turnout_female_5', 'turnout_other_5',
#                    'turnout_male_6', 'turnout_female_6', 'turnout_other_6',
#                    'turnout_male_sangha', 'turnout_female_sangha', 'turnout_other_sangha',
#                      'remarks', 'last_updated', 'created_at')


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
    flask_admin.add_view(ModelView(Question, db.session))
    flask_admin.add_view(UserAdmin(User, db.session))
    flask_admin.add_view(UserPasswordAdmin(User, db.session, endpoint='UserPassword', name='User Password'))
    flask_admin.add_view(RoleAdmin(Role, db.session))
    flask_admin.add_view(PostAdmin(Post, db.session))
    flask_admin.add_view(PollingStationAdmin(PollingStation, db.session))
    flask_admin.add_view(AssemblyConstAdmin(AssemblyConst, db.session))
    flask_admin.add_view(AcElectionOfficerAdmin(AcElectionOfficer, db.session))
    flask_admin.add_view(PsElectionOfficerAdmin(PsElectionOfficer, db.session))
    flask_admin.add_view(ModelView(VotersTurnout, db.session))