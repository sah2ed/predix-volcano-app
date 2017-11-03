
from flask import jsonify

import predix.data.asset

from . import api

asset = predix.data.asset.Asset()

@api.route('/nodes')
def nodes():
    """
    Resource representing sensor nodes -- a collection of sensors installed as
    part of a network at a single location.

    .. http:get:: /api/1.0/nodes

    Responds with a list of available nodes.

    **Example request**:

    .. sourcecode:: http

        GET /api/1.0/nodes HTTP/1.1
        Host: predix-volcano.run.aws-usw02-pr.ice.predix.io
        Accept: application/json

    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json

        [
            {
                "description": "\\N",
                "location": "\\N",
                "name": "N10",
                "status": "OFFLINE",
                "uri": "/node/762b8ff0-8679-11e6-a353-2f6c041e2491",
                "volcano": "/volcano/35dc3e90-8679-11e6-bda3-ef77801087ee"
            },
            {
                "description": "\\N",
                "location": "\\N",
                "name": "N7",
                "status": "OFFLINE",
                "uri": "/node/762c5340-8679-11e6-a353-2f6c041e2491",
                "volcano": "/volcano/35dc3e90-8679-11e6-bda3-ef77801087ee"
            },
        ...
        ]

    """
    nodes = asset.get_collection('/node')
    return jsonify(nodes)

@api.route('/node/<guid>')
def node(guid):
    """
    .. http:get:: /api/1.0/node/:guid

    Responds with metadata for a single node and its
    corresponding sensors.

    **Example request**:

    .. sourcecode:: http

        GET /api/1.0/node/762b8ff0-8679-11e6-a353-2f6c041e2491 HTTP/1.1
        Host: predix-volcano.run.aws-usw02-pr.ice.predix.io
        Accept: application/json

    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json

        {
        "description": "\\N",
        "location": "\\N",
        "name": "N10",
        "sensors": [
            {
            "uri": "/sensor/7635c920-8679-11e6-a353-2f6c041e2491"
            },
            {
            "uri": "/sensor/763701a1-8679-11e6-a353-2f6c041e2491"
            },
            ...
        ],
        "status": "OFFLINE",
        "uri": "/node/762b8ff0-8679-11e6-a353-2f6c041e2491",
        "volcano": "/volcano/35dc3e90-8679-11e6-bda3-ef77801087ee"
        }

    """
    nodes = asset.get_collection("/node/%s" % (guid))
    if len(nodes) == 1:
        node = nodes[0]
        uri = node['uri']

        sensors = asset.get_collection('/sensor', filter="node=%s" % (uri),
                fields=['uri', 'name'])
        nodes[0].update({'sensors': sensors})

    return jsonify(nodes[0])

