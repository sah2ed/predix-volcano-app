
import sys
from flask import jsonify

import predix

from . import api

@api.route('/health')
def health():
    """
    Provides basic system health.

    - *status*: UP indicates good health
    - *dependencies*: dictionary of some versioning for critical dependencies

    .. http:get:: /api/1.0/health

    Responds with app metadata to indicate health status for monitoring systems.

    **Example request**

    .. sourcecode:: http

       GET /api/1.0/health HTTP
       Host: predix-volcano.run.aws-usw02-pr.ice.predix.io
       Accept: application/json

    **Example response**

    .. sourcecode:: http

       HTTP/1.1 200 OK
       Content-Type: application/json

       {
       "dependencies": {
           "predixpy": "0.0.8",
           "python": "2.7.10 (default, Oct 23 2015, 19:19:21) [GCC 4.2.1 Compatible Apple LLVM 7.0.0 (clang-700.0.59.5)]"
            },
       "status": "UP"
       }


    """
    return jsonify({
            'status': 'UP',
            'dependencies': {
                'predixpy': predix.version,
                'python': sys.version,
            }
        })
