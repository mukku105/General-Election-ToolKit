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

    function voters_turnout_page() {
        console.log('Voters Turnout Page');
        let ac_no = $('#ac-no').attr('data-ac-no');
        console.log('AC NO - ' + ac_no);
        fetch_voters_turnout_data(ac_no);
    }

    function fetch_voters_turnout_data(ac_no, ps_code) {
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
            },
            error: function(error) {
                console.log(error);
                console.log('Error in Fetching Voters Turnout Data');
            }
        });
    }

    function populate_voters_turnout_fields(data) {
        console.log('Populating Voters Turnout Fields');



        for (let key in data) {
            accordian_id = '#accordian-' + key.split('/')[0] + '-' + key.split('/')[1];
            collapse_id = '#collapse-' + key.split('/')[0] + '-' + key.split('/')[1];
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