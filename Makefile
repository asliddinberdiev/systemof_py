run:
	python3 manage.py runserver

migrations:
	python3 manage.py makemigrations

migrate:
	python3 manage.py migrate

clear:
	python3 manage.py flush

super:
	python3 manage.py createsuperuser