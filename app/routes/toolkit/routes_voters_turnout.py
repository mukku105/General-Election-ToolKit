from flask import jsonify, render_template, request, url_for, redirect
from flask_login import current_user, login_required
from app.models.assembly_const import AssemblyConst
from app.routes.toolkit import bp
from app.extensions import db
from app.models.user import User
from app.models.polling_station import PollingStation
from app.models.voters_turnout import VotersTurnout
from sqlalchemy import func, text
from sqlalchemy.orm import Session
from app.helper import calc_ac_turnout

import pandas as pd

@bp.route('/voters_turnout', methods=['GET', 'POST'])
@login_required
def voters_turnout():
    p_station = PollingStation.query.all()
    assembly_const = None
    for role in current_user.roles:
        if role.name.startswith('ac_'):
            ac_no = role.name.split('ac_')[1]
            print(ac_no)
            p_station = PollingStation.query.filter_by(assembly_const_no=ac_no).all()
            assembly_const = AssemblyConst.query.get(ac_no)
            # p_station = VotersTurnout.query.join(PollingStation).filter(PollingStation.assembly_const_no==ac_no).all()
            break

    print(p_station)

    return render_template('toolkit/voter_turnout/index.html', p_station=p_station, assembly_const=assembly_const)

@bp.route('/voters_turnout/get_data', methods=['GET', 'POST'])
@login_required
def voters_turnout_get_data():
    ps_code = request.args.get('ps_code')
    ac_no = request.args.get('ac_no')
    print(ps_code)
    if ps_code:
        voters_turnout = VotersTurnout.query.filter_by(polling_station_code=ps_code).all()
    else :
        voters_turnout = VotersTurnout.query.join(PollingStation).filter(PollingStation.assembly_const_no==ac_no).all()
    response = {}
    voters_turnout_data = {}
    if voters_turnout:
        for vt in voters_turnout:
            polling_station_code = vt.polling_station_code
            vt_data = {
                'id': vt.id,
                'ps_code': vt.polling_station_code,
                '1': {
                    't_male': vt.turnout_male_1 if vt.turnout_male_1 else 0,
                    't_male_percentage': round(vt.turnout_male_percentage_1, 2),
                    't_female': vt.turnout_female_1 if vt.turnout_female_1 else 0,
                    't_female_percentage': round(vt.turnout_female_percentage_1, 2),
                    't_other': vt.turnout_other_1 if vt.turnout_other_1 else 0,
                    't_other_percentage': round(vt.turnout_other_percentage_1, 2),
                    't_total': vt.total_turnout_1 if vt.total_turnout_1 else 0,
                    't_total_percentage': round(vt.turnout_total_percentage_1, 2),

                    't_male_sangha': vt.turnout_male_1_sangha if vt.turnout_male_1_sangha else 0,
                    't_male_percentage_sangha': round(vt.turnout_male_percentage_1_sangha, 2),
                    't_female_sangha': vt.turnout_female_1_sangha if vt.turnout_female_1_sangha else 0,
                    't_female_percentage_sangha': round(vt.turnout_female_percentage_1_sangha, 2),
                    't_other_sangha': vt.turnout_other_1_sangha if vt.turnout_other_1_sangha else 0,
                    't_other_percentage_sangha': round(vt.turnout_other_percentage_1_sangha, 2),
                    't_total_sangha': vt.total_turnout_1_sangha if vt.total_turnout_1_sangha else 0,
                    't_total_percentage_sangha': round(vt.turnout_total_percentage_1_sangha, 2),
                },
                '2': {
                    't_male': vt.turnout_male_2 if vt.turnout_male_2 else 0,
                    't_male_percentage': round(vt.turnout_male_percentage_2, 2),
                    't_female': vt.turnout_female_2 if vt.turnout_female_2 else 0,
                    't_female_percentage': round(vt.turnout_female_percentage_2, 2),
                    't_other': vt.turnout_other_2 if vt.turnout_other_2 else 0,
                    't_other_percentage': round(vt.turnout_other_percentage_2, 2),
                    't_total': vt.total_turnout_2 if vt.total_turnout_2 else 0,
                    't_total_percentage': round(vt.turnout_total_percentage_2, 2),

                    't_male_sangha': vt.turnout_male_2_sangha if vt.turnout_male_2_sangha else 0,
                    't_male_percentage_sangha': round(vt.turnout_male_percentage_2_sangha, 2),
                    't_female_sangha': vt.turnout_female_2_sangha if vt.turnout_female_2_sangha else 0,
                    't_female_percentage_sangha': round(vt.turnout_female_percentage_2_sangha, 2),
                    't_other_sangha': vt.turnout_other_2_sangha if vt.turnout_other_2_sangha else 0,
                    't_other_percentage_sangha': round(vt.turnout_other_percentage_2_sangha, 2),
                    't_total_sangha': vt.total_turnout_2_sangha if vt.total_turnout_2_sangha else 0,
                    't_total_percentage_sangha': round(vt.turnout_total_percentage_2_sangha, 2),
                },
                '3': {
                    't_male': vt.turnout_male_3 if vt.turnout_male_3 else 0,
                    't_male_percentage': round(vt.turnout_male_percentage_3, 2),
                    't_female': vt.turnout_female_3 if vt.turnout_female_3 else 0,
                    't_female_percentage': round(vt.turnout_female_percentage_3, 2),
                    't_other': vt.turnout_other_3 if vt.turnout_other_3 else 0,
                    't_other_percentage': round(vt.turnout_other_percentage_3, 2),
                    't_total': vt.total_turnout_3 if vt.total_turnout_3 else 0,
                    't_total_percentage': round(vt.turnout_total_percentage_3, 2),

                    't_male_sangha': vt.turnout_male_3_sangha if vt.turnout_male_3_sangha else 0,
                    't_male_percentage_sangha': round(vt.turnout_male_percentage_3_sangha, 2),
                    't_female_sangha': vt.turnout_female_3_sangha if vt.turnout_female_3_sangha else 0,
                    't_female_percentage_sangha': round(vt.turnout_female_percentage_3_sangha, 2),
                    't_other_sangha': vt.turnout_other_3_sangha if vt.turnout_other_3_sangha else 0,
                    't_other_percentage_sangha': round(vt.turnout_other_percentage_3_sangha, 2),
                    't_total_sangha': vt.total_turnout_3_sangha if vt.total_turnout_3_sangha else 0,
                    't_total_percentage_sangha': round(vt.turnout_total_percentage_3_sangha, 2),

                },
                '4': {
                    't_male': vt.turnout_male_4 if vt.turnout_male_4 else 0,
                    't_male_percentage': round(vt.turnout_male_percentage_4, 2),
                    't_female': vt.turnout_female_4 if vt.turnout_female_4 else 0,
                    't_female_percentage': round(vt.turnout_female_percentage_4, 2),
                    't_other': vt.turnout_other_4 if vt.turnout_other_4 else 0,
                    't_other_percentage': round(vt.turnout_other_percentage_4, 2),
                    't_total': vt.total_turnout_4 if vt.total_turnout_4 else 0,
                    't_total_percentage': round(vt.turnout_total_percentage_4, 2),

                    't_male_sangha': vt.turnout_male_4_sangha if vt.turnout_male_4_sangha else 0,
                    't_male_percentage_sangha': round(vt.turnout_male_percentage_4_sangha, 2),
                    't_female_sangha': vt.turnout_female_4_sangha if vt.turnout_female_4_sangha else 0,
                    't_female_percentage_sangha': round(vt.turnout_female_percentage_4_sangha, 2),
                    't_other_sangha': vt.turnout_other_4_sangha if vt.turnout_other_4_sangha else 0,
                    't_other_percentage_sangha': round(vt.turnout_other_percentage_4_sangha, 2),
                    't_total_sangha': vt.total_turnout_4_sangha if vt.total_turnout_4_sangha else 0,
                    't_total_percentage_sangha': round(vt.turnout_total_percentage_4_sangha, 2),

                },
                '5': {
                    't_male': vt.turnout_male_5 if vt.turnout_male_5 else 0,
                    't_male_percentage': round(vt.turnout_male_percentage_5, 2),
                    't_female': vt.turnout_female_5 if vt.turnout_female_5 else 0,
                    't_female_percentage': round(vt.turnout_female_percentage_5, 2),
                    't_other': vt.turnout_other_5 if vt.turnout_other_5 else 0,
                    't_other_percentage': round(vt.turnout_other_percentage_5, 2),
                    't_total': vt.total_turnout_5 if vt.total_turnout_5 else 0,
                    't_total_percentage': round(vt.turnout_total_percentage_5, 2),

                    't_male_sangha': vt.turnout_male_5_sangha if vt.turnout_male_5_sangha else 0,
                    't_male_percentage_sangha': round(vt.turnout_male_percentage_5_sangha, 2),
                    't_female_sangha': vt.turnout_female_5_sangha if vt.turnout_female_5_sangha else 0,
                    't_female_percentage_sangha': round(vt.turnout_female_percentage_5_sangha, 2),
                    't_other_sangha': vt.turnout_other_5_sangha if vt.turnout_other_5_sangha else 0,
                    't_other_percentage_sangha': round(vt.turnout_other_percentage_5_sangha, 2),
                    't_total_sangha': vt.total_turnout_5_sangha if vt.total_turnout_5_sangha else 0,
                    't_total_percentage_sangha': round(vt.turnout_total_percentage_5_sangha, 2),

                },
                '6': {
                    't_male': vt.turnout_male_6 if vt.turnout_male_6 else 0,
                    't_male_percentage': round(vt.turnout_male_percentage_6, 2),
                    't_female': vt.turnout_female_6 if vt.turnout_female_6 else 0,
                    't_female_percentage': round(vt.turnout_female_percentage_6, 2),
                    't_other': vt.turnout_other_6 if vt.turnout_other_6 else 0,
                    't_other_percentage': round(vt.turnout_other_percentage_6, 2),
                    't_total': vt.total_turnout_6 if vt.total_turnout_6 else 0,
                    't_total_percentage': round(vt.turnout_total_percentage_6, 2),
                    
                    't_male_sangha': vt.turnout_male_6_sangha if vt.turnout_male_6_sangha else 0,
                    't_male_percentage_sangha': round(vt.turnout_male_percentage_6_sangha, 2),
                    't_female_sangha': vt.turnout_female_6_sangha if vt.turnout_female_6_sangha else 0,
                    't_female_percentage_sangha': round(vt.turnout_female_percentage_6_sangha, 2),
                    't_other_sangha': vt.turnout_other_6_sangha if vt.turnout_other_6_sangha else 0,
                    't_other_percentage_sangha': round(vt.turnout_other_percentage_6_sangha, 2),
                    't_total_sangha': vt.total_turnout_6_sangha if vt.total_turnout_6_sangha else 0,
                    't_total_percentage_sangha': round(vt.turnout_total_percentage_6_sangha, 2),

                },
                # '7': {
                #     't_male': vt.turnout_male_sangha if vt.turnout_male_sangha else 0,
                #     't_female': vt.turnout_female_sangha if vt.turnout_female_sangha else 0,
                #     't_other': vt.turnout_other_sangha if vt.turnout_other_sangha else 0,
                #     't_male_percentage': '-',
                #     't_female_percentage': '-',
                #     't_other_percentage': '-',

                #     't_total': vt.total_turnout_sangha if vt.total_turnout_sangha else 0,
                #     't_total_percentage': '-',
                # },

                '7': {
                    't_male': vt.turnout_male_pc if vt.turnout_male_pc else 0,
                    't_male_percentage': round(vt.turnout_male_percentage_pc, 2),
                    't_female': vt.turnout_female_pc if vt.turnout_female_pc else 0,
                    't_female_percentage': round(vt.turnout_female_percentage_pc, 2),
                    't_other': vt.turnout_other_pc if vt.turnout_other_pc else 0,
                    't_other_percentage': round(vt.turnout_other_percentage_pc, 2),
                    't_total': vt.total_turnout_pc if vt.total_turnout_pc else 0,
                    't_total_percentage': round(vt.turnout_total_percentage_pc, 2),
                },

                'current_turnout_percentage': {
                    'male': round(vt.current_turnout_male, 2),
                    'female': round(vt.current_turnout_female, 2),
                    'other': round(vt.current_turnout_other, 2),
                    'total': round(vt.current_turnout_total, 2),
                },
                
                'actual_ps_voters': {
                    'male': vt.polling_station.electors_male if vt.polling_station.electors_male else 0,
                    'female': vt.polling_station.electors_female if vt.polling_station.electors_female else 0,
                    'other': vt.polling_station.electors_other if vt.polling_station.electors_other else 0,
                    'total': vt.polling_station.electors_total if vt.polling_station.electors_total else 0,
                },
            }
            voters_turnout_data[polling_station_code] = vt_data
    
    response['status'] = 'success'
    response['data'] = voters_turnout_data
    return jsonify(response), 200


