import datetime
from app.extensions import db

class PsElectionOfficer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    polling_station_code = db.Column(db.String(12), db.ForeignKey('polling_station.ps_code'), name='fk_polling_station_code')

    presiding_officer = db.Column(db.String(150))
    polling_officer_1 = db.Column(db.String(150))
    micro_observers = db.Column(db.String(150))
    block_level_officer = db.Column(db.String(150))

    remarks = db.Column(db.String(150))

    last_updated = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    def on_create(self):
        self.created_at = datetime.datetime.now()

    def __repr__(self):
        return f'<PsElectionOfficer "{self.polling_station_code} | {self.presiding_officer}">'