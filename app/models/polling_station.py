import datetime
from app.extensions import db
from app.models.assembly_const import AssemblyConst


class PollingStation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    assembly_const_no = db.Column(db.Integer, db.ForeignKey('assembly_const.ac_no'), name='fk_assembly_const_no')
    part_no = db.Column(db.Integer, nullable=False)
    part_name = db.Column(db.String(150))
    ps_no = db.Column(db.Integer, unique=True, nullable=False)
    ps_name = db.Column(db.String(150))
    ps_type = db.Column(db.String(150))
    ps_category = db.Column(db.String(150))
    location_type = db.Column(db.String(150))
    electors_male = db.Column(db.Integer)
    electors_female = db.Column(db.Integer)
    electors_other = db.Column(db.Integer)
    electors_total = db.Column(db.Integer)

    last_updated = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    def on_create(self):
        self.created_at = datetime.datetime.now()

    def __repr__(self):
        return f'<PollingStation "{self.ps_name}">'