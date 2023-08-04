.ONESHELL:
SHELL := /bin/bash


GREEN=\033[0;32m
RED=\033[0;31m
NC=\033[0m

VENVNAME=venv
VENVBIN=$(VENVNAME)/bin

CURR_DIR=$(PWD)

define done
    @echo -e "${GREEN} DONE${NC}"
endef

.PHONY: dependencies
dependencies:
	@echo -e "${GREEN} Installing virtualenv using pip3${NC}"
	@pip3 install virtualenv --user
	$(call done)

.PHONY: setup
setup:
	@echo -e "${GREEN} Creating new virtual environment${NC}"
	@python3 -m virtualenv $(VENVNAME)
	@echo -e "${GREEN} Installing requirements${NC}"
	@$(VENVBIN)/pip3 install -r requirements.txt
	@echo -e "${GREEN} Virtual environment successfully created!${NC}"
	$(call done)

.PHONY: clean
clean:
	@echo -e "${RED} Removing virtual environment${NC}"
	@rm -rf $(VENVNAME)/
	@echo -e "${RED} Removing python cached files${NC}"
	@find . | grep -E "(/__pycache__)" | xargs rm -rf
	$(call done)

.PHONY: run
run:
	@$(VENVBIN)/python3 manage.py runserver