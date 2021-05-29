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

Reference:
- https://askubuntu.com/questions/631392/saving-and-restoring-window-positions

"""

# ------------
# System Modules - Included with Python

import sys
import logging

from pathlib import Path

# ------------
# 3rd Party - From pip

import click
from appdirs import AppDirs

# ------------
# Custom Modules

from .save import save
from .restore import restore

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

__appname__ = "hindsight"
__company__ = "bluebill.net"

def common_paths():
    """
    The paths that the application will commonly use for storing settings
    and caching things.

    """

    dirs = AppDirs()

    paths = {
        "config": Path(dirs.user_config_dir).joinpath(__company__).joinpath(__appname__),
    }

    paths['config'].mkdir(parents=True, exist_ok=True)

    paths["locations"] = paths["config"].joinpath("locations.json")

    return paths

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

    ctx.obj['paths'] = common_paths()

# -----------
# Add the child menu options

main.add_command(save)
main.add_command(restore)
