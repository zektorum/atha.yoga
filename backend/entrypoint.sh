if [ "$REFRESH_DATABASE" = true ]; then
  ./manage.py reset_db --noinput
fi

./manage.py migrate
./manage.py wait_for_elasticsearch

if [ "$REFRESH_DATABASE" = true ]; then
 ./manage.py seed
fi

./manage.py search_index --rebuild -f
./manage.py collectstatic --noinput
celery -A server.celery_app worker -c2 -l fatal &
celery -A server.celery_app beat -l info &
gunicorn --chdir server --bind :8000 server.wsgi:application
