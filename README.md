# Hermes Graphs library
[![Build Status](https://travis-ci.org/ekiourk/hermes.svg?branch=master)](https://travis-ci.org/ekiourk/hermes)

### How do I install hermes for development?

You need to have python3 installed on your system

1. Create yourself a Python3 virtual environment: `virtualenv -p python3 ~/hermes_env`
2. Activate the virtualenv: `source ~/hermes_env/bin/activate`
3. Install all requirements by calling `./install_requirements_develop.sh` from the root of the project

### How do I run the tests and the example?

1. First install hermes on a virtualenv by following the steps above
2. Call `run-contexts -sv tests` for the unitests
4. Call `./examples/shipping_operator.py` to run the example