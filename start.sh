#! /bin/bash

# Check for dependencies like flask

export FLASK_APP=flaskr
export FLASK_ENV=development

if command -v python3 &>/dev/null; then
	echo Python 3 is installed
	eval $(export FLASK_APP=flaskr)
	eval $(export FLASK_ENV=development)
	eval $(flask run)
else
	echo Python 3 is not installed
fi
