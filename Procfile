web: gunicorn project.wsgi --log-file -
worker: celery -A project worker -l info --without-gossip --without-mingle --without-heartbeat
