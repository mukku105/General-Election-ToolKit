$(document).ready(function() {
    if (window.location.pathname == '/toolkit/voters_turnout') {
        voters_turnout_page()
    }

    $('#ac_gen_comm_plan').click(function() {
        let ac_no = this.getAttribute('data-ac-no');
        let api_url = this.getAttribute('data-api-url');
        console.log('AC NO - ' + ac_no);

        $.ajax({
            type: 'POST',
            url: api_url,
            data: {
                ac_no: ac_no
            },
            success: function(response) {
                console.log(response);
                if (response.status == 'success') {
                    alert(response.msg);
                    window.open(response.url, '_blank');
                } else {
                    alert('Error in Generating Comm Plan');
                }
            },
            error: function(error) {
                console.log(error);
                alert('Error in Generating Comm Plan');
            }
        });
    })

    $('#ps_gen_comm_plan').click(function() {
        let ac_no = this.getAttribute('data-ac-no');
        let api_url = this.getAttribute('data-api-url');
        console.log('PS NO - ' + ac_no);

        $.ajax({
            type: 'POST',
            url: api_url,
            data: {
                ac_no: ac_no
            },
            success: function(response) {
                console.log(response);
                if (response.status == 'success') {
                    alert(response.msg);
                    window.open(response.url, '_blank');
                } else {
                    alert('Error in Generating Comm Plan');
                }
            },
            error: function(error) {
                console.log(error);
                alert('Error in Generating Comm Plan');
            }
        });
    })

    $('#import-ps-excel-btn').click(function() {
        let api_url = this.getAttribute('data-api-url');

        let excel_file = $('#file-import-ps')[0].files[0];

        let form_data = new FormData();
        form_data.append('file', excel_file);

        $.ajax({
            type: 'POST',
            url: api_url,
            data: form_data,
            contentType: false,
            processData: false,
            success: function(response) {
                console.log(response);
                if (response.status == 'success') {
                    alert(response.msg);
                    window.location.reload();
                } else {
                    alert('Error in Importing PS Data');
                }
            }
        });
    })

    $('.calc-ac-sangha-btn').click(function() {
        let ac_close_poll_table = $(this).closest('.accordion-body').find('.table-responsive')[5];
        let ac_close_poll_table_tr = $(ac_close_poll_table).find('table tbody tr');
        let ac_close_poll_table_tr_inp = $(ac_close_poll_table_tr[0]).find('td input');

        let sangha_close_poll_table = $(this).closest('.accordion-body').find('.table-responsive')[5];
        let sangha_close_poll_table_tr = $(sangha_close_poll_table).find('table tbody tr');
        let sangha_close_poll_table_tr_inp = $(sangha_close_poll_table_tr[2]).find('td input');

        let current_pc_close_poll_table = $(this).closest('.card-body').find('table')[0];
        let current_pc_close_poll_table_tr = $(current_pc_close_poll_table).find('tbody tr');
        let current_pc_close_poll_table_tr_inp = $(current_pc_close_poll_table_tr[0]).find('td input');

        current_pc_close_poll_table_tr_inp[0].value = parseInt(ac_close_poll_table_tr_inp[0].value) + parseInt(sangha_close_poll_table_tr_inp[0].value);
        current_pc_close_poll_table_tr_inp[1].value = parseInt(ac_close_poll_table_tr_inp[1].value) + parseInt(sangha_close_poll_table_tr_inp[1].value);
        current_pc_close_poll_table_tr_inp[2].value = parseInt(ac_close_poll_table_tr_inp[2].value) + parseInt(sangha_close_poll_table_tr_inp[2].value);
    })

    $('.copy-ac-btn').click(function() {
        let ac_close_poll_table = $(this).closest('.accordion-body').find('.table-responsive')[5];
        let ac_close_poll_table_tr = $(ac_close_poll_table).find('table tbody tr');
        let ac_close_poll_table_tr_inp = $(ac_close_poll_table_tr[0]).find('td input');

        let current_pc_close_poll_table = $(this).closest('.card-body').find('table')[0];
        let current_pc_close_poll_table_tr = $(current_pc_close_poll_table).find('tbody tr');
        let current_pc_close_poll_table_tr_inp = $(current_pc_close_poll_table_tr[0]).find('td input');

        current_pc_close_poll_table_tr_inp[0].value = ac_close_poll_table_tr_inp[0].value;
        current_pc_close_poll_table_tr_inp[1].value = ac_close_poll_table_tr_inp[1].value;
        current_pc_close_poll_table_tr_inp[2].value = ac_close_poll_table_tr_inp[2].value;

    })


    $('.calc-sangha-btn').click(function() {
        let accordionBody = $(this).closest('.accordion-body')
        let voters_turnout_ac = accordionBody.find(".table-responsive")[5]
        let voters_turnout_pc = accordionBody.find(".table-responsive")[7]
        console.log(voters_turnout_ac)

    })

    $('.reload-turnout-btn').click(function() {
        let accordionBody = $(this).closest('.accordion-body');
        let psCode = accordionBody.attr('data-ps-code');
        let acNo = accordionBody.attr('data-ac-no');
        fetch_voters_turnout_data(acNo, psCode);
    })

    $('.update-turnout-btn').click(function() {
        let accordionBody = $(this).closest('.accordion-body');
        let psCode = accordionBody.attr('data-ps-code');
        let acNo = accordionBody.attr('data-ac-no');
        let voters_turnout = accordionBody.find('.table-responsive');
        console.log(voters_turnout);

        let data = {};
        for(let i=0; i<7; i++) {
            let voters_turnout_tr = $(voters_turnout[i]).find('table tbody tr');
            let voters_turnout_input_ac = $(voters_turnout_tr[0]).find('td input');
            // let turnout_input = $(voters_turnout[i]).find('table tbody td input');
            data[i+1] = {
                            "t_male": voters_turnout_input_ac[0].value ? voters_turnout_input_ac[0].value : 0,
                            "t_female": voters_turnout_input_ac[1].value ? voters_turnout_input_ac[1].value : 0,
                            "t_other": voters_turnout_input_ac[2].value ? voters_turnout_input_ac[2].value : 0,
                            "t_male_sangha": 0,
                            "t_female_sangha": 0,
                            "t_other_sangha": 0
                        }
            if(voters_turnout_tr.length == 3) {
                let voters_turnout_input_pc = $(voters_turnout_tr[2]).find('td input');

                data[i+1]["t_male_sangha"] = voters_turnout_input_pc[0].value ? voters_turnout_input_pc[0].value : 0;
                data[i+1]["t_female_sangha"] = voters_turnout_input_pc[1].value ? voters_turnout_input_pc[1].value : 0;
                data[i+1]["t_other_sangha"] = voters_turnout_input_pc[2].value ? voters_turnout_input_pc[2].value : 0;

            }
        }

        let data_json = {
            data: data,
            ac_no: acNo,
            ps_code: psCode
        };
        console.log(data);
        $('#overlay-spinner').show();

        $.ajax({
            type: 'POST',
            url: '/toolkit/voters_turnout/update',
            contentType: 'application/json',
            data: JSON.stringify(data_json),

            success: function(response) {
                console.log(response);
                if (response.status == 'success') {
                    alert(response.msg);
                    fetch_voters_turnout_data(acNo, psCode);
                    fetch_ac_voters_turnout_data(acNo);
                } else {
                    alert('Error in Updating Voters Turnout Data');
                }
                $('#overlay-spinner').hide();
            },
            error: function(error) {
                $('#overlay-spinner').hide();
                console.log(error);
                alert('Error in Updating Voters Turnout Data');
            }
        });
    })

    function voters_turnout_page() {
        console.log('Voters Turnout Page');
        let ac_no = $('#ac-no').attr('data-ac-no');
        console.log('AC NO - ' + ac_no);
        fetch_ac_voters_turnout_data(ac_no);
        fetch_voters_turnout_data(ac_no);
    }

    function fetch_ac_voters_turnout_data(ac_no) {
        $('#overlay-spinner').show();
        console.log('Fetching AC Voters Turnout Data');

        $.ajax({
            type: 'GET',
            url: '/toolkit/voters_turnout/get_ac_turnout?ac_no=' + ac_no,
            success: function(response) {
                console.log(response);
                if (response.status == 'success') {
                    let ac_electors_badge = $('#ac-voters-turnout #ac-electors').find('.badge');


                    ac_electors_badge[0].innerHTML = 'M: ' + response.data['total_electors']['male']
                    ac_electors_badge[1].innerHTML = 'F: ' + response.data['total_electors']['female']
                    ac_electors_badge[2].innerHTML = 'O: ' + response.data['total_electors']['other']
                    ac_electors_badge[3].innerHTML = 'T: ' + response.data['total_electors']['total']
                    ac_electors_badge[4].innerHTML = 'Sg.T: ' + response.data['total_electors_sangha']['total']

                    let ac_turnout_badge = $('#ac-voters-turnout #ac-turnout').find('.badge');
                    let pc_turnout_badge = $('#ac-voters-turnout #pc-turnout').find('.badge');
                    let sangha_turnout_badge = $('#ac-voters-turnout #sangha-turnout').find('.badge');

                    $('#ac-voters-turnout #ac-turnout').find('h5 span')[0].innerHTML ='<mark class="rounded">' + response.data['total_turnout_current_ac'] + '</mark>';
                    $('#ac-voters-turnout #sangha-turnout').find('h5 span')[0].innerHTML ='<mark class="rounded">' + response.data['total_turnout_current_ac_sangha'] + '</mark>';
                    $('#ac-voters-turnout #pc-turnout').find('h5 span')[0].innerHTML ='<mark class="rounded">' + response.data['total_turnout_current_pc'] + '</mark>';

                    ac_turnout_badge[3].innerHTML = response.data['total_turnout_current_ac_percent'] + '%'
                    pc_turnout_badge[3].innerHTML = response.data['total_turnout_current_pc_percent'] + '%'
                    sangha_turnout_badge[3].innerHTML = response.data['total_turnout_current_ac_sangha_percent'] + '%'

                } else {
                    console.log('Error in Fetching AC Voters Turnout Data');
                }
                $('#overlay-spinner').hide();

            },
            error: function(error) {
                $('#overlay-spinner').hide();
                console.log(error);
                console.log('Error in Fetching AC Voters Turnout Data');
            }
        });

    }

    function fetch_voters_turnout_data(ac_no, ps_code) {
        $('#overlay-spinner').show();
        console.log('Fetching Voters Turnout Data');

        let param = '?ac_no=' + ac_no + (ps_code == undefined ? '' : '&ps_code=' + ps_code);

        $.ajax({
            type: 'POST',
            url: '/toolkit/voters_turnout/get_data' + param,
            success: function(response) {
                console.log(response);
                if (response.status == 'success') {
                    populate_voters_turnout_fields(response.data);
                } else {
                    console.log('Error in Fetching Voters Turnout Data');
                }
                $('#overlay-spinner').hide();

            },
            error: function(error) {
                $('#overlay-spinner').hide();
                console.log(error);
                console.log('Error in Fetching Voters Turnout Data');
            }
        });
    }

    function populate_voters_turnout_fields(data) {
        console.log('Populating Voters Turnout Fields');

        for (let key in data) {
            let accordian_id = '#accordian-' + parseInt(key.split('/')[0]) + '-' + key.split('/')[1];
            let collapse_id = '#collapse-' + parseInt(key.split('/')[0]) + '-' + key.split('/')[1];
            console.log(collapse_id);

            let voters_turnout = $(collapse_id).find('.table-responsive');

            $(accordian_id).find('.current-turnout span')[0].innerHTML = 'M: ' + data[key]['current_turnout_percentage']['male'] + '%';
            $(accordian_id).find('.current-turnout span')[1].innerHTML = 'F: ' + data[key]['current_turnout_percentage']['female'] + '%';
            $(accordian_id).find('.current-turnout span')[2].innerHTML = 'O: ' + data[key]['current_turnout_percentage']['other'] + '%';
            $(accordian_id).find('.current-turnout span')[3].innerHTML = 'T: ' + data[key]['current_turnout_percentage']['total'] + '%';

            // 9AM field populate
            // $(voters_turnout[0]).find('table tbody').empty();
            for(let i=0; i<7; i++) {
                let voters_turnout_tr = $(voters_turnout[i]).find('table tbody tr');
                let voters_turnout_td_ac = $(voters_turnout_tr[0]).find('td');
                $(voters_turnout_td_ac[0]).find('input').val(data[key][i+1]['t_male']);
                $(voters_turnout_td_ac[1]).html('<span class="badge bg-success fs-5">'+data[key][i+1]['t_male_percentage']+'%</span>');
                $(voters_turnout_td_ac[2]).find('input').val(data[key][i+1]['t_female']);
                $(voters_turnout_td_ac[3]).html('<span class="badge bg-success fs-5">'+data[key][i+1]['t_female_percentage']+'%</span>');
                $(voters_turnout_td_ac[4]).find('input').val(data[key][i+1]['t_other']);
                $(voters_turnout_td_ac[5]).html('<span class="badge bg-success fs-5">'+data[key][i+1]['t_other_percentage']+'%</span>');
                $(voters_turnout_td_ac[6]).html('<span class="badge bg-danger fs-5">'+data[key][i+1]['t_total']+'</span>');
                $(voters_turnout_td_ac[7]).html('<span class="badge bg-success fs-5">'+data[key][i+1]['t_total_percentage']+'%</span>')
                
                if(voters_turnout_tr.length == 3) {
                    let voters_turnout_td_pc = $(voters_turnout_tr[2]).find('td');
                    console.log(voters_turnout_td_pc)

                    $(voters_turnout_td_pc[0]).find('input').val(data[key][i+1]['t_male_sangha']);
                    $(voters_turnout_td_pc[1]).html('<span class="badge bg-success fs-5">'+data[key][i+1]['t_male_percentage_sangha']+'%</span>');
                    $(voters_turnout_td_pc[2]).find('input').val(data[key][i+1]['t_female_sangha']);
                    $(voters_turnout_td_pc[3]).html('<span class="badge bg-success fs-5">'+data[key][i+1]['t_female_percentage_sangha']+'%</span>');
                    $(voters_turnout_td_pc[4]).find('input').val(data[key][i+1]['t_other_sangha']);
                    $(voters_turnout_td_pc[5]).html('<span class="badge bg-success fs-5">'+data[key][i+1]['t_other_percentage_sangha']+'%</span>');
                    $(voters_turnout_td_pc[6]).html('<span class="badge bg-danger fs-5">'+data[key][i+1]['t_total_sangha']+'</span>');
                    $(voters_turnout_td_pc[7]).html('<span class="badge bg-success fs-5">'+data[key][i+1]['t_total_percentage_sangha']+'%</span>')
                }
            }
        }
    }
});