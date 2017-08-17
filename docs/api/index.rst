
Volcano API
===========

The data used by the Digital Volcano App is exposed as a set of RESTful
endpoints.  You can use these endpoints to retrieve data for your own
applications.  The public API is only open for `GET` requests so no
authentication, tokens, or api keys are necessary.

The resources representing the connected volcano include:

1. volcanoes
2. nodes
3. sensors
4. datatypes
5. datapoints

Volcano
-------

There is only one volcano as part of the sample data set representing the
expedition to the Masaya Volcano in Nicaragua.

.. automodule:: app.api_1_0.volcano
   :members:

Node
----

There were 10 nodes installed at the Masaya Volcano -- two at the very bottom
by the lava lake, three halfway into the crater at level 1, and five around the
perimeter of the Santiago Crater rim.

Data samples were commissioned by a node twice per hour to preserve battery
life for a total of 2400 data samples per day.

Each node was named N1 through N10.

.. automodule:: app.api_1_0.node
    :members:

Sensor
------

Each node housed a collection of sensors.  The sensors were provided by
Libelium_, a Spanish manufacturer of Open Source Hardware focused on data
sampling.

.. _Libelium: https://www.libelium.com

+---------------+---------+------------------+--------------------------------+
|    Sensor     |  Type   |  Accuracy (95%)  | Description                    |
+===============+=========+==================+================================+
| BME280        | Digital | ±1°C             | This sensor samples relative   |
|               |         |                  | humidity, temperature and      |
|               |         |                  | atmospheric pressure           |
+---------------+---------+------------------+--------------------------------+
| INE20 CO2P    | Near    | ±50°ppm          | This sensor samples Carbon     |
| NCVSP         | Infrared|                  | Dioxide, measured in PPM       |
|               | (NDIR)  |                  |                                |
+---------------+---------+------------------+--------------------------------+
| 4-H2S-100     | Electro | ±0.1ppm          | This sensor samples Hydrogen   |
|               | chemical|                  | Sulfide                        |
|               |         |                  |                                |
+---------------+---------+------------------+--------------------------------+

It would take up to 5 minutes for an accurate sampling to finish, where the Carbon Dioxide sensor typically caused delays as it required a warming up period before readings could be collected.

.. automodule:: app.api_1_0.sensor
    :members:

DataType
--------

There were five main data types collected by the sensors.

+---------------------+-----------+-----------------------------------------+
| Data Type           |  SI Unit  |  Description                            |
+=====================+===========+=========================================+
| Carbon Dioxide      |   PPM     | Measured in parts per million.          |
|   (GP_CO2)          |           |                                         |
+---------------------+-----------+-----------------------------------------+
| Hydrogen Sulfide    |   PPM     | Measured in parts per million.          |
|   (GP_H2S)          |           |                                         |
+---------------------+-----------+-----------------------------------------+
| Temperature         | Celsius   | Measured in degrees in Celsius.         |
|   (TCA)             |           |                                         |
+---------------------+-----------+-----------------------------------------+
| Atmospheric         | Pascal    | Measured in Pascal units.               |
| Pressure (PA)       |           |                                         |
+---------------------+-----------+-----------------------------------------+
| Relative Humidity   | Percent   | Measured in partial pressure ratios.    |
|   (HUMA)            |           |                                         |
+---------------------+-----------+-----------------------------------------+
| Battery             |           |                                         |
|   (BAT)             |           |                                         |
+---------------------+-----------+-----------------------------------------+
|                     |           |                                         |
|   (RSAM)            |           |                                         |
+---------------------+-----------+-----------------------------------------+

.. automodule:: app.api_1_0.datatype
    :members:

DataPoint
---------

.. automodule:: app.api_1_0.datapoint
    :members:

Health
------

.. automodule:: app.api_1_0.health
    :members:

*Last updated:* |today|