@bp.route('/voters_turnout/update', methods=['POST'])
@login_required
def voters_turnout_update():
    response = {}
    data = request.json
    ps_code = data['ps_code']
    data_update = data['data']

    record_exist = True
    print(data)
    vt = VotersTurnout.query.filter_by(polling_station_code=ps_code).first()
    if not vt :
        record_exist = False
        vt = VotersTurnout(polling_station_code=ps_code)

    # Voter-turnout 7AM - 9AM
    vt.turnout_male_1           = data_update['1']['t_male']
    vt.turnout_female_1         = data_update['1']['t_female']
    vt.turnout_other_1          = data_update['1']['t_other']
    vt.turnout_male_1_sangha    = data_update['1']['t_male_sangha']
    vt.turnout_female_1_sangha  = data_update['1']['t_female_sangha']
    vt.turnout_other_1_sangha   = data_update['1']['t_other_sangha']
    # Voter-turnout 9AM - 11AM
    vt.turnout_male_2           = data_update['2']['t_male']
    vt.turnout_female_2         = data_update['2']['t_female']
    vt.turnout_other_2          = data_update['2']['t_other']
    vt.turnout_male_2_sangha    = data_update['2']['t_male_sangha']
    vt.turnout_female_2_sangha  = data_update['2']['t_female_sangha']
    vt.turnout_other_2_sangha   = data_update['2']['t_other_sangha']
    # Voter-turnout 11AM - 1PM
    vt.turnout_male_3           = data_update['3']['t_male']
    vt.turnout_female_3         = data_update['3']['t_female']
    vt.turnout_other_3          = data_update['3']['t_other']
    vt.turnout_male_3_sangha    = data_update['3']['t_male_sangha']
    vt.turnout_female_3_sangha  = data_update['3']['t_female_sangha']
    vt.turnout_other_3_sangha   = data_update['3']['t_other_sangha']
    # Voter-turnout 1PM - 3PM
    vt.turnout_male_4           = data_update['4']['t_male']
    vt.turnout_female_4         = data_update['4']['t_female']
    vt.turnout_other_4          = data_update['4']['t_other']
    vt.turnout_male_4_sangha    = data_update['4']['t_male_sangha']
    vt.turnout_female_4_sangha  = data_update['4']['t_female_sangha']
    vt.turnout_other_4_sangha   = data_update['4']['t_other_sangha']
    # Voter-turnout 3PM - 5PM
    vt.turnout_male_5           = data_update['5']['t_male']
    vt.turnout_female_5         = data_update['5']['t_female']
    vt.turnout_other_5          = data_update['5']['t_other']
    vt.turnout_male_5_sangha    = data_update['5']['t_male_sangha']
    vt.turnout_female_5_sangha  = data_update['5']['t_female_sangha']
    vt.turnout_other_5_sangha   = data_update['5']['t_other_sangha']
    # Voter-turnout 5PM - 7PM (Close of Poll)
    vt.turnout_male_6           = data_update['6']['t_male']
    vt.turnout_female_6         = data_update['6']['t_female']
    vt.turnout_other_6          = data_update['6']['t_other']
    vt.turnout_male_6_sangha    = data_update['6']['t_male_sangha']
    vt.turnout_female_6_sangha  = data_update['6']['t_female_sangha']
    vt.turnout_other_6_sangha   = data_update['6']['t_other_sangha']
    # Total Sangha Voter Turn Out
    vt.turnout_male_pc      = data_update['7']['t_male']
    vt.turnout_female_pc    = data_update['7']['t_female']
    vt.turnout_other_pc     = data_update['7']['t_other']

    if not record_exist:
        db.session.add(vt)

    db.session.commit()
    response['status'] = 'success'
    response['msg'] = 'Data Updated Successfully'

    return jsonify(response), 200


@bp.route('/voters_turnout/get_ac_turnout', methods=['GET'])
@login_required
def get_ac_turnout():
    ac_no = request.args.get('ac_no')
    response_data = calc_ac_turnout.calc_ac_turnout(ac_no)

    return jsonify(response_data), 200

