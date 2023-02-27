SHELL := /bin/bash

GREEN := \033[32m
RESET := \033[39m
ARROW := \033[1m\033[31m>$(GREEN)>\033[33m>$(RESET)

venv/bin/python:
	@ echo -e "${ARROW} Installing virtual environment..."
	@ python3.10 -m venv venv
	@ venv/bin/pip install -r requirements.txt

init: venv/bin/python
	@ echo -e "${ARROW} Initialize..."
	@ venv/bin/python scripts/make.py
	@ echo -e "[${GREEN}OK${RESET}] Initialized"

env: venv/bin/python
	@ echo -e "${ARROW} Compiling environment..."
	@ venv/bin/pip freeze > requirements.txt
	@ echo -e "[${GREEN}OK${RESET}] Compiled"

build: venv/bin/python
	@ echo -e "${ARROW} Building..."
	@ venv/bin/python scripts/build.py -l fr
	@ echo -e "[${GREEN}OK${RESET}] Built (fr)"

.PHONY: init, env, build