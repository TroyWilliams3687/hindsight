#!/usr/bin/env python3
#-*- coding:utf-8 -*-

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

# ------------
# Custom Modules


# -------------
# Logging

# Assign the variable
log = logging.getLogger(__name__)
# -------------


@click.command('save')
@click.pass_context
def save(*args, **kwargs):
    """

    # Usage

    """

    # Extract the configuration file from the click context
    # config = args[0].obj['cfg']

    pass
