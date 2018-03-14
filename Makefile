.PHONY: default

default: migrate

install:
	PIPENV_VENV_IN_PROJECT=true pipenv install

migrate:
	PIPENV_VENV_IN_PROJECT=true pipenv run python manage.py migrate

service:
	./systemd/create_service.sh
	chwon -R nginx:nginx .
	mkdir -p /run/uwsgi
	chown -R nginx:nginx /run/uwsgi
	mkdir -p /var/log/uwsgi
	touch /var/log/uwsgi/notes.log
	chown nginx:nginx /var/log/uwsgi/notes.log

static:
	PIPENV_VENV_IN_PROJECT=true pipenv run python manage.py collectstatic
