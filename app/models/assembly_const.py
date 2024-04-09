import datetime
from app.extensions import db

class AssemblyConst(db.Model):
    ac_no = db.Column(db.Integer, primary_key=True)
    ac_name = db.Column(db.String(150))
    ac_category = db.Column(db.String(150))
    remarks = db.Column(db.String(150))
    state = db.Column(db.String(150))
    district = db.Column(db.String(150))

    polling_stations = db.relationship('PollingStation', backref='assembly_const', lazy=True)
    ac_election_officers = db.relationship('AcElectionOfficer', backref='assembly_const', lazy=True)

    last_updated = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    def on_create(self):
        self.created_at = datetime.datetime.now()

    def __repr__(self):
        return f'<PollingStation "{self.ac_no} {self.ac_name}">'