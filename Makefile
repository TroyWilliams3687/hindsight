# -----------
# SPDX-License-Identifier: MIT
# Copyright (c) 2021 Troy Williams

# uuid       = eb910f22-b7ed-11eb-89b8-59b62252b88f
# author     = Troy Williams
# email      = troy.williams@bluebill.net
# date       = 2021-05-18
# -----------

# ----------
# Variables

# The location to the python installation to use - we have an environment
# variable set with the correct path
PYPATH = ${python}

# The name of the virtual environment to use
VENV = .venv

# The path to the bin folder in the virtual environment. We define this
# so we can use the correct binaries
BIN=$(VENV)/bin

# Set the search path so the venv is searched first
export PATH := $(BIN):$(PATH)

# ---
# all

# What do we execute if `$ make` is called?
# We'll simple build the virtual environment if it doesn't exist. You could modify this
# to build the html or pdf -> `all: $(VENV) html`

all: $(VENV)

# -------------------
# Virtual Environment

$(VENV): requirements.txt
	@$(PYPATH)/virtualenv $(VENV)

	# --------------------
	# Install Requirements

	@$(BIN)/python -m pip install --upgrade -r requirements.txt

	# -----------------------
	# Install Custom Packages

	# we need to install this package for things to work
	@$(BIN)/python -m pip install --editable .

	# -------------
	# Pretty Errors
	#(https://github.com/onelivesleft/PrettyErrors/)

	# install the pretty errors module and set it up to format errors globally for the virtual environment

	@$(BIN)/python -m pip install pretty_errors
	@$(BIN)/python -m pretty_errors -s

	@touch $(VENV)

# ------
# pypi

.PHONY: pypi
pypi: $(VENV)
	@echo "Generating Python Package for PYPI..."
	@$(BIN)/python setup.py sdist bdist_wheel

# -----w
# Black

.PHONY: black
black: $(VENV)
	@echo "Applying Black Code Formatting..."
	@$(BIN)/black src/

# ------
# Remove

# Remove the Virtual Environment and clean the cached files

.PHONY: remove
remove:
	@echo "Removing ${VENV} and Cached Files..."
	@find . -type d -name ${VENV} -exec rm -r {} +
	@find . -type d -name dist -exec rm -r {} +
	@find . -type d -name '*.egg-info' -exec rm -r {} +
	@find . -type d -name __pycache__ -exec rm -r {} +
	@find . -type f -name *.pyc -delete
	@find . -type d -name .pytest_cache -exec rm -r {} +
	@find . -type d -name .ipynb_checkpoints -exec rm -r {} +

