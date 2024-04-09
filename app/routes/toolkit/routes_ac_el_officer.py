import datetime
from flask import jsonify, render_template, request, url_for, redirect
from flask_login import current_user, login_required
from app.models.assembly_const import AssemblyConst
from app.routes.toolkit import bp
from app.extensions import db
from app.models.user import User
from app.models.polling_station import PollingStation
from app.models.ac_election_officer import AcElectionOfficer
from app.helper.generate_comm_plan import generate_comm_plan

import pandas as pd

@bp.route('/elofficers/ac', methods=['GET', 'POST'])
@login_required
def elofficers_ac():
    ac_election_officers = AcElectionOfficer.query.all()
    for role in current_user.roles:
        if role.name.startswith('ac_'):
            ac_no = role.name.split('ac_')[1]
            ac_election_officers = AcElectionOfficer.query.filter_by(assembly_const_no=ac_no).all()
            break
    
    return render_template('toolkit/comm_plan/index.html', ac_election_officers=ac_election_officers)

# @bp.route('/ps/list', methods=['GET', 'POST'])
# @login_required
# def ps_list():
#     p_station = PollingStation.query.all()

#     # json rest response
#     return jsonify([p.serialize for p in p_station])

# @bp.route('/ps/update', methods=['POST'])
# @login_required
# def ps_update():
#     data = request.get_json()
#     p = PollingStation.query.get(data['id'])
#     p.part_no           = data['part_no']
#     p.part_name         = data['part_name']
#     p.ps_no             = data['ps_no']
#     p.ps_name           = data['ps_name']
#     p.ps_type           = data['ps_type']
#     p.ps_category       = data['ps_category']
#     p.location_type     = data['location_type']
#     p.electors_male     = data['electors_male']
#     p.electors_female   = data['electors_female']
#     p.electors_other    = data['electors_other']
#     p.electors_total    = data['electors_total']

#     db.session.commit()
#     return jsonify({'msg': 'Data updated successfully'}), 200

# @bp.route('/ps/delete', methods=['POST'])
# @login_required
# def ps_delete():
#     data = request.get_json()
#     p = PollingStation.query.get(data['id'])
#     db.session.delete(p)
#     db.session.commit()
#     return jsonify({'msg': 'Data deleted successfully'}), 200

@bp.route('/elofficers/ac/list', methods=['GET', 'POST'])
@login_required
def elofficers_ac_list():
    pass

@bp.route('/elofficers/ac/update', methods=['POST'])
@login_required
def elofficers_ac_update():
    pass

@bp.route('/elofficers/ac/delete', methods=['POST'])
@login_required
def elofficers_ac_delete():
    pass

@bp.route('/elofficers/ac/import', methods=['POST'])
@login_required
def elofficers_ac_import():
    # pass
    if 'file' not in request.files:
        return jsonify({'msg': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'msg': 'No selected file'}), 400
    if not file.filename.endswith('.xlsx'):
        return jsonify({'msg': 'Invalid file extension'}), 400
    
    df = pd.read_excel(file)

    for index, row in df.iterrows():
        officer = AcElectionOfficer.query.filter_by(assembly_const_no=row['AC'], phone_no=row['PHNO']).first()
        if officer is None:
            officer = AcElectionOfficer()

            officer.assembly_const_no = row['AC']
            officer.designation = row['DESIGNATION']
            officer.designation_full = row['DESIGNATION_FULL']
            officer.name = row['NAME']
            officer.office = row['OFFICE']
            officer.phone_no = row['PHNO']

            db.session.add(officer)

    db.session.commit()
    return jsonify({'msg': 'Data imported successfully'}), 200


@bp.route('/elofficers/ac/gen_comm_plan', methods=['POST'])
@login_required
def elofficers_ac_gen_comm_plan():
    ac_no = request.form.get('ac_no')
    file_name = 'AC_' + ac_no + '_Election_Officers_List-' + datetime.datetime.now().strftime('%Y%m%d%H%M%S')+'.docx'
    generate_comm_plan(ac_no, file_name)

    return jsonify({
        'status': 'success',
        'msg': 'Communication plan generated successfully', 
        'ac_no': ac_no, 
        'url': url_for('static', filename='generated_file/comm_plan/' + file_name)
        }), 200
