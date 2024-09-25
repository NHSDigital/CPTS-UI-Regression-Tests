[![Regression Tests](https://github.com/NHSDigital/cpts-ui-regression-tests/actions/workflows/regression_tests.yml/badge.svg?branch=main)](https://github.com/NHSDigital/electronic-prescription-service-api-regression-tests/actions/workflows/regression_tests.yml)

![Warning](https://img.freepik.com/free-vector/warning-sign-with-warning-word_78370-4060.jpg "Warning Image")
<b> The information provided here has been copied from [Electronic Prescription Service API Regression Tests](https://github.com/NHSDigital/electronic-prescription-service-api-regression-tests/) as has much of the code.
This is to provide a template repo which will be modified once active development beings on the Clinical Prescription Tracking Service.
</b>


# Regression Tests
These tests will automate End-to-End UI regression testing for the Clinical Prescription Tracking Service website
Using Playwright integrated with pytest-bdd

## General usage
These tests are run automatically during deployment and shouldn't need to be touched unless performing debugging or
adding/removing/changing test cases <br />
If there are any test failures, this will report a failed build
## Setup

### Environment Variables
It is necessary to set some Environment variables in order to run any tests in your local environment. The tests will look for environment variables in the following order
(For security, the values will not be displayed here):
1. `.env` file
2. OS environment variable

The following environment variables need to be set for the correct environment you wish to test against:
* CLIENT_ID
* CLIENT_SECRET
* PRIVATE_KEY
* CERTIFICATE

To make this easier, a `template.env` file is located on the root. Fill in the values and rename this to `.env`

Any file that begins with `.env` is automatically ignored by Git

### Preparing your development environment
This test pack utilises the power of Docker to quickly and easily spin up a dev environment for you to work in
the Dockerfile is located in `{project_root}/.devcontainer/Dockerfile`

### Setup without docker development environment
If you'd like to use your own machine without containerisation. You will need the following;
* Ubuntu (WSL)
* [ASDF](https://asdf-vm.com/guide/getting-started.html)
#### Once ASDF is installed, add the following plugins:
* ASDF python plugin `asdf plugin add python`
* ASDF poetry plugin `asdf plugin add poetry`
* ASDF shellcheck plugin `asdf plugin add shellcheck`
* ASDF nodejs plugin `asdf plugin add nodejs`
#### Once the plugins are added you can install them
`asdf install` This will install the versions as described in .tool-versions

Now you can run `make install` to install the virtualenv and packages

## Developing/Debugging Tests

## Running the tests:
### Method 1 (Recommended):
Run the `runner.py` file located in the root of the project <br />
This is the preferred method and allows you to include/exclude tags <br />
a `~` before the tag name excludes it. <br />
This is how the tests are run on the CI
<h4> You MUST specify the environment and product <br />

#### Example: `python runner.py --product=CPTS-UI --env=INT --tags smoke --tags ~slow`
This will run all tests with the tag `@smoke` but skip any tests tagged with `@slow`

### Method 2:
If your IDE supports it, you can directly run the .feature files within `/features` <br />
Make sure that your behave run configuration includes the `--product=` & `--env=` <B>These are mandatory</B>

### Method 3:
Run the tests by calling the Make command `make run-tests`. This requires the parameters `product=` and `env=` to be passed in
* This will run the tests without tags so will run everything

### Method 4 (Not Recommended):
Run the tests by running `behave` in a command prompt or terminal window.
* This will run the tests and print the results to console

Example:
```
behave -D product=CPTS-UI -D env=INT -f behave_cucumber_formatter:PrettyCucumberJSONFormatter -o reports/cucumber_json.json -f
allure_behave.formatter:AllureFormatter -o allure-results -f pretty features --no-capture --no-capture-stderr --no-skipped --expand --logging-level=DEBUG --tags eps_fhir
```

Change the `env` variable accordingly to either `INT` or `INTERNAL-DEV`.
If you wish to test a different product then you must change `product=` and `--tags` respectively.
