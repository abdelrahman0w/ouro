.PHONY: clean clean-build clean-pyc clean-test coverage dist docs help install lint lint/flake8 lint/black
.DEFAULT_GOAL := help

define BROWSER_PYSCRIPT
import os
import sys
import webbrowser

from urllib.request import pathname2url


webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re
import sys


for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

BROWSER := python -c "$$BROWSER_PYSCRIPT"

SITE_PACKAGES := $(shell python -c 'import site; print(site.getsitepackages()[0])')

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: clean-build clean-pyc clean-test clear-my-py ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	@rm -rf build/
	@rm -rf dist/
	@rm -rf .eggs/
	@find . -name '*.egg-info' -exec rm -rf {} +
	@find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@find . -name '*~' -exec rm -f {} +
	@find . -name '__pycache__' -exec rm -rf {} +

clean-test: ## remove test and coverage artifacts
	@rm -rf .tox/
	@rm -f .coverage
	@rm -rf htmlcov/
	@rm -rf .pytest_cache

clear-my-py: ## remove mypy cache
	@find . -name '.mypy_cache' -exec rm -rf {} +

lint/flake8: ## check style with flake8
	@flake8 ouro tests

lint/black: ## check style with black
	@black --check ouro tests

lint: lint/flake8 lint/black ## check style

test: ## run tests quickly with the default Python
	@pytest

test-all: ## run tests on every Python version with tox
	@tox

dist: clean ## builds source and wheel package
	@python setup.py sdist
	@python setup.py bdist_wheel
	@ls -l dist

install: clean ## install the package to the active Python's site-packages
	@python setup.py install

uninstall: clean ## uninstall the package from the active Python's site-packages
	@cd $(SITE_PACKAGES) && rm -rf ouro*
