
from flask import Blueprint
api = Blueprint('api', __name__)

from . import volcano, node, sensor, datatype, datapoint, health

