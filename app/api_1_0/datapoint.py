
import logging

from flask import jsonify
from flask import request

import predix.data.timeseries

from . import api

timeseries = predix.data.timeseries.TimeSeries()

@api.route('/datapoints')
def datapoints():
    """
    Data points collected for the given nodes and sensors.

    - *x*: epoch in millisecond timestamp for when data points collected

    Additionally each selected sensor will be returned as the key with the
    corresponding value being the reading for the timestamp.

    .. http:get:: /api/1.0/datapoints?node=/node/c5e39fa0&sensor=GP_CO2

    Responds with collected data for node and sensor.

    **Example request**:

    .. sourcecode:: http

        GET /api/1.0/datapoints? HTTP/1.1
        Host: predix-volcano.run.aws-usw02-pr.ice.predix.io
        Accept: application/json

    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json

        [
            {
                "GP_CO2": 32.035, 
                "x": 1471421209000
            }, 
            {
                "GP_CO2": 32.035, 
                "x": 1471423009000
            }, 
            {
                "GP_CO2": 32.035, 
                "x": 1471424807000
            }, 
            {
                "GP_CO2": 32.035, 
                "x": 1471426606000
            }, 
            ...
        ]

    """
    # TODO: better error handling for no node/sensors selected
    node = request.args.get('node')
    sensors = request.args.get('sensor').split(',')
    logging.info("Query: %s, %s" % (node, sensors))

    response = timeseries.get_datapoints(sensors, start='5y-ago', limit=10000,
            attributes={'node': node})

    # get_datapoints() returns data like this...
    #   {"tags": [{"name": "HUMA", "results": [{"values": [
    #       [1471266639000,83.3,1],
    #       [1471270237000,87.2,1], ... ]}]},
    #       {"name": "PA", "results": [{"values": [ ... ]}]}]}
    # We need to transform it for px-vis-timeseries which expects this...
    #   [{'x': 1471266639000, 'TAG1': 83.3, 'TAG2': 57.3}, ...]
    #
    #   [{'x': 1471266639000, 'TAG1': 83.3}, {'x': 1471266639000, 'TAG2':
    #   57.3}] does not
    # and requires them to be sorted by x to render properly

    data = {}
    for tag in response['tags']:
        name = tag['name']
        for result in tag['results']:
            for value in result['values']:
                timestamp = value[0]
                if timestamp not in data:
                    data[timestamp] = {'x': timestamp}

                data[timestamp][name] = value[1]

    datapoints = []
    for key in sorted(data.keys()):
        datapoints.append(data[key])

    return jsonify(datapoints)
