<script language="javascript">

// Use WebComponentsReady instead of $.ready() to allow
// Polyfills to finish for more complex Web Components in Polymer.
window.addEventListener('WebComponentsReady', function() {
    $('#wait-for-it').show();

    // Select sensors and nodes for initial load
    $.get({
        url: '/api/1.0/datapoints',
        data: {
            "sensor": "HUMA,TCA",
            "node": "/node/762b8ff0-8679-11e6-a353-2f6c041e2491"
        },
    }).done(function(data) {
        $('#wait-for-it').hide();
        $('#volcanograph')[0].chartData = data;
    }).fail(function(err) {
        alert("Error: Unable to fetch initial node and sensor data.  Try again.");
    });

    $("#refresh-button").click(function(evt) {
        // Show spinner that we're working
        $('#wait-for-it').show();

        // Check which sensors are selected
        var sensors = [];
        var items = $('#sensor-selection')[0].items;
        for (var i in items) {
            if (items[i]['checked']) {
                sensors.push(items[i]['key']);
            }
        }

        // Check which nodes are selected
        var node = $('#node')[0].selectedKey

        if (node.length == 0 || sensors.length == 0) {
            alert("Select at least one node and sensor to display.");
            return false;
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
