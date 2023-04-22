POETRY_VERSION :=$(shell poetry --version)

poetry/setup:
ifdef POETRY_VERSION
	@echo "Found poetry version $(POETRY_VERSION)"
else
	@echo "Poetry not found, starting to install poetry"
	pip install pip -U
	pip install setuptools
	pip install poetry
	@echo "Installed poetry version" $(shell poetry --version)
endif

poetry/install-dependencies:
	poetry install

code-quality/setup:
	poetry add flake8
	poetry add unimport
	poetry add isort
	poetry add black
	poetry add pytest

code-quality/scan:
	poetry run flake8
	poetry run unimport --check .
	poetry run isort --check .
	poetry run black --check .

code-quality/format:
	poetry run unimport -r .
	poetry run isort .
	poetry run black .

code-quality/tests:
	poetry run pytest tests/
