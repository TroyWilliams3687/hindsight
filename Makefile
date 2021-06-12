# -----------
# SPDX-License-Identifier: MIT
# Copyright (c) 2021 Troy Williams

# uuid       = e846e160-cb8a-11eb-9f40-79b2f2a7c797
# author     = Troy Williams
# email      = troy.williams@bluebill.net
# date       = 2021-06-06
# -----------

# -----------
# Information

# This is the prototype for the main Makefile in Python code repositories. It
# will make use of the `Makefile.python` to deal with the majority of python
# functionality that the repos will require. It will also help to make the main
# Makefile clean and contain only specific things that are required for the
# individual repository.


# -----------
# Variables

# The location to the python installation to use - we have an environment
# variable set with the correct path. The variable is set in `~/.bashrc` and
# will point to something like python=`~/opt/python_3.9.5/bin`

PYPATH?=$(python)

# define the binary to use
PY?=$(PYPATH)/python3.9

include Makefile.python
include Makefile.python.build  # Optional


# -----
# make clean

# Remove any created documents from the build process

## make clean - Remove the build components
.PHONY: clean
clean:
	@echo "Cleaning PyPI build folder..."
	@rm -rf build
	@echo "Cleaning PyPI dist folder..."
	@rm -rf dist
	@echo "Cleaning Build Output..."
	@rm -rf output

# ------
# make remove

# Remove the Virtual Environment and clean the cached files

## make remove - Remove the virtual environment and all cache files.
.PHONY: remove
remove: remove-venv
	@echo "Removing ${VENV} and Cached Files..."