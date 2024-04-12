import datetime
from app.extensions import db
from sqlalchemy.ext.hybrid import hybrid_property

class VotersTurnout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    polling_station_code = db.Column(db.String(12), db.ForeignKey('polling_station.ps_code'), name='fk_polling_station_code')

    # Voter-turnout 7AM - 9AM
    turnout_male_1 = db.Column(db.Integer, default=0)
    turnout_female_1 = db.Column(db.Integer, default=0)
    turnout_other_1 = db.Column(db.Integer, default=0)

    turnout_male_1_sangha = db.Column(db.Integer, default=0)
    turnout_female_1_sangha = db.Column(db.Integer, default=0)
    turnout_other_1_sangha = db.Column(db.Integer, default=0)
    

    # Voter-turnout 9AM - 11AM
    turnout_male_2 = db.Column(db.Integer, default=0)
    turnout_female_2 = db.Column(db.Integer, default=0)
    turnout_other_2 = db.Column(db.Integer, default=0)

    turnout_male_2_sangha = db.Column(db.Integer, default=0)
    turnout_female_2_sangha = db.Column(db.Integer, default=0)
    turnout_other_2_sangha = db.Column(db.Integer, default=0)

    # Voter-turnout 11AM - 1PM
    turnout_male_3 = db.Column(db.Integer, default=0)
    turnout_female_3 = db.Column(db.Integer, default=0)
    turnout_other_3 = db.Column(db.Integer, default=0)

    turnout_male_3_sangha = db.Column(db.Integer, default=0)
    turnout_female_3_sangha = db.Column(db.Integer, default=0)
    turnout_other_3_sangha = db.Column(db.Integer, default=0)

    # Voter-turnout 1PM - 3PM
    turnout_male_4 = db.Column(db.Integer, default=0)
    turnout_female_4 = db.Column(db.Integer, default=0)
    turnout_other_4 = db.Column(db.Integer, default=0)

    turnout_male_4_sangha = db.Column(db.Integer, default=0)
    turnout_female_4_sangha = db.Column(db.Integer, default=0)
    turnout_other_4_sangha = db.Column(db.Integer, default=0)

    # Voter-turnout 3PM - 5PM
    turnout_male_5 = db.Column(db.Integer, default=0)
    turnout_female_5 = db.Column(db.Integer, default=0)
    turnout_other_5 = db.Column(db.Integer, default=0)

    turnout_male_5_sangha = db.Column(db.Integer, default=0)
    turnout_female_5_sangha = db.Column(db.Integer, default=0)
    turnout_other_5_sangha = db.Column(db.Integer, default=0)

    # Voter-turnout 5PM - 7PM (Close of Poll)
    turnout_male_6 = db.Column(db.Integer, default=0)
    turnout_female_6 = db.Column(db.Integer, default=0)
    turnout_other_6 = db.Column(db.Integer, default=0)

    turnout_male_6_sangha = db.Column(db.Integer, default=0)
    turnout_female_6_sangha = db.Column(db.Integer, default=0)
    turnout_other_6_sangha = db.Column(db.Integer, default=0)

    # # Total Sangha Voter Turn Out
    # turnout_male_sangha = db.Column(db.Integer, default=0)
    # turnout_female_sangha = db.Column(db.Integer, default=0)
    # turnout_other_sangha = db.Column(db.Integer, default=0)

    turnout_male_pc = db.Column(db.Integer, default=0)
    turnout_female_pc = db.Column(db.Integer, default=0)
    turnout_other_pc = db.Column(db.Integer, default=0)

    remarks = db.Column(db.String(150))

    last_updated = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    @hybrid_property
    def total_turnout_1(self):
        return self.turnout_male_1 + self.turnout_female_1 + self.turnout_other_1
    @hybrid_property
    def total_turnout_1_sangha(self):
        return self.turnout_male_1_sangha + self.turnout_female_1_sangha + self.turnout_other_1_sangha
    
    @hybrid_property
    def total_turnout_2(self):
        return self.turnout_male_2 + self.turnout_female_2 + self.turnout_other_2
    @hybrid_property
    def total_turnout_2_sangha(self):
        return self.turnout_male_2_sangha + self.turnout_female_2_sangha + self.turnout_other_2_sangha
    
    @hybrid_property
    def total_turnout_3(self):
        return self.turnout_male_3 + self.turnout_female_3 + self.turnout_other_3
    @hybrid_property
    def total_turnout_3_sangha(self):
        return self.turnout_male_3_sangha + self.turnout_female_3_sangha + self.turnout_other_3_sangha
    
    @hybrid_property
    def total_turnout_4(self):
        return self.turnout_male_4 + self.turnout_female_4 + self.turnout_other_4
    @hybrid_property
    def total_turnout_4_sangha(self):
        return self.turnout_male_4_sangha + self.turnout_female_4_sangha + self.turnout_other_4_sangha
    
    @hybrid_property
    def total_turnout_5(self):
        return self.turnout_male_5 + self.turnout_female_5 + self.turnout_other_5
    @hybrid_property
    def total_turnout_5_sangha(self):
        return self.turnout_male_5_sangha + self.turnout_female_5_sangha + self.turnout_other_5_sangha
    
    @hybrid_property
    def total_turnout_6(self):
        return self.turnout_male_6 + self.turnout_female_6 + self.turnout_other_6
    @hybrid_property
    def total_turnout_6_sangha(self):
        return self.turnout_male_6_sangha + self.turnout_female_6_sangha + self.turnout_other_6_sangha
    
    @hybrid_property
    def total_turnout_pc(self):
        return self.turnout_male_pc + self.turnout_female_pc + self.turnout_other_pc
    
    # @hybrid_property
    # def total_turnout_sangha(self):
    #     return self.turnout_male_sangha + self.turnout_female_sangha + self.turnout_other_sangha
    
    #------------------------------------------------------------------------------------------------
    
    @hybrid_property
    def turnout_male_percentage_1(self):
        return (self.turnout_male_1 / self.polling_station.electors_male) * 100 if self.polling_station.electors_male > 0 else 0
    @hybrid_property
    def turnout_male_percentage_1_sangha(self):
        return (self.turnout_male_1_sangha / self.polling_station.electors_male_sangha) * 100 if self.polling_station.electors_male_sangha > 0 else 0
    
    @hybrid_property
    def turnout_male_percentage_2(self):
        return (self.turnout_male_2 / self.polling_station.electors_male) * 100 if self.polling_station.electors_male > 0 else 0
    @hybrid_property
    def turnout_male_percentage_2_sangha(self):
        return (self.turnout_male_2_sangha / self.polling_station.electors_male_sangha) * 100 if self.polling_station.electors_male_sangha > 0 else 0
    
    @hybrid_property
    def turnout_male_percentage_3(self):
        return (self.turnout_male_3 / self.polling_station.electors_male) * 100 if self.polling_station.electors_male > 0 else 0
    @hybrid_property
    def turnout_male_percentage_3_sangha(self):
        return (self.turnout_male_3_sangha / self.polling_station.electors_male_sangha) * 100 if self.polling_station.electors_male_sangha > 0 else 0
    
    @hybrid_property
    def turnout_male_percentage_4(self):
        return (self.turnout_male_4 / self.polling_station.electors_male) * 100 if self.polling_station.electors_male > 0 else 0
    @hybrid_property
    def turnout_male_percentage_4_sangha(self):
        return (self.turnout_male_4_sangha / self.polling_station.electors_male_sangha) * 100 if self.polling_station.electors_male_sangha > 0 else 0
    
    @hybrid_property
    def turnout_male_percentage_5(self):
        return (self.turnout_male_5 / self.polling_station.electors_male) * 100 if self.polling_station.electors_male > 0 else 0
    @hybrid_property
    def turnout_male_percentage_5_sangha(self):
        return (self.turnout_male_5_sangha / self.polling_station.electors_male_sangha) * 100 if self.polling_station.electors_male_sangha > 0 else 0
    
    @hybrid_property
    def turnout_male_percentage_6(self):
        return (self.turnout_male_6 / self.polling_station.electors_male) * 100 if self.polling_station.electors_male > 0 else 0
    @hybrid_property
    def turnout_male_percentage_6_sangha(self):
        return (self.turnout_male_6_sangha / self.polling_station.electors_male_sangha) * 100 if self.polling_station.electors_male_sangha > 0 else 0
    
    @hybrid_property
    def turnout_male_percentage_pc(self):
        return (self.turnout_male_pc / (self.polling_station.electors_male + self.polling_station.electors_male_sangha)) * 100 if (self.polling_station.electors_male + self.polling_station.electors_male_sangha) > 0 else 0

    #------------------------------------------------------------------------------------------------

    
    @hybrid_property
    def turnout_female_percentage_1(self):
        return (self.turnout_female_1 / self.polling_station.electors_female) * 100 if self.polling_station.electors_female > 0 else 0
    @hybrid_property
    def turnout_female_percentage_1_sangha(self):
        return (self.turnout_female_1_sangha / self.polling_station.electors_female_sangha) * 100 if self.polling_station.electors_female_sangha > 0 else 0
    
    @hybrid_property
    def turnout_female_percentage_2(self):
        return (self.turnout_female_2 / self.polling_station.electors_female) * 100 if self.polling_station.electors_female > 0 else 0
    @hybrid_property
    def turnout_female_percentage_2_sangha(self):
        return (self.turnout_female_2_sangha / self.polling_station.electors_female_sangha) * 100 if self.polling_station.electors_female_sangha > 0 else 0
    
    @hybrid_property
    def turnout_female_percentage_3(self):
        return (self.turnout_female_3 / self.polling_station.electors_female) * 100 if self.polling_station.electors_female > 0 else 0
    @hybrid_property
    def turnout_female_percentage_3_sangha(self):
        return (self.turnout_female_3_sangha / self.polling_station.electors_female_sangha) * 100 if self.polling_station.electors_female_sangha > 0 else 0
    
    @hybrid_property
    def turnout_female_percentage_4(self):
        return (self.turnout_female_4 / self.polling_station.electors_female) * 100 if self.polling_station.electors_female > 0 else 0
    @hybrid_property
    def turnout_female_percentage_4_sangha(self):
        return (self.turnout_female_4_sangha / self.polling_station.electors_female_sangha) * 100 if self.polling_station.electors_female_sangha > 0 else 0
    
    @hybrid_property
    def turnout_female_percentage_5(self):
        return (self.turnout_female_5 / self.polling_station.electors_female) * 100 if self.polling_station.electors_female > 0 else 0
    @hybrid_property
    def turnout_female_percentage_5_sangha(self):
        return (self.turnout_female_5_sangha / self.polling_station.electors_female_sangha) * 100 if self.polling_station.electors_female_sangha > 0 else 0
    
    @hybrid_property
    def turnout_female_percentage_6(self):
        return (self.turnout_female_6 / self.polling_station.electors_female) * 100 if self.polling_station.electors_female > 0 else 0
    @hybrid_property
    def turnout_female_percentage_6_sangha(self):
        return (self.turnout_female_6_sangha / self.polling_station.electors_female_sangha) * 100 if self.polling_station.electors_female_sangha > 0 else 0
    
    @hybrid_property
    def turnout_female_percentage_pc(self):
        return (self.turnout_female_pc / (self.polling_station.electors_female + self.polling_station.electors_female_sangha)) * 100 if (self.polling_station.electors_female + self.polling_station.electors_female_sangha) > 0 else 0
    #------------------------------------------------------------------------------------------------
    
    @hybrid_property
    def turnout_other_percentage_1(self):
        return (self.turnout_other_1 / self.polling_station.electors_other) * 100 if self.polling_station.electors_other > 0 else 0
    @hybrid_property
    def turnout_other_percentage_1_sangha(self):
        return (self.turnout_other_1_sangha / self.polling_station.electors_other_sangha) * 100 if self.polling_station.electors_other_sangha > 0 else 0
    
    @hybrid_property
    def turnout_other_percentage_2(self):
        return (self.turnout_other_2 / self.polling_station.electors_other) * 100 if self.polling_station.electors_other > 0 else 0
    @hybrid_property
    def turnout_other_percentage_2_sangha(self):
        return (self.turnout_other_2_sangha / self.polling_station.electors_other_sangha) * 100 if self.polling_station.electors_other_sangha > 0 else 0
    
    @hybrid_property
    def turnout_other_percentage_3(self):
        return (self.turnout_other_3 / self.polling_station.electors_other) * 100 if self.polling_station.electors_other > 0 else 0
    @hybrid_property
    def turnout_other_percentage_3_sangha(self):
        return (self.turnout_other_3_sangha / self.polling_station.electors_other_sangha) * 100 if self.polling_station.electors_other_sangha > 0 else 0
    
    @hybrid_property
    def turnout_other_percentage_4(self):
        return (self.turnout_other_4 / self.polling_station.electors_other) * 100 if self.polling_station.electors_other > 0 else 0
    @hybrid_property
    def turnout_other_percentage_4_sangha(self):
        return (self.turnout_other_4_sangha / self.polling_station.electors_other_sangha) * 100 if self.polling_station.electors_other_sangha > 0 else 0
    
    @hybrid_property
    def turnout_other_percentage_5(self):
        return (self.turnout_other_5 / self.polling_station.electors_other) * 100 if self.polling_station.electors_other > 0 else 0
    @hybrid_property
    def turnout_other_percentage_5_sangha(self):
        return (self.turnout_other_5_sangha / self.polling_station.electors_other_sangha) * 100 if self.polling_station.electors_other_sangha > 0 else 0
    
    @hybrid_property
    def turnout_other_percentage_6(self):
        return (self.turnout_other_6 / self.polling_station.electors_other) * 100 if self.polling_station.electors_other > 0 else 0
    @hybrid_property
    def turnout_other_percentage_6_sangha(self):
        return (self.turnout_other_6_sangha / self.polling_station.electors_other_sangha) * 100 if self.polling_station.electors_other_sangha > 0 else 0
    
    @hybrid_property
    def turnout_other_percentage_pc(self):
        return (self.turnout_other_pc / (self.polling_station.electors_other + self.polling_station.electors_other_sangha)) * 100 if (self.polling_station.electors_other + self.polling_station.electors_other_sangha) > 0 else 0

    #------------------------------------------------------------------------------------------------
    @hybrid_property
    def turnout_total_percentage_1(self):
        return (self.total_turnout_1 / self.polling_station.electors_total) * 100 if self.polling_station.electors_total > 0 else 0
    @hybrid_property
    def turnout_total_percentage_1_sangha(self):
        return (self.total_turnout_1_sangha / self.polling_station.electors_total_sangha) * 100 if self.polling_station.electors_total_sangha > 0 else 0
    
    @hybrid_property
    def turnout_total_percentage_2(self):
        return (self.total_turnout_2 / self.polling_station.electors_total) * 100 if self.polling_station.electors_total > 0 else 0
    @hybrid_property
    def turnout_total_percentage_2_sangha(self):
        return (self.total_turnout_2_sangha / self.polling_station.electors_total_sangha) * 100 if self.polling_station.electors_total_sangha > 0 else 0
    
    @hybrid_property
    def turnout_total_percentage_3(self):
        return (self.total_turnout_3 / self.polling_station.electors_total) * 100 if self.polling_station.electors_total > 0 else 0
    @hybrid_property
    def turnout_total_percentage_3_sangha(self):
        return (self.total_turnout_3_sangha / self.polling_station.electors_total_sangha) * 100 if self.polling_station.electors_total_sangha > 0 else 0
    
    @hybrid_property
    def turnout_total_percentage_4(self):
        return (self.total_turnout_4 / self.polling_station.electors_total) * 100 if self.polling_station.electors_total > 0 else 0
    @hybrid_property
    def turnout_total_percentage_4_sangha(self):
        return (self.total_turnout_4_sangha / self.polling_station.electors_total_sangha) * 100 if self.polling_station.electors_total_sangha > 0 else 0
    
    @hybrid_property
    def turnout_total_percentage_5(self):
        return (self.total_turnout_5 / self.polling_station.electors_total) * 100 if self.polling_station.electors_total > 0 else 0
    @hybrid_property
    def turnout_total_percentage_5_sangha(self):
        return (self.total_turnout_5_sangha / self.polling_station.electors_total_sangha) * 100 if self.polling_station.electors_total_sangha > 0 else 0
    
    @hybrid_property
    def turnout_total_percentage_6(self):
        return (self.total_turnout_6 / self.polling_station.electors_total) * 100 if self.polling_station.electors_total > 0 else 0
    @hybrid_property
    def turnout_total_percentage_6_sangha(self):
        return (self.total_turnout_6_sangha / self.polling_station.electors_total_sangha) * 100 if self.polling_station.electors_total_sangha > 0 else 0
    
    @hybrid_property
    def turnout_total_percentage_pc(self):
        return (self.total_turnout_pc / (self.polling_station.electors_total + self.polling_station.electors_total_sangha)) * 100 if (self.polling_station.electors_total + self.polling_station.electors_total_sangha) > 0 else 0
    
    

    @hybrid_property
    def current_turnout_male(self):
        return ((self.turnout_male_1 + self.turnout_male_2 + self.turnout_male_3 + self.turnout_male_4 + self.turnout_male_6)/self.polling_station.electors_male) * 100 if self.polling_station.electors_male > 0 else 0
    @hybrid_property
    def current_turnout_female(self):
        return ((self.turnout_female_1 + self.turnout_female_2 + self.turnout_female_3 + self.turnout_female_4 + self.turnout_female_6)/self.polling_station.electors_female) * 100 if self.polling_station.electors_female > 0 else 0
    @hybrid_property
    def current_turnout_other(self):
        return ((self.turnout_other_1 + self.turnout_other_2 + self.turnout_other_3 + self.turnout_other_4 + self.turnout_other_6)/self.polling_station.electors_other) * 100 if self.polling_station.electors_other > 0 else 0
    @hybrid_property
    def current_turnout_total(self):
        return ((self.total_turnout_1 + self.total_turnout_2 + self.total_turnout_3 + self.total_turnout_4 + self.total_turnout_6)/self.polling_station.electors_total) * 100 if self.polling_station.electors_total > 0 else 0



    def on_create(self):
        self.created_at = datetime.datetime.now()

    def __repr__(self):
        return f'<PsElectionOfficer "{self.polling_station_code}">'