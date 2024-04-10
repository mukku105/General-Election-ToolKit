$(document).ready(function() {


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
});