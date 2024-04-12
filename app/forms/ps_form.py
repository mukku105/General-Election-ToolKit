from flask_admin.form import SecureForm
from wtforms import IntegerField, StringField, BooleanField
from wtforms_sqlalchemy.fields import QuerySelectField
from app.models.polling_station import PollingStation
from app.models.assembly_const import AssemblyConst

class PollingStationForm(SecureForm):
    assembly_const_no = QuerySelectField(query_factory=lambda: AssemblyConst.query.all(), get_label='ac_name')
    part_no = IntegerField('Part No')
    part_name = StringField('Part Name')
    ps_no = IntegerField('PS No')
    ps_name = StringField('PS Name')
    ps_type = StringField('PS Type')
    ps_category = StringField('PS Category')
    location_type = StringField('Location Type')
    electors_male = IntegerField('electors_male')
    electors_female = IntegerField('electors_female')
    electors_other = IntegerField('electors_other')
    electors_total = IntegerField('electors_total')
    is_sangha = BooleanField('Is Sanga')
    electors_male_sangha = IntegerField('electors_male_sangha')
    electors_female_sangha  =   IntegerField('electors_female_sangha')
    electors_other_sangha = IntegerField('electors_other_sangha')
    electors_total_sangha = IntegerField('electors_total_sangha')