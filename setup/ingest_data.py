#!/usr/bin/env python

import csv
import time
import logging
import predix.app

import assetmodel

manifest_path = '../manifest.yml'

def read_csv(csvfile):
    """
    Read CSV file and index by the unique id.
    """
    index = {}
    with open(csvfile, 'r') as data:
        for row in csv.DictReader(data):
            index[row['id']] = row

    return index

def index_datasets():
    """
    Read CSV and return an index of the datasets where
    relationships can be referenced by id.
    """
    datasets = [
        'volcanos', #id,description,location,name,status
        'nodes', # id,description,location,name,status,volcano_id
        'sensors', # id,data_frequency,data_type_id,description,node_id,status
        'datatypes', # id,si_unit,type,type_id
        'datapoints', # id,sensor_id,timestamp,value
        ]

    index = {}
    for dataset in datasets:
        index[dataset] = read_csv("./data/%s.csv" % (dataset))

    return index

def utc_to_epoch(utc):
    """
    Take UTC formatted date and return it in
    millisecond accurate epoch time.
    """
    timeformat = '%Y-%m-%d %H:%M:%S+00'
    return int(time.mktime(time.strptime(utc, timeformat)) * 1000)

def batch(asset, mock=False):
    """
    To load a large dataset we want to send the data up in
    batches.  We've batched based on common attributes so
    that we can send a bunch of datapoints together.
    """
    batches = {}
    asset_catalog = {}

    index = index_datasets()
    for point in index['datapoints'].values():

        # Get attributes
        sensor = index['sensors'][point['sensor_id']]
        node = index['nodes'][sensor['node_id']]
        datatype = index['datatypes'][sensor['data_type_id']]
        volcano = index['volcanos'][node['volcano_id']]

        # We need to chunk by volcano/node/sensor for batch
        # ingestion since attributes are per set

        volcano_id = volcano['id']
        node_id = node['id']
        sensor_id = sensor['id']

        if volcano_id not in batches:
            batches[volcano_id] = {}

            name = index['volcanos'][volcano_id]['name']
            description = index['volcanos'][volcano_id]['description']
            status = index['volcanos'][volcano_id]['status']
            location = index['volcanos'][volcano_id]['location']

            volcano = assetmodel.Volcano(name, description, location, status, guid=volcano_id)
            if not mock:
                asset.save(volcano)

            asset_catalog[volcano_id] = volcano

        if node_id not in batches[volcano_id]:
            batches[volcano_id][node_id] = {}

            name = index['nodes'][node_id]['name']
            description = index['nodes'][node_id]['description']
            location = index['nodes'][node_id]['location']
            status = index['nodes'][node_id]['status']
            volcano_uri = asset_catalog[volcano_id].uri

            node = assetmodel.Node(name, description, location, status,
                    volcano_uri, guid=node_id)
            if not mock:
                asset.save(node)

            asset_catalog[node_id] = node

        if sensor_id not in batches[volcano_id][node_id]:
            batches[volcano_id][node_id][sensor_id] = []

            description = index['sensors'][sensor_id]['description']
            status = index['sensors'][sensor_id]['status']
            data_frequency = index['sensors'][sensor_id]['data_frequency']
            node_uri = asset_catalog[node_id].uri

            data_type_id = index['sensors'][sensor_id]['data_type_id']
            if data_type_id not in asset_catalog:
                data_type = index['datatypes'][data_type_id]['type']
                unit = index['datatypes'][data_type_id]['si_unit']
                tag = index['datatypes'][data_type_id]['type_id']

                dt = assetmodel.DataType(data_type, unit, tag,
                        guid=data_type_id)
                if not mock:
                    asset.save(dt)
                asset_catalog[data_type_id] = dt

            data_type = asset_catalog[data_type_id].uri

            sensor = assetmodel.Sensor(description, status, data_type,
                    data_frequency, node_uri, guid=sensor_id)
            if not mock:
                asset.save(sensor)

            asset_catalog[sensor_id] = sensor

        # Get Timestamp
        stamp = utc_to_epoch(point['timestamp'])

        # Get value / quality
        value = point['value']
        quality = predix.data.timeseries.TimeSeries.UNCERTAIN
        if value == 'NaN':
            quality = predix.data.timeseries.TimeSeries.BAD
            value = 0

        tag = datatype['type_id']

        batches[volcano_id][node_id][sensor_id].append({
                'tag': tag,
                'attributes': {
                    'volcano': asset_catalog[volcano_id].uri,
                    'node': asset_catalog[node_id].uri,
                    'sensor': asset_catalog[sensor_id].uri
                },
                'timestamp': stamp,
                'value': value,
                'quality': quality
            })

    return batches

def main(mock=False):

    # Load configuration from manifest
    app = predix.app.Manifest(manifest_path)
    timeseries = app.get_timeseries()
    asset = app.get_asset()

    total = 0

    # Iterate over the hierarchy in batches of datapoints
    # based on volcano > node > sensor relationship.
    batches = batch(asset, mock=mock)
    for volcano in batches.keys():
        logging.info("Processing volcano " + volcano)

        for node in batches[volcano].keys():
            logging.info("Processing node " + node)

            for sensor in batches[volcano][node].keys():
                logging.info("Processing sensor " + sensor)

                count = 0
                for item in batches[volcano][node][sensor]:
                    if mock:
                        logging.info(item)
                        continue

                    logging.debug(str(item))
                    timeseries.queue(item['tag'], item['value'],
                            timestamp=item['timestamp'],
                            quality=item['quality'],
                            attributes=item['attributes'])
                    count += 1

                    if count == 100:
                        total += count
                        logging.info("Sent %s total datapoints" % (total))
                        if not mock:
                            timeseries.send()
                        count = 0

                if not mock:
                    timeseries.send()

if __name__ == '__main__':
    debug = False
    if debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)
    main(mock=debug)

