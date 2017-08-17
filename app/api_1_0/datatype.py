
from flask import jsonify

import predix.data.asset

from . import api

asset = predix.data.asset.Asset()

@api.route('/datatypes')
def datatypes():
    """
    Resource representing data types available.

    .. http:get:: /api/1.0/datatypes

    Responds with a list of available datatypes.

    **Example request**:

    .. sourcecode:: http

        GET /api/1.0/datatypes HTTP/1.1
        Host: predix-volcano.run.aws-usw02-pr.ice.predix.io
        Accept: application/json

        [
            {
                "data_type": "temperature", 
                "tag": "TCA", 
                "unit": "celcius", 
                "uri": "/datatype/35dcb3c0-8679-11e6-bda3-ef77801087ee"
            }, 
            {
                "data_type": "pressure", 
                "tag": "PA", 
                "unit": "pascal", 
                "uri": "/datatype/35dcb3c1-8679-11e6-bda3-ef77801087ee"
            }, 
            ...
        ]

    """
    datatypes = asset.get_collection('/datatype')
    return jsonify(datatypes)

@api.route('/datatype/<guid>')
def datatype(guid):
    """
    A specific datatype instance.

    .. http:get:: /api/1.0/datatype/:guid

    Responds with metadata for a single data type

    **Example request**:

    .. sourcecode:: http

        GET /api/1.0/datatype/35dcb3c2-8679-11e6-bda3-ef77801087ee HTTP/1.1
        Host: predix-volcano.run.aws-usw02-pr.ice.predix.io
        Accept: application/json

    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json

        {
        "data_type": "humidity", 
        "tag": "HUMA", 
        "unit": "relative humidity", 
        "uri": "/datatype/35dcb3c2-8679-11e6-bda3-ef77801087ee"
        }

    """
    datatypes = asset.get_collection("/datatype/%s" % (guid))
    return jsonify(datatypes[0])
