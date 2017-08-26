
Getting Started
===============

Sign Up
-------

You will need to register for a Predix Account.  The platform requires identity
proofing so you will need to provide accurate details about yourself, your
company, and your address to expedite account creation.  No credit card is
required and this demo uses free trial services and plans.

.. note::

   Go `sign up now`_ to get your account.

.. _Sign Up Now: https://predix.io/registration

Install Cloud Foundry
---------------------

Predix is based on Cloud Foundry, so you will need the `cf` Cloud Foundry CLI
to deploy your application if not already installed.

.. note::

    See the `Cloud Foundry Installation`_ documentation for full instructions for
    Mac OS X, Linux, and Windows.

.. _Cloud Foundry Installation: https://docs.cloudfoundry.org/cf-cli/install-go-cli.html

Create a Space
--------------

Cloud Foundry is made with enterprises in mind and manages compute and storage
resources through the concepts of organizations and spaces.  You can create a space
specifically to work on your volcano project in your own default organization.

From a terminal::

   cf login -a https://api.system.aws-usw02-pr.ice.predix.io
   cf create-space volcano
   cf target -s volcano

To learn more review the `Orgs and Spaces`_ documentation.

.. _Orgs and Spaces: https://docs.cloudfoundry.org/concepts/roles.html

Install Python
--------------

This reference application makes use of Python.  If you are not a Python
developer you may not have access to the dependencies but they are beyond the
scope of this Getting Started guide.

- python (2.7.10+)
- pip (9.0.1+)

.. note::

    If you need help with these, check out the `Hitchiker's Guide to
    Python`_ or `Python docs`_ for details.

.. _Python docs: https://wiki.python.org/moin/BeginnersGuide
.. _Hitchiker's Guide to Python: http://docs.python-guide.org/en/latest/starting/installation/

Setup Services
--------------

There are two setup scripts you should run to prepare your space.  The first
creates all of the services you need to use.  The second will ingest the data
into those services.

If you haven't yet, clone the github repository and install Python dependencies
by running::

   git clone https://github.com/PredixDev/predix-volcano-app
   cd predix-volcano-app
   pip install -r requirements.txt

Then change into the **setup** directory to run the setup scripts::

   cd setup
   python create_services.py
   python ingest_data.py

You will need to run these from the **setup** directory of the volcano-app
repository.  The services use the *free* plans that allow you to learn,
experiment, and develop proof of concept implementations.  The second aids in
reading the CSV files to populate the services with the volcano data from
masaya.

It will take a few minutes to complete the full data ingestion.

Build
-----

The repository does not contain all of the library dependencies so you will
need to use a few common web development tools.  Please see the respective
documentation of these projects for instructions on installing npm_, bower_,
and gulp_.

.. _npm: https://docs.npmjs.com/cli/install
.. _bower: https://bower.io/#install-bower
.. _gulp: https://github.com/gulpjs/gulp/blob/master/docs/getting-started.md

From the root **predix-volcano-app** directory of the repository::

   cd app/dashboard
   npm install
   bower install
   gulp

Push Your App
-------------

You are now ready to deploy your app to the cloud.  The **manifest.yml**
generated for you in the root of your repository has details about your
application.  Typically these details should be encrypted to avoid others from
accessing your services.

From the root **predix-volcano-app** of the repository you can cf push::

   cd ../../
   cf push --random-route

After pushing your app, you'll see the URL in the output.  Add `https://` to
the front of that URL and you can navigate to the app in your web browser.

.. note::

    For more detailed description of cf commands see the Cloud Foundry
    documentation for how to `Deploy An App`_.

.. _Deploy An App: https://docs.cloudfoundry.org/devguide/deploy-apps/deploy-app.html#push

Next Steps
----------

This is just the beginning, go learn more about Predix Services by checking out
the `Predix Guides`_.

.. _Predix Guides: https://www.predix.io/resources/tutorials

