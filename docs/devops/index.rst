
DevOps
======

This section looks in more detail at some of the DevOps concerns for running a
production application such as the Predix Volcano App.  The development plan
for this project aimed to follow principles of the `twelve-factor app`_
methodology for building software.

.. _twelve-factor app: https://12factor.net/

Configuration
-------------

This section discuses the factors for the *Codebase*, *Dependencies*, and *Config*.

The source code for the project is stored in a revision control system on
GitHub to enable tracking of changes and deploy releases of the code at various
stages of development.  It was split between two separate repositories:

- `predixpy`_: which is home to the client library useful for working with
  Predix Services from Python
- `predix-volcano-app`_: which is home to the reference application and
  this documentation along with volcano data

There are a few ways which the dependencies are specified.

Python
......

Python dependencies are configured in *setup.py* and *requirements.txt* as is
the typical approach for Python development with setuptools.  Typically the
``pip install`` will pull these dependencies down for local development.  When
doing a ``cf push`` the Cloud Foundry buildpack will also reference these files
for building the container.

JavaScript
..........

Running ``npm install`` pulls down any JavaScript libraries specified in
*package.json* which are needed for building the application.  This includes
primarily **bower** and **gulp**.

Predix UI
.........

Being based on Polymer Predix UI components share the **bower** dendency.  The
UI components used in the reference app are specified in the *bower.json* file
and are resolved when running ``bower install``.

Cloud Foundry
.............

The *manifest.yml* file is generated when you run the *create_services.py*
script as part of the Getting Started Guide.  The purpose is to provide
bindings for dependent service instances used by the application.  It also
includes a few additional configuration details such as the Cloud Foundry
Python buildpack the solution is dependent upon.

.. note::

   The *manifest.yml* is excluded from the repository for security reasons
   since it contains details about accessing your services.  The intention is
   that you would encrypt the keys / endpoints using a private key.

.. _predix-volcano-app: https://github.com/PredixDev/predix-volcano-app
.. _predixpy: https://github.com/PredixDev/predixpy

Operations
----------

This section discusses factors for Backing Services, Build / Release / Run,
Processes, Port binding, Concurrency, and Disposability.

Cloud Foundry
.............

There are many other good resources on basics of `Cloud Foundry`_ for learning
about the open source platform as a service.  They key advantages for the
volcano app:

- Can run the Volcano App on AWS, MS Azure, or on premises because Cloud
  Foundry supports multiple cloud infrastructures.

- Provides a co-development environment where runtimes are scoped to an
  organization and space so it was easy for a team to collaborate and share the
  same services while insulating the production space from only release
  engineering concerns or qa space for only a CI/CD system.

- Provides container orchestration so once ``cf push`` is complete for an app
  the platform is able to keep it running and available. So long as there are no
  software defects the platform provides disposability of containers along with
  resiliency to bring the app back up again.

- Cloud Foundry provides a marketplace of backing services -- so the volcano
  app could be stateless and services such as Predix Asset and Predix Time
  Series handle persistence.  By being stateless we can maximize concurrency of
  the application and data reads with the Cloud Foundry router balancing load
  across instances.

- Cloud Foundry provides port binding and environment configuration so that the
  application itself can have multiple runtimes and reduce concerns around
  misconfigurations.

Apps
....

Running ``cf app volcano-qa`` shows the resources assigned to and being
consumed by the application::

   name:              volcano-qa
   requested state:   started
   instances:         1/1
   usage:             1G x 1 instances
   routes:            volcano-qa.run.aws-usw02-pr.ice.predix.io
   last uploaded:     Tue 22 Aug 19:12:29 PDT 2017
   stack:             cflinuxfs2
   buildpack:         python 1.5.15

   state     since                  cpu    memory         disk details
   #0   running   2017-08-23T02:15:22Z   0.0%   223.6M of 1G   396.1M of 1G

It is also easily to scale the application horizontally with the command ``cf
scale -i 3`` to create 3 instances::

     state     since                  cpu    memory         disk
     details
     #0   running   2017-08-23T15:02:36Z   0.0%   172.7M of 1G   416.1M of 1G
     #1   running   2017-08-26T14:54:54Z   0.0%   172.4M of 1G   416M of 1G
     #2   running   2017-08-23T15:02:36Z   0.0%   171.7M of 1G   416M of 1G

When we first launched the marketing campaign for this project there is an
expectation of increased load.  For industrial applications, there may also be
common patterns around maintenance, weekends, etc. where it may not be
necessary to reserve as many resources exclusively for the app.

In this example, memory and disk consumption is not fully utilized so it may
also be worth considering vertically downscaling these instances to better size
resources to the application.

.. _Cloud Foundry: https://www.cloudfoundry.org/

Quality Assurance
-----------------

This section discusses factors for Dev/Prod parity.

Spaces
......

The application leverages Cloud Foundry's capability to setup multiple spaces
within an Enterprise Organization for team collaboration.  Since the setup
scripts were designed to reproduce creating services and ingesting data, it was
possible to setup multiple near identical environments or reset them back to an
original state after running a test.

Running ``cf spaces`` in the organization shows multiple environments::

   volcano-j12y
   volcano-prod
   volcano-qa

Each developer can have a space dedicated to their own individual work or
function, or multiple developers could operate within the same environment and
then use a separate environment for integration.

CI/CD
.....

Utilizing a tool like **Jenkins**, source code check-ins to GitHub can trigger
an automatic build and deploy as well as run a full test suite against mock
services or a fully integrated envrionment.

Monitoring
----------

This section looks at the factors for Logs and Admin Processes.

Smoke Test
..........

A simple Smoke Test such as this example was created against the
``/api/1.0/healthcheck`` endpoint to verify the production app is alive.  Any
spikes in response time can trigger an alarm to attend to the application.
Here is a sample bash health check script::

    set -e
    export responseCurl=$(curl --write-out %{http_code} --output /dev/null https://volcano-app.run.aws-usw02-pr.ice.predix.io/api/1.0/health)
    if [ $responseCurl -ne 200 ]; then
        echo "Failed"
        exit 1
    else
        echo "Success"
        exit 0
    fi

Logging
.......

Cloud Foundry provides ``cf logs`` for tailing logs of the application of ``cf
logs --recent`` to see any log output still buffered.  If you completed the
Getting Started Guide you may have an instance of the Volcano App running, but
for production we also plug in Cloud Foundry with the Logging Service.

Running `cf s` shows a list of the services including **logstash-3**::

    name                                service             plan   bound apps
    last operation
    volcano-qa-logstash-3-free          logstash-3          free   volcano-qa,
    volcano-qa-kibana   create succeeded

It is bound to the volcano app but also an instance of kibana so that it is
possible to search, filter, and review many days of log output beyond what the
``cf logs`` command can produce.

.. _Logging Service: https://www.predix.io/services/service.html?id=1184
