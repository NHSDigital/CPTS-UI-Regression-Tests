[![Regression Tests](https://github.com/NHSDigital/cpts-ui-regression-tests/actions/workflows/regression_tests.yml/badge.svg?branch=main)](https://github.com/NHSDigital/electronic-prescription-service-api-regression-tests/actions/workflows/regression_tests.yml)

![Warning](https://img.freepik.com/free-vector/warning-sign-with-warning-word_78370-4060.jpg "Warning Image")
<b> !!! The information provided here has been copied from [Electronic Prescription Service API Regression Tests](https://github.com/NHSDigital/electronic-prescription-service-api-regression-tests/) as has much of the code.
This is to provide a template repo which will be modified once active development beings on the Clinical Prescription Tracking Service.
</br>
The information provided here is not likely to be correct and should be updated with accurate information !!!
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
It is *NOT* currently necessary to set some Environment variables  to run any tests in your local environment. <br />
You can supply environment variables and the tests will look for environment variables in the following order:
1. `.env` file
2. OS environment variable

Any file that begins with `.env` is automatically ignored by Git

### Preparing your development environment
This test pack utilises the power of Docker to quickly and easily spin up a dev environment for you to work in
the Dockerfile is located in `{project_root}/.devcontainer/Dockerfile`

### Setup without docker development environment
If you'd like to use your own machine without containerisation. You will need the following;
* Ubuntu (WSL)
* [ASDF](https://asdf-vm.com/guide/getting-started.html)
#### Once ASDF is installed, add the following plugins:
	asdf plugin add python
	asdf plugin add poetry
	asdf plugin add shellcheck
	asdf plugin add nodejs
	asdf plugin add actionlint
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
<h4> You MUST specify the product with needs to be `CPTS-UI` <br />

#### Example: `python runner.py --product=CPTS-UI --tags smoke --tags ~slow`
This will run all tests with the tag `@smoke` but skip any tests tagged with `@slow`
*tags not currently functional*

### Method 2:
Run the tests by calling the Make command `make run-tests`.
* This will run the tests without tags so will run everything


## Recording new tests:
Playwright contains a handy (but not perfect) feature which will record actions you make and give you the code for them
to begin, run the command: <br />
`playwright codegen`
