#!/bin/sh

echo "Waiting for database..."

until python -c "
import pymysql, os

pymysql.connect(
    host=os.environ['DB_HOST'],
    port=int(os.environ.get('DB_PORT', 3306)),
    user=os.environ['DB_USER'],
    password=os.environ['DB_PASSWORD'],
).close()
" 2>/dev/null
do
  sleep 2
done

echo "Database is ready."

python manage.py migrate
python manage.py collectstatic --noinput

exec "$@"