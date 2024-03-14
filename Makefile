.ONESHELL:
RED=\033[0;31m
NC=\033[0m # No Color
ENV_PREFIX=$(shell python -c "if __import__('pathlib').Path('venv/Scripts/pip').exists(): print('venv/Scripts/pip.exe ')")
SHELL = /usr/bin/perl
.SHELLFLAGS = -e

.PHONY: help
help: ## Show the help
	@echo Usage: make {target}
	@echo ...
	@echo Targets:
	@findstr /r "##" Makefile | findstr -V findstr

.PHONY: install
install: ## Install requirements
	@echo creating venv...
	@rmdir /s /q venv || echo Not found
	@python -m venv venv
	@venv\Scripts\python.exe -m pip install -U pip
	@venv\Scripts\pip.exe install -r requirements.txt
	@echo ...
	@echo !!! Please run `venv\Scripts\activate` to enable the environment !!!

.PHONY: dev
dev: ## Install development mode dependencies
	@venv\Scripts\pip.exe install -e .[dev]

.PHONY: lint
lint: ## Install development mode dependencies
	@$(ENV_PREFIX)flake8 src || echo ...
	@$(ENV_PREFIX)mypy --ignore-missing-imports -m src || echo ...
	@$(ENV_PREFIX)pyink -l 99 --check ./ || echo ...
