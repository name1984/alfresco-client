#!/bin/bash

#START GUNICORN PROCESS
echo Starting Gunicorn ...
exec gunicorn alfresco_client.wsgi:application --bind 0.0.0.0:9000 --workers 3