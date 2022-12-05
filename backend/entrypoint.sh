./manage.py migrate
./manage.py search_index --rebuild -f
./manage.py collectstatic --noinput

gunicorn --chdir server --bind :8080 server.wsgi:application