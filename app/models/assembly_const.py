import datetime
from app.extensions import db

class AssemblyConst(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ac_no = db.Column(db.Integer, unique=True, nullable=False)
    ac_name = db.Column(db.String(150))
    ac_category = db.Column(db.String(150))
    remarks = db.Column(db.String(150))
    state = db.Column(db.String(150))
    district = db.Column(db.String(150))

    last_updated = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    def on_create(self):
        self.created_at = datetime.datetime.now()

    def __repr__(self):
        return f'<PollingStation "{self.ps_name}">'