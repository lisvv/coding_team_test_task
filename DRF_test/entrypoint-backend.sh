#!/bin/bash

while ! python3 manage.py makemigrations; do
  echo "make migrations"
done

while ! python3 manage.py migrate; do
  echo "creating tables in data base"
done

while ! python3 manage.py loadall; do
  echo "load fixtures"
done

exec "$@"
