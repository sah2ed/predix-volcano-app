
import os
import logging
import predix.app

from flask_script import Manager, Server

import app

# Prepare environment with runtime environment variables
# for our application as set in the manifest.
manifest = predix.app.Manifest()

# Configuration differences for prod and dev modes for
# debugging and other application settings.
config_name = os.getenv('FLASK_CONFIG', 'default')
app = app.create_app(config_name)
manager = Manager(app)

if __name__ == '__main__':
    port = os.getenv('PORT', 8080)
    manager.add_command("runserver", Server(port=port))

    print("Running %s server on port %s." % (config_name, port))

    # Turn on additional logging output when dev server
    if app.config['DEBUG']:
        logging.basicConfig(level=logging.DEBUG)

    manager.run()

