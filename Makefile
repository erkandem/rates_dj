
# via https://gist.github.com/prwhite/8168133
help:  ## Show this help.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

reqs:  ## compile application requirements
	pip-compile requirements/common.in -o requirements.txt

reqs-dev:  ## compile development and testing requirements
	pip-compile requirements/dev.in -o requirements-dev.txt

reqs-test:  ## compile development and testing requirements
	pip-compile requirements/test.in -o requirements-test.txt

reqs-all:  ## compile both app and dev requirements
	make reqs && make reqs-dev && make reqs-test

install-dev: ## install development packages
	pip install -r requirements-dev.txt

install-test: ## install development packages
	pip install -r requirements-test.txt

clean:  ## remove .pyc and __pycache__
	py3clean .

run:  ## run rev server
	python manage.py runserver
