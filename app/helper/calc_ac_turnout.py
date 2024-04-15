from app.extensions import db
from sqlalchemy import func, text
from sqlalchemy.orm import Session

def calc_ac_turnout(ac_no):
    total_turnout_male_ac = {}
    total_turnout_male_ac_sangha = {}
    total_turnout_female_ac = {}
    total_turnout_female_ac_sangha = {}
    total_turnout_other_ac = {}
    total_turnout_other_ac_sangha = {}
    total_turnout_male_ac_percent = {}
    total_turnout_female_ac_percent = {}
    total_turnout_other_ac_percent = {}

    total_turnout_male_sangha_ac = {}
    total_turnout_female_sangha_ac = {}
    total_turnout_other_sangha_ac = {}
    total_turnout_male_sangha_ac_percent = {}
    total_turnout_female_sangha_ac_percent = {}
    total_turnout_other_sangha_ac_percent = {}

    total_turnout_male_pc = {}
    total_turnout_female_pc = {}
    total_turnout_other_pc = {}
    total_turnout_male_pc_percent = {}
    total_turnout_female_pc_percent = {}
    total_turnout_other_pc_percent = {}

    total_turnout_current = 0

    total_electors = {}
    total_electors_sangha = {}
    total_electors_percent = {}

    response_data = {}

    total_query_sql = text("""
                            SELECT 
                                sum(voters_turnout.turnout_male_1) as tm_1, 
                                sum(voters_turnout.turnout_male_1_sangha) as tm_1_sangha,
                                sum(voters_turnout.turnout_male_2) as tm_2,
                                sum(voters_turnout.turnout_male_2_sangha) as tm_2_sangha,
                                sum(voters_turnout.turnout_male_3) as tm_3,
                                sum(voters_turnout.turnout_male_3_sangha) as tm_3_sangha,
                                sum(voters_turnout.turnout_male_4) as tm_4,
                                sum(voters_turnout.turnout_male_4_sangha) as tm_4_sangha,
                                sum(voters_turnout.turnout_male_5) as tm_5,
                                sum(voters_turnout.turnout_male_5_sangha) as tm_5_sangha,
                                sum(voters_turnout.turnout_male_6) as tm_6,
                                sum(voters_turnout.turnout_male_6_sangha) as tm_6_sangha,
                                sum(voters_turnout.turnout_male_pc) as tm_pc,

                                sum(voters_turnout.turnout_female_1) as tf_1, 
                                sum(voters_turnout.turnout_female_1_sangha) as tf_1_sangha, 
                                sum(voters_turnout.turnout_female_2) as tf_2,
                                sum(voters_turnout.turnout_female_2_sangha) as tf_2_sangha,
                                sum(voters_turnout.turnout_female_3) as tf_3,
                                sum(voters_turnout.turnout_female_3_sangha) as tf_3_sangha,
                                sum(voters_turnout.turnout_female_4) as tf_4,
                                sum(voters_turnout.turnout_female_4_sangha) as tf_4_sangha,
                                sum(voters_turnout.turnout_female_5) as tf_5,
                                sum(voters_turnout.turnout_female_5_sangha) as tf_5_sangha,
                                sum(voters_turnout.turnout_female_6) as tf_6,
                                sum(voters_turnout.turnout_female_6_sangha) as tf_6_sangha,
                                sum(voters_turnout.turnout_female_pc) as tf_pc,

                                sum(voters_turnout.turnout_other_1) as to_1, 
                                sum(voters_turnout.turnout_other_1_sangha) as to_1_sangha, 
                                sum(voters_turnout.turnout_other_2) as to_2,
                                sum(voters_turnout.turnout_other_2_sangha) as to_2_sangha,
                                sum(voters_turnout.turnout_other_3) as to_3,
                                sum(voters_turnout.turnout_other_3_sangha) as to_3_sangha,
                                sum(voters_turnout.turnout_other_4) as to_4,
                                sum(voters_turnout.turnout_other_4_sangha) as to_4_sangha,
                                sum(voters_turnout.turnout_other_5) as to_5,
                                sum(voters_turnout.turnout_other_5_sangha) as to_5_sangha,
                                sum(voters_turnout.turnout_other_6) as to_6,
                                sum(voters_turnout.turnout_other_6_sangha) as to_6_sangha,
                                sum(voters_turnout.turnout_other_pc) as to_pc,

                                sum(polling_station.electors_male) as em,
                                sum(polling_station.electors_male_sangha) as em_sangha,
                                sum(polling_station.electors_female) as ef,
                                sum(polling_station.electors_female_sangha) as ef_sangha,
                                sum(polling_station.electors_other) as eo,
                                sum(polling_station.electors_other_sangha) as eo_sangha,
                                sum(polling_station.electors_total) as et,
                                sum(polling_station.electors_total_sangha) as et_sangha
                            FROM 
                                polling_station 
                            LEFT JOIN voters_turnout
                            ON polling_station.ps_code = voters_turnout.fk_polling_station_code
                            WHERE fk_assembly_const_no = :ac_no
                          """)
    
    session = Session(bind=db.engine)
    total_query = session.execute(total_query_sql, {'ac_no': ac_no})
    total_query = total_query.fetchone()
    session.close()

    total_turnout_male_ac['1'] = total_query.tm_1 if total_query.tm_1 else 0
    total_turnout_male_ac_sangha['1'] = total_query.tm_1_sangha if total_query.tm_1_sangha else 0
    total_turnout_male_ac['2'] = total_query.tm_2 if total_query.tm_2 else 0
    total_turnout_male_ac_sangha['2'] = total_query.tm_2_sangha if total_query.tm_2_sangha else 0
    total_turnout_male_ac['3'] = total_query.tm_3 if total_query.tm_3 else 0
    total_turnout_male_ac_sangha['3'] = total_query.tm_3_sangha if total_query.tm_3_sangha else 0
    total_turnout_male_ac['4'] = total_query.tm_4 if total_query.tm_4 else 0
    total_turnout_male_ac_sangha['4'] = total_query.tm_4_sangha if total_query.tm_4_sangha else 0
    total_turnout_male_ac['5'] = total_query.tm_5 if total_query.tm_5 else 0
    total_turnout_male_ac_sangha['5'] = total_query.tm_5_sangha if total_query.tm_5_sangha else 0
    total_turnout_male_ac['6'] = total_query.tm_6 if total_query.tm_6 else 0
    total_turnout_male_ac_sangha['6'] = total_query.tm_6_sangha if total_query.tm_6_sangha else 0
    total_turnout_male_ac['pc'] = total_query.tm_pc if total_query.tm_pc else 0

    total_turnout_female_ac['1'] = total_query.tf_1 if total_query.tf_1 else 0
    total_turnout_female_ac_sangha['1'] = total_query.tf_1_sangha if total_query.tf_1_sangha else 0
    total_turnout_female_ac['2'] = total_query.tf_2 if total_query.tf_2 else 0
    total_turnout_female_ac_sangha['2'] = total_query.tf_2_sangha if total_query.tf_2_sangha else 0
    total_turnout_female_ac['3'] = total_query.tf_3 if total_query.tf_3 else 0
    total_turnout_female_ac_sangha['3'] = total_query.tf_3_sangha if total_query.tf_3_sangha else 0
    total_turnout_female_ac['4'] = total_query.tf_4 if total_query.tf_4 else 0
    total_turnout_female_ac_sangha['4'] = total_query.tf_4_sangha if total_query.tf_4_sangha else 0
    total_turnout_female_ac['5'] = total_query.tf_5 if total_query.tf_5 else 0
    total_turnout_female_ac_sangha['5'] = total_query.tf_5_sangha if total_query.tf_5_sangha else 0
    total_turnout_female_ac['6'] = total_query.tf_6 if total_query.tf_6 else 0
    total_turnout_female_ac_sangha['6'] = total_query.tf_6_sangha if total_query.tf_6_sangha else 0
    total_turnout_female_ac['pc'] = total_query.tf_pc if total_query.tf_pc else 0

    total_turnout_other_ac['1'] = total_query.to_1 if total_query.to_1 else 0
    total_turnout_other_ac_sangha['1'] = total_query.to_1_sangha if total_query.to_1_sangha else 0
    total_turnout_other_ac['2'] = total_query.to_2 if total_query.to_2 else 0
    total_turnout_other_ac_sangha['2'] = total_query.to_2_sangha if total_query.to_2_sangha else 0
    total_turnout_other_ac['3'] = total_query.to_3 if total_query.to_3 else 0
    total_turnout_other_ac_sangha['3'] = total_query.to_3_sangha if total_query.to_3_sangha else 0
    total_turnout_other_ac['4'] = total_query.to_4 if total_query.to_4 else 0
    total_turnout_other_ac_sangha['4'] = total_query.to_4_sangha if total_query.to_4_sangha else 0
    total_turnout_other_ac['5'] = total_query.to_5 if total_query.to_5 else 0
    total_turnout_other_ac_sangha['5'] = total_query.to_5_sangha if total_query.to_5_sangha else 0
    total_turnout_other_ac['6'] = total_query.to_6 if total_query.to_6 else 0
    total_turnout_other_ac_sangha['6'] = total_query.to_6_sangha if total_query.to_6_sangha else 0
    total_turnout_other_ac['pc'] = total_query.to_pc if total_query.to_pc else 0

    total_electors['male'] = total_query.em if total_query.em else 0
    total_electors_sangha['male'] = total_query.em_sangha if total_query.em_sangha else 0
    total_electors['female'] = total_query.ef if total_query.ef else 0
    total_electors_sangha['female'] = total_query.ef_sangha if total_query.ef_sangha else 0
    total_electors['other'] = total_query.eo if total_query.eo else 0
    total_electors_sangha['other'] = total_query.eo_sangha if total_query.eo_sangha else 0
    total_electors['total'] = total_query.et if total_query.et else 0
    total_electors_sangha['total'] = total_query.et_sangha if total_query.et_sangha else 0

    total_turnout_current_ac = max(total_turnout_male_ac.values()) + max(total_turnout_female_ac.values()) + max(total_turnout_other_ac.values())
    total_turnout_current_ac_sangha = max(total_turnout_male_ac_sangha.values()) + max(total_turnout_female_ac_sangha.values()) + max(total_turnout_other_ac_sangha.values())
    total_turnout_current_pc = total_turnout_current_ac + total_turnout_current_ac_sangha


    # total_turnout_male_ac['1'] = tm_1 if tm_1 else 0

    data = {
        'total_turnout_male_ac': total_turnout_male_ac,
        'total_turnout_male_ac_sangha': total_turnout_male_ac_sangha,
        'total_turnout_female_ac': total_turnout_female_ac,
        'total_turnout_female_ac_sangha': total_turnout_female_ac_sangha,
        'total_turnout_other_ac': total_turnout_other_ac,
        'total_turnout_other_ac_sangha': total_turnout_other_ac_sangha,
        'total_turnout_male_ac_percent': (max(total_turnout_male_ac.values())/total_electors['male'])*100,
        'total_turnout_female_ac_percent': (max(total_turnout_female_ac.values())/total_electors['female'])*100,
        'total_turnout_other_ac_percent': (max(total_turnout_other_ac.values())/total_electors['other'])*100 if total_electors['other'] > 0 else 0,

        # 'total_turnout_male_sangha_ac': total_turnout_male_sangha_ac,
        # 'total_turnout_female_sangha_ac': total_turnout_female_sangha_ac,
        # 'total_turnout_other_sangha_ac': total_turnout_other_sangha_ac,
        # 'total_turnout_male_sangha_ac_percent': (total_turnout_male_sangha_ac_percent)*100,
        # 'total_turnout_female_sangha_ac_percent': (total_turnout_female_sangha_ac_percent)*100,
        # 'total_turnout_other_sangha_ac_percent': (total_turnout_other_sangha_ac_percent)*100,

        'total_turnout_male_pc': total_turnout_male_pc,
        'total_turnout_female_pc': total_turnout_female_pc,
        'total_turnout_other_pc': total_turnout_other_pc,
        # 'total_turnout_male_ac_pc_percent': (total_turnout_male_ac_pc)*100,
        # 'total_turnout_female_ac_pc_percent': (total_turnout_female_ac_pc)*100,
        # 'total_turnout_other_ac_pc_percent': (total_turnout_other_ac_pc)*100,

        'total_electors': total_electors,
        'total_electors_sangha': total_electors_sangha,
        'total_turnout_current_ac': total_turnout_current_ac,
        'total_turnout_current_ac_sangha': total_turnout_current_ac_sangha,
        'total_turnout_current_ac_percent': round((total_turnout_current_ac/total_electors['total'])*100, 2),
        'total_turnout_current_pc': total_turnout_current_pc,
        'total_turnout_current_pc_percent': round((total_turnout_current_pc/(total_electors['total'] + total_electors_sangha['total']))*100 if (total_electors['total'] + total_electors_sangha['total']) > 0 else 0, 2),
        'total_turnout_current_ac_sangha_percent': round((total_turnout_current_ac_sangha/total_electors_sangha['total'])*100 if total_electors_sangha['total'] > 0 else 0, 2),
    }

    response_data['status'] = 'success'
    response_data['data'] = data
    response_data['ac_no'] = ac_no

    return response_data