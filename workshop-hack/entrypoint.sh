#!/bin/sh

if [ ! -e /workshop-hack/hackut/settings.py ]; then
    cp /workshop-hack/hackut/settings.py.dev /workshop-hack/hackut/settings.py
  fi;

python manage.py migrate --run-syncdb

if [ "${DEBUG}" = true ]; then
    python manage.py collectstatic --noinput --link -v 0
else
    python manage.py collectstatic --noinput -v 0
fi;

exec "$@"
