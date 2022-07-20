release: python manage.py makemigrations --no-input
release: python manage.py migrate --no-input
release: python manage.py runscript student_load


web: gunicorn accounting_system.wsgi
