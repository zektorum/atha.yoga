./manage.py migrate
./manage.py search_index --rebuild -f
./manage.py collectstatic --noinput

wget https://raw.githubusercontent.com/eficode/wait-for/master/wait-for
chmod +x wait-for
./wait-for http://localhost:9200 -- gunicorn --chdir server --bind :8000 server.wsgi:application