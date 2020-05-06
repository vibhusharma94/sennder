PIP = pip

develop:
	@echo "--> Installing Python dependencies"
	# order matters here, base package must install first
	$(PIP) install --upgrade "setuptools>=0.9.8" "pip>=8.0.0"
	$(PIP) install -r requirements.txt


test: lint test-python


lint:
	@echo "--> Linting python"
	flake8 sennder/
	@echo ""

test-python:
	@echo "Running tests"
	pytest tests/

server:
	flask run

server-uwsgi:
	uwsgi --http :5000 --wsgi-file wsgi.py --callable app -H venv


celery: celery worker -A wsgi.celery --loglevel=INFO
celery-beat:  celery beat -A wsgi.celery --schedule=/tmp/celerybeat-schedule --loglevel=INFO --pidfile=/tmp/celerybeat.pid

test-coverage: coverage run -m pytest tests/
