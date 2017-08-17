<script language="javascript">
$(document).ready(function() {

    $('#wait-for-it').show();
    // var node = $('#node')[0].selectedKey;
    $.get({
        url: '/api/1.0/datapoints',
        data: {
            "sensor": "HUMA,TCA",
            "node": $('#node')[0].selectedKey
        },
    }).done(function(data) {
        $('#volcanograph')[0].chartData = data;
        $('#wait-for-it').hide();
    }).fail(function(err) {
        alert("Unable to fetch initial data.");
    });

    $("#refresh-button").click(function(evt) {

        $('#wait-for-it').show();

        // Check which sensors are selected
        var sensors = [];
        var items = $('#sensor-selection')[0].items;
        for (var i in items) {
            if (items[i]['checked']) {
                sensors.push(items[i]['key']);
            }
        }
        console.log("sensors=" + sensors);

        // Check which nodes are selected
        var node = $('#node')[0].selectedKey
        console.log("node=" + node);

        if (node.length == 0 || sensors.length == 0) {
            alert("Select a node and sensors to display.");
        }

        // Refresh chart data with new datapoints
        $.get({
            url: '/api/1.0/datapoints',
            data: {
                "sensor": sensors.join(),
                "node": node,
            },
        }).done(function(data) {
            $('#volcanograph')[0].chartData = data;
            $('#wait-for-it').hide();
        }).fail(function(err) {
            alert("Unable to fetch data for this node and sensors.");
        });

    });

});
</script>
