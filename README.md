
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

- [Digital Volcano Story][story] (**Start Here**)
- [Digtal Volcano Demo App][volcanoapp]
- [Documentation][docs]

# Getting Started

See the [Getting Started Guide][quickstart] for details.  You will need to
complete the following steps:

- [ ] Sign up for a [Free Predix Account][signup] (no credit card required)
- [ ] Clone this repository
- [ ] Run `pip install predix` (making sure you have python 2.7.10+ and pip 9.0.1+)
- [ ] Run setup scripts
- [ ] Deploy your app with `cf push`

The specifics on how to complete these steps can be found in the [Getting Started Guide][quickstart].

# Volcano Data

To access the volcano data you have a few options.

1. Use the [Digital Volcano App][volcanoapp] for simple exploration.
2. Use the [Volcano API][volcanoapi] to make REST calls.
3. Use the CSV files in the **setup/data** directory to import to your
   preferred data science tools.

# Predix Services Used

The following services have Free trial plans sufficient to run this
application.

- [Predix User Account and Authentication][uaa] (UAA)
- [Predix Time Series][timeseries]
- [Predix Asset][asset]
- [Predix UI][ui]
- [PredixPy][predixpy]

# Getting Help

If something didn't work as expected and you want help:

- Create a [GitHub Issue][github] in this project
- Ask on the [Predix Developer Forum][forum]
- Send email to volcano@ge.com and we'll try to respond when we can

[![Analytics](https://ga-beacon.appspot.com/UA-82773213-1/predix-sdks/readme?pixel)](https://github.com/PredixDev)

[story]: https://www.ge.com/digitalvolcano
[volcanoapp]: https://volcano-app.run.aws-usw02-pr.ice.predix.io
[docs]: https://volcano-app.run.aws-usw02-pr.ice.predix.io/docs/html/index.html
[quickstart]: https://volcano-app.run.aws-usw02-pr.ice.predix.io/docs/html/getting-started/index.html
[signup]: https://www.predix.io/registration/
[uaa]: https://www.predix.io/services/service.html?id=1172
[timeseries]: https://www.predix.io/services/service.html?id=1177
[asset]: https://www.predix.io/services/service.html?id=1171
[ui]: https://www.predix-ui.com/#/home/
[predixpy]: https://github.com/PredixDev/predixpy
[volcanoapi]: https://volcano-app.run.aws-usw02-pr.ice.predix.io/docs/html/api/index.html
[forum]: https://forum.predix.io/index.html
[github]: https://github.com/PredixDev/predix-volcano-app/issues
