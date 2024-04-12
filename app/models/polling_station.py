import datetime
from app.extensions import db
from app.models.assembly_const import AssemblyConst
from sqlalchemy.ext.hybrid import hybrid_property


class PollingStation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    assembly_const_no = db.Column(db.Integer, db.ForeignKey('assembly_const.ac_no'), name='fk_assembly_const_no')
    part_no = db.Column(db.Integer, nullable=False)
    part_name = db.Column(db.String(150))
    ps_no = db.Column(db.Integer, unique=True, nullable=False)
    ps_code = db.Column(db.String(12), unique=True, index=True)
    ps_name = db.Column(db.String(150))
    ps_type = db.Column(db.String(150))
    ps_category = db.Column(db.String(150))
    location_type = db.Column(db.String(150))
    electors_male = db.Column(db.Integer, default=0)
    electors_female = db.Column(db.Integer, default=0)
    electors_other = db.Column(db.Integer, default=0)
    electors_total = db.Column(db.Integer, default=0)

    is_sangha = db.Column(db.Boolean, default=False)
    electors_male_sangha = db.Column(db.Integer, default=0)
    electors_female_sangha = db.Column(db.Integer, default=0)
    electors_other_sangha = db.Column(db.Integer, default=0)
    electors_total_sangha = db.Column(db.Integer, default=0)

    ps_election_officers = db.relationship('PsElectionOfficer', backref='polling_station', lazy=True)
    voters_turnouts = db.relationship('VotersTurnout', backref='polling_station', lazy=True)

    last_updated = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    # @hybrid_property
    # def ps_code(self):
    #     return f'{self.assembly_const_no if self.assembly_const_no > 9 else '0' + str(self.assembly_const_no)}/{self.part_no}'

    def on_create(self):
        self.created_at = datetime.datetime.now()
        
    def __repr__(self):
        return f'<PollingStation "{self.ps_name}">'