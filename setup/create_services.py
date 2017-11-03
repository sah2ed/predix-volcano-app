#!/bin/env python

import logging
import predix.admin.app

# You should configure these settings with something
# unique for your own application deployment.
admin_secret = 'admin-secret'
client_id = 'masaya'
client_secret = 'masaya-yousaya'
manifest_path = '../manifest.yml'
debug = False

def create_services():
    # Your configuration will be stored in the manifest file
    # which you may not want to check into a public repository
    # as it will have secrets about your passwords and zone ids
    app = predix.admin.app.Manifest(manifest_path)
    app.lock_to_org_space()
    print("Targeting org %s and space %s" % (app.space.org.name,
        app.space.name))

    # We need UAA for end-to-end security of our volcano
    # application and when working with Predix services.
    uaa = app.create_uaa(admin_secret)
    print("Created Predix UAA service %s" % (uaa.service.name))
    app.create_client(client_id, client_secret)
    print("Added client %s for your application" % (client_id))

    # The Time Series service will store data points collected
    # from sensors.
    ts = app.create_timeseries()
    print("Created Predix Time Series service %s" % (ts.service.name))

    # The asset service holds our data model for the nodes and
    # sensors deployed in the volcano.
    asset = app.create_asset()
    print("Created Predix Asset service %s" % (asset.service.name))

    # This merely initializes the services, you will still need to
    # add data.
    print("You are now ready to ingest data")

if __name__ == '__main__':
    # If something goes wrong will help investigate.
    if debug:
        logging.basicConfig(level=logging.DEBUG)

    create_services()

