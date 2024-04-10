from flask import jsonify, render_template, request, url_for, redirect
from flask_login import current_user, login_required
from app.models.assembly_const import AssemblyConst
from app.routes.toolkit import bp
from app.extensions import db
from app.models.user import User
from app.models.polling_station import PollingStation

import pandas as pd

@bp.route('/ps', methods=['GET', 'POST'])
@login_required
def ps():
    p_station = PollingStation.query.all()
    for role in current_user.roles:
        if role.name.startswith('ac_'):
            ac_no = role.name.split('ac_')[1]
            p_station = PollingStation.query.filter_by(assembly_const_no=ac_no).all()
            break
    
    electors_mtotal = sum([p.electors_male for p in p_station])
    electors_ftotal = sum([p.electors_female for p in p_station])
    electors_ototal = sum([p.electors_other for p in p_station])
    electors_gtotal = sum([p.electors_total for p in p_station])

    el_grand_total = {
                        'mtotal': electors_mtotal, 
                        'ftotal': electors_ftotal, 
                        'ototal': electors_ototal,
                        'gtotal': electors_gtotal
                    }

    return render_template('toolkit/polling_station/index.html', p_station=p_station, el_grand_total=el_grand_total)

@bp.route('/ps/list', methods=['GET', 'POST'])
@login_required
def ps_list():
    p_station = PollingStation.query.all()

    # json rest response
    return jsonify([p.serialize for p in p_station])

@bp.route('/ps/update', methods=['POST'])
@login_required
def ps_update():
    data = request.get_json()
    p = PollingStation.query.get(data['id'])
    p.part_no           = data['part_no']
    p.part_name         = data['part_name']
    p.ps_no             = data['ps_no']
    p.ps_name           = data['ps_name']
    p.ps_type           = data['ps_type']
    p.ps_category       = data['ps_category']
    p.location_type     = data['location_type']
    p.electors_male     = data['electors_male']
    p.electors_female   = data['electors_female']
    p.electors_other    = data['electors_other']
    p.electors_total    = data['electors_total']

    db.session.commit()
    return jsonify({'msg': 'Data updated successfully'}), 200

@bp.route('/ps/delete', methods=['POST'])
@login_required
def ps_delete():
    data = request.get_json()
    p = PollingStation.query.get(data['id'])
    db.session.delete(p)
    db.session.commit()
    return jsonify({'msg': 'Data deleted successfully'}), 200

@bp.route('/ps/import', methods=['POST'])
@login_required
def ps_import():
    ac_no = None
    for role in current_user.roles:
        if role.name.startswith('ac_'):
            ac_no = role.name.split('ac_')[1]
            break
    if 'file' not in request.files:
        return jsonify({'msg': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'msg': 'No selected file'}), 400
    if not file.filename.endswith('.xlsx'):
        return jsonify({'msg': 'Invalid file extension'}), 400
    
    df = pd.read_excel(file)

    for index, row in df.iterrows():
        p = PollingStation.query.filter_by(part_no=row['PART_NO'], ps_no=row['PS_NO']).first()
        if p is None:
            p = PollingStation()

            p.assembly_const_no = ac_no
            p.part_no           = row['PART_NO']
            p.part_name         = row['PART_NAME']
            p.ps_no             = row['PS_NO']
            p.ps_code           = (ac_no if int(ac_no) > 9 else '0' + ac_no) + '/' + str(row['PART_NO'])
            p.ps_name           = row['PS_NAME_EN']
            p.ps_type           = row['PS_TYPE']
            p.ps_category       = row['PS_CATEGORY']
            p.location_type     = row['LOCN_TYPE']
            p.electors_male     = row['electors_male']
            p.electors_female   = row['electors_female']
            p.electors_other    = row['electors_other']
            p.electors_total    = row['electors_total']

            db.session.add(p)
    db.session.commit()
    return jsonify({'msg': 'Data imported successfully'}), 200