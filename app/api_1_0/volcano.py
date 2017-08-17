
from flask import jsonify

import predix.data.asset

from . import api

asset = predix.data.asset.Asset()

@api.route('/volcanoes')
def volcanoes():
    """
    Resource representing volcanoes -- a vent in the earth's crust
    which lava, steam, ashes are expelled.

    - **uri**: unique guid representing each volcano being tracked.
    - **name**: the name of a volcano
    - **description**: longer description describing volcano
    - **status**: OFFLINE or ONLINE; offline when no connected node is sending
      sensor data
    - **location**: GPS longitude and latitude

    .. http:get:: /api/1.0/volcanoes

    Responds with a list of available volcanoes and summary.

    **Example request**:

    .. sourcecode:: http

        GET /api/1.0/volcanoes HTTP/1.1
        Host: predix-volcano.run.aws-usw02-pr.ice.predix.io
        Accept: application/json

    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json

        [
          {
            "description": "This is the world's biggest, baddest, most evil volcano.",
            "location": "{11.985318299999999,-86.178342900000004}",
            "name": "Masaya",
            "status": "OFFLINE",
            "uri": "/volcano/35dc3e90-8679-11e6-bda3-ef77801087ee"
          }
        ]

    """
    volcanoes = asset.get_collection('/volcano')
    return jsonify(volcanoes)

@api.route('/volcano/<guid>')
def volcano(guid):
    """
    .. http:get:: /api/1.0/volcano/:guid

    Responds with metadata for a single volcano and its
    corresponding sensor network nodes.

    **Example request**:

    .. sourcecode:: http

        GET /api/1.0/volcano/35dc3e90-8679-11e6-bda3-ef77801087ee HTTP/1.1
        Host: predix-volcano.run.aws-usw02-pr.ice.predix.io
        Accept: application/json

    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json

        {
        "description": "This is the world's biggest, baddest, most evil volcano.",
        "location": "{11.985318299999999,-86.178342900000004}",
        "name": "Masaya",
        "nodes": [
            {
            "name": "N10",
            "uri": "/node/762b8ff0-8679-11e6-a353-2f6c041e2491"
            },
            {
            "name": "N7",
            "uri": "/node/762c5340-8679-11e6-a353-2f6c041e2491"
            },
            ...
        ],
        "status": "OFFLINE",
        "uri": "/volcano/35dc3e90-8679-11e6-bda3-ef77801087ee"
        }

    """
    volcanoes = asset.get_collection("/volcano/%s" % (guid))
    if len(volcanoes) == 1:
        volcano = volcanoes[0]
        uri = volcano['uri']

        nodes = asset.get_collection('/node', filter="volcano=%s" % (uri),
                fields=['uri', 'name'])
        volcanoes[0].update({'nodes': nodes})

    return jsonify(volcanoes[0])
