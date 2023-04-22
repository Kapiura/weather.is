#!/usr/bin/bash bash
export DJANGO_SETTINGS_MODULE=PJS.settings
python3 manage.py check
python3 getting_info_about_weather.py