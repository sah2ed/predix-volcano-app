
import re
import json
from flask import render_template

import predix.data.asset

from . import dashboard

asset = predix.data.asset.Asset()

def natural_sort(l):
    """
    Sort alpha-naturally so N10 comes after N2.
    """
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([\d]+)', key['val']) ]
    return sorted(l, key=alphanum_key)

@dashboard.route('/')
def home():
    """
    For root route we display a simple volcano dashboard to view node and
    sensor data in a time series graph.
    """
    # Query the node assets we tracked
    nodes = []
    default_node = ''
    for node in asset.get_collection('/node'):
        nodes.append({
            "key": node['uri'],
            "val": node['name']
            })
        if node['name'] == 'N10':
            default_node = node['uri']

    # Query the sensor assets we tracked
    sensors = []
    for sensor in asset.get_collection('/datatype'):
        sensors.append({
            "key": sensor['tag'],
            "val": sensor['data_type'] + " (%s)" % (sensor['tag'])
            })

    # Render the dashboard jinja2 template
    return render_template('home.html',
            sensors=json.dumps(natural_sort(sensors)),
            default_node=default_node,
            nodes=json.dumps(natural_sort(nodes)))

