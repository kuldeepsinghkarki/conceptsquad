#!/bin/bash
#exec python3 manage.py migrate
exec python3 manage.py createsuperuser
exec python3 manage.py runserver 8002
"$@"
