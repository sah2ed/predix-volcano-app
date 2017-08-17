
Architecture
============

This section aims to explain how the application was built in detail so that
you can understand how the components interact with one another to form an
application architecture.

Overview
--------

The Volcano App is designed to run on the **Predix Cloud**.  The Predix Cloud
is running **Cloud Foundry**, a multi-cloud container-based architecture.  The
app could run on top of OpenStack, Microsoft Azure, Google Compute Platform, or
as the case with Predix Free Trial accounts -- AWS in the US-West environment.

The application consists of *client* and *server* components that integrate via
RESTful service calls to Predix Micro-Services.  

.. image:: images/overview.png

The primary components in the tech stack we'll discuss include:

- polymer
- bower
- sass
- gulp
- npm
- jQuery
- python
- flask
- gunicorn
- jinja

.. include:: services.rst

.. include:: ui.rst


*Last updated:* |today|






