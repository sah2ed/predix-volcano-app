
# Introduction

To test our ability to digitize the natural world and take the first step
toward creating better predictive systems, GE embarked on an expedition to see
how industrial big data and predictive analytics can inform communities about
dangerous volcanic activity.

This repository is home to the source code, data, and documentation for the
Digital Volcano.  The App is a simple reference demonstrating the use of Predix
Services to help you learn how to extend it.  It is based on the data set
collected from industrial sensors installed in the Masaya Volcano near
Nicaragua's capital Managua.

Learn more about the project by taking the Digital Expedition and view the
sample app.

- [Digital Expedition Story][story]
- [Digtal Volcano Demo App][volcanoapp]
- [Documentation][docs]

# Getting Started

To run this application you will need to complete the following steps:

- [ ] Sign up for a [Free Predix Account][signup] (no credit card required)
- [ ] Install Python dependencies and libraries in requirements.txt
- [ ] Run from the setup directory both `create_services.py` and `ingest_data.py`
- [ ] Deploy your app with `cf push`

For more detailed descriptions of these steps view the [Getting Started Guide][quickstart].

# Predix Services Used

The following services have Free trial plans sufficient to run this
application.

- [Predix User Account and Authentication][uaa] (UAA)
- [Predix Time Series][timeseries]
- [Predix Asset][asset]
- [Predix UI][ui]
- [PredixPy][predixpy]


[![Analytics](https://ga-beacon.appspot.com/UA-82773213-1/predix-sdks/readme?pixel)](https://github.com/PredixDev)

[story]: https://ge.com/digitalvolcano
[volcanoapp]: https://volcano-app.run.aws-usw02-pr.ice.predix.io
[docs]: https://volcano-app.run.aws-usw02-pr.ice.predix.io/docs
[quickstart]: https://volcano-app.run.aws-usw02-pr.ice.predix.io/docs/html/quickstart/index.html
[signup]: https://www.predix.io/registration/
[uaa]: https://www.predix.io/services/service.html?id=1172
[timeseries]: https://www.predix.io/services/service.html?id=1177
[asset]: https://www.predix.io/services/service.html?id=1171
[ui]: https://www.predix-ui.com/#/home/
[predixpy]:Include://github.com/predixpy/predixpy 
