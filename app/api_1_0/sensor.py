
from flask import jsonify

import predix.data.asset

from . import api

asset = predix.data.asset.Asset()

@api.route('/sensors')
def sensors():
    """
    Resource representing individual sensors.

    .. http:get:: /api/1.0/sensors

    Responds with a list of available sensors.

    **Example request**:

    .. sourcecode:: http

        GET /api/1.0/sensors HTTP/1.1
        Host: predix-volcano.run.aws-usw02-pr.ice.predix.io
        Accept: application/json

    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json

        [
            {
                "data_frequency": "1800000", 
                "data_type": "/datatype/ed5edee0-e701-11e6-83c1-01ce06e6d17f", 
                "description": "\\N", 
                "node": "/node/ede3ed60-e701-11e6-83c1-01ce06e6d17f", 
                "status": "OFFLINE", 
                "uri": "/sensor/1248ff60-e707-11e6-89c8-314aa4f67f8c"
            }, 
            {
                "data_frequency": "1800000", 
                "data_type": "/datatype/35dcdad2-8679-11e6-bda3-ef77801087ee", 
                "description": "\\N", 
                "node": "/node/762b8ff0-8679-11e6-a353-2f6c041e2491", 
                "status": "OFFLINE", 
                "uri": "/sensor/7635c920-8679-11e6-a353-2f6c041e2491"
            }, 
            ...
        ]

    """
    sensors = asset.get_collection('/sensor')
    return jsonify(sensors)

@api.route('/sensor/<guid>')
def sensor(guid):
    """
    .. http:get:: /api/1.0/sensor/:guid

    Responds with metadata for a single sensor.

    **Example request**:

    .. sourcecode:: http

        GET /api/1.0/sensor/1248ff60-e707-11e6-89c8-314aa4f67f8c HTTP/1.1
        Host: predix-volcano.run.aws-usw02-pr.ice.predix.io
        Accept: application/json

    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json

        {
        "data_frequency": "1800000", 
        "data_type": "/datatype/ed5edee0-e701-11e6-83c1-01ce06e6d17f", 
        "description": "\\N", 
        "node": "/node/ede3ed60-e701-11e6-83c1-01ce06e6d17f", 
        "status": "OFFLINE", 
        "uri": "/sensor/1248ff60-e707-11e6-89c8-314aa4f67f8c"
        }

    """
    sensors = asset.get_collection("/sensor/%s" % (guid))
    return jsonify(sensors[0])

