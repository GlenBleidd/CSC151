<script charset="utf-8" type="text/javascript">

$(function() {

    // jQuery selection for the 2 select boxes
    var dropdown = {
        course: $('#select_state'),
    };

    // call to update on load
    updateCounties();

    // function to call XHR and update county dropdown
    function updateCounties() {
        var send = {
            state: dropdown.state.val()
        };
        dropdown.county.attr('disabled', 'disabled');
        dropdown.county.empty();
        $.getJSON("{{ url_for('_get_counties') }}", send, function(data) {
            data.forEach(function(item) {
                dropdown.county.append(
                    $('<option>', {
                        value: item[0],
                        text: item[1]
                    })
                );
            });
            dropdown.county.removeAttr('disabled');
        });
    }

    // event listener to state dropdown change
    dropdown.state.on('change', function() {
        updateCounties();
    });

});

</script>
