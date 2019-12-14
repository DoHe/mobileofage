release: python3 manage.py migrate --noinput
web: gunicorn mobileofage.wsgi --log-file - -c gunicorn_conf.py