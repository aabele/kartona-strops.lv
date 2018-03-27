#!/usr/bin/env bash

python manage.py thumbnail cleanup
#python manage.py thumbnail clear_delete_all
python ./manage.py build
python ./manage.py build  # Because of sorl
