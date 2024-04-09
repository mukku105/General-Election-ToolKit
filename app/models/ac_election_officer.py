import datetime
from app.extensions import db

class AcElectionOfficer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    assembly_const_no = db.Column(db.Integer, db.ForeignKey('assembly_const.ac_no'), name='fk_assembly_const_no')
    designation = db.Column(db.String(150))
    designation_full = db.Column(db.String(150))
    name = db.Column(db.String(150))
    office = db.Column(db.String(150))
    phone_no = db.Column(db.String(150))

    remarks = db.Column(db.String(150))

    last_updated = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    def on_create(self):
        self.created_at = datetime.datetime.now()

    def __repr__(self):
        return f'<PollingStation "{self.assembly_const_no} | {self.designation} | {self.name} | {self.office}">'