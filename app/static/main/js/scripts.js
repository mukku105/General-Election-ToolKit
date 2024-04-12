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

    $('.calc-sangha-btn').click(function() {
        accordionBody = $(this).closest('.accordion-body')
        voters_turnout_ac = accordionBody.find(".table-responsive")[5]
        voters_turnout_pc = accordionBody.find(".table-responsive")[7]
        console.log(voters_turnout_ac)

    })

    $('.reload-turnout-btn').click(function() {
        accordionBody = $(this).closest('.accordion-body');
        psCode = accordionBody.attr('data-ps-code');
        acNo = accordionBody.attr('data-ac-no');
        fetch_voters_turnout_data(acNo, psCode);
    })

    $('.update-turnout-btn').click(function() {
        accordionBody = $(this).closest('.accordion-body');
        psCode = accordionBody.attr('data-ps-code');
        acNo = accordionBody.attr('data-ac-no');
        voters_turnout = accordionBody.find('.table-responsive');
        console.log(voters_turnout);

        data = {};
        for(let i=0; i<7; i++) {
            turnout_input = $(voters_turnout[i]).find('table tbody td input');
            data[i+1] = {
                            "t_male": turnout_input[0].value ? turnout_input[0].value : 0,
                            "t_female": turnout_input[1].value ? turnout_input[1].value : 0,
                            "t_other": turnout_input[2].value ? turnout_input[2].value : 0,
                        }
        }

        data_json = {
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
        fetch_voters_turnout_data(ac_no);
    }

    function fetch_voters_turnout_data(ac_no, ps_code) {
        $('#overlay-spinner').show();
        console.log('Fetching Voters Turnout Data');

        param = '?ac_no=' + ac_no + (ps_code == undefined ? '' : '&ps_code=' + ps_code);

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
            accordian_id = '#accordian-' + parseInt(key.split('/')[0]) + '-' + key.split('/')[1];
            collapse_id = '#collapse-' + parseInt(key.split('/')[0]) + '-' + key.split('/')[1];
            console.log(collapse_id);

            voters_turnout = $(collapse_id).find('.table-responsive');

            $(accordian_id).find('.current-turnout span')[0].innerHTML = 'M: ' + data[key]['current_turnout_percentage']['male'] + '%';
            $(accordian_id).find('.current-turnout span')[1].innerHTML = 'F: ' + data[key]['current_turnout_percentage']['female'] + '%';
            $(accordian_id).find('.current-turnout span')[2].innerHTML = 'O: ' + data[key]['current_turnout_percentage']['other'] + '%';
            $(accordian_id).find('.current-turnout span')[3].innerHTML = 'T: ' + data[key]['current_turnout_percentage']['total'] + '%';

            // 9AM field populate
            // $(voters_turnout[0]).find('table tbody').empty();
            for(let i=0; i<7; i++) {
                voters_turnout_td_1 = $(voters_turnout[i]).find('table tbody td');
                $(voters_turnout_td_1[0]).find('input').val(data[key][i+1]['t_male']);
                $(voters_turnout_td_1[1]).html('<span class="badge bg-success fs-5">'+data[key][i+1]['t_male_percentage']+'%</span>');
                $(voters_turnout_td_1[2]).find('input').val(data[key][i+1]['t_female']);
                $(voters_turnout_td_1[3]).html('<span class="badge bg-success fs-5">'+data[key][i+1]['t_female_percentage']+'%</span>');
                $(voters_turnout_td_1[4]).find('input').val(data[key][i+1]['t_other']);
                $(voters_turnout_td_1[5]).html('<span class="badge bg-success fs-5">'+data[key][i+1]['t_other_percentage']+'%</span>');
                $(voters_turnout_td_1[6]).html('<span class="badge bg-danger fs-5">'+data[key][i+1]['t_total']+'</span>');
                $(voters_turnout_td_1[7]).html('<span class="badge bg-success fs-5">'+data[key][i+1]['t_total_percentage']+'%</span>');
            }
        }
    }
});