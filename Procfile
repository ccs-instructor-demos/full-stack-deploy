release: python manage.py migrate --settings=conf.settings.production
web: gunicorn conf.wsgi --log-file -