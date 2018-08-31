#! /bin/bash

# Check for dependencies like flask

export FLASK_APP=flaskr
export FLASK_ENV=development

if command -v python3 &>/dev/null; then
	echo Python 3 is installed
	echo I am assuming pip3 is also installed.
	# for templates
	eval $(pip install jinja2)

	eval $(pip install flask)
	eval $(flask initdb)
else
	echo Python 3 is not installed. Please install Python 3.
	# I'm not sure you want your students' code to update python...?
	# eval $(apt-get install python3)
fi
