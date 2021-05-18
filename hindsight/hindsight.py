#!/usr/bin/env python3
#-*- coding:utf-8 -*-

# -----------
# SPDX-License-Identifier: MIT
# Copyright (c) 2021 Troy Williams

# uuid       = be569314-b7ee-11eb-89b8-59b62252b88f
# author     = Troy Williams
# email      = troy.williams@bluebill.net
# date       = 2021-05-18
# -----------

"""
"""

# ------------
# System Modules - Included with Python

import sys
import logging

from pathlib import Path

# ------------
# 3rd Party - From pip

import click

# ------------
# Custom Modules

from .save import save

# -------------
# Logging

# configure logging for this module - it is a bit different here because
# it is intended to be executed by the user <http://nathanielobrown.com/blog/posts/quick_and_dirty_python_logging_lesson.html>

# Logging Levels:
# CRITICAL
# ERROR
# WARNING
# INFO
# DEBUG
# NOTSET

# get the root logger
logger = logging.getLogger()
logger.setLevel(logging.INFO) # change logging level here...

# make a console logger
console = logging.StreamHandler()

# add the console logger to the root logger
logger.addHandler(console)

# Assign the variable
log = logging.getLogger(__name__)
# -------------

@click.group()
@click.version_option()
@click.pass_context
def main(*args, **kwargs):
    """

    # Parameters

    build_cfg:str
        - The path to the YAML configuration file to use to drive the process.

    # Usage


    """

    # Initialize the shared context object to a dictionary and configure it for the app
    ctx = args[0]
    ctx.ensure_object(dict)


# -----------
# Add the child menu options

main.add_command(save)
# main.add_command(pdf)
