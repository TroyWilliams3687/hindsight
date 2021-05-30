#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# -----------
# SPDX-License-Identifier: MIT
# Copyright (c) 2021 Troy Williams

# uuid       = c3207508-b7ef-11eb-89b8-59b62252b88f
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

# ------------
# 3rd Party - From pip

import click

# ------------
# Custom Modules

from .common import run_cmd, write_json

# -------------
# Logging

# Assign the variable
log = logging.getLogger(__name__)
# -------------


@click.command("save")
@click.option(
    "--log", is_flag=True, help="Display the list of saved windows to STDOUT."
)
@click.pass_context
def save(*args, **kwargs):
    """

    # Usage

    """

    # Extract the configuration file from the click context
    paths = args[0].obj["paths"]

    # We will use the wmctrl program to save the active window positions
    # $ sudo apt install wmctrl

    # to capture the information we will use `$ wmctrl -Gl`

    # $ man wmctrl, -l:
    # List the windows being managed by the window manager. One line is output for each window, with the line broken
    # up into space separated columns.
    # - The first column always contains the window identity as a hexadecimal integer
    # - the second column always contains the desktop number (a -1 is used to identify a  sticky window)
    # - If the -p option is specified the next column will contain the PID for the window as a decimal integer
    # - If the -G option is specified then  four  integer  columns  will  follow:
    #   - x-offset
    #   - y-offset
    #   - width
    #   - height
    # - The next column always contains the client machine name. The remainder of the line contains the window title (possibly with multiple spaces in the title).

    cmd = ["wmctrl", "-lG"]

    results = run_cmd(cmd)

    # positions = [p.split()[:6] for p in results]
    items = [p.split() for p in results]

    if kwargs["log"]:

        for p in items:
            log.info(p)

    write_json(paths["locations"], items)

    if kwargs["log"]:

        log.info(f'Positions saved to {paths["locations"]}...')

    # NOTE: wmctrl -lG returns x and y in desktop coordinates, we have to multiply by the x and y scale factors to get the correct coordinates.
