#!/usr/bin/env python3
#-*- coding:utf-8 -*-

# -----------
# SPDX-License-Identifier: MIT
# Copyright (c) 2021 Troy Williams

# uuid       = f6792b10-b7f5-11eb-89b8-59b62252b88f
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
import math

# ------------
# 3rd Party - From pip

import click

# ------------
# Custom Modules

from .common import run_cmd, read_json

# ------------
# Custom Modules


# -------------
# Logging

log = logging.getLogger(__name__)
# -------------

@click.command('restore')
@click.option('--log',
              is_flag=True,
              help='Display the list of saved windows to STDOUT.')
@click.pass_context
def restore(*args, **kwargs):
    """

    # Usage

    """

    # Extract the configuration file from the click context
    paths = args[0].obj['paths']

    items = read_json(paths['locations'])

    if items is None:
        log.info('Nothing to restore!')

        return

    # Determine the scale factors for the x and y position
    # The scale factor will help restore the windows to the correct position given the system has
    # 2 monitors at different resolutions and the system thinks we have 5760x2160 virtual desktop

    # monitor 1: 1920 x 1080
    # monitor 2: 3840 x 2160

    m1 = [1920, 1080]
    m2 = [3840, 2160]

    scale_x = m1[0]/m2[0]
    scale_y = m1[1]/m2[1]

    for p in items:
        wid, deskid, x, y, w, h, *title = p

        title = " ".join(title)

        if kwargs['log']:
            log.info(f'Restoring: id={wid}, x={x}, y={y}, w={w}, h={h}, {title}')

        x = int(x)
        y = int(y)

        if 'Firefox' in title:

            x -= 7
            y -= 8

        elif 'Sublime Text' in title:

            x = math.floor(x*scale_x) + 2
            y = math.floor(y*scale_y) + 121

        elif 'Discord' in title:

            x -= 10
            # y = math.floor(y*scale_y) + 121

        else:

            x = math.floor(x*scale_x)
            y = math.floor(y*scale_y)

        # w = int(w)
        # h = int(h)

        if kwargs['log']:
            log.info(f'scaled: id={wid}, x={x}, y={y}, w={w}, h={h}, {" ".join(p[6:])}')
            log.info(f'wmctrl -ir {wid} -e 0,{x},{y},{w},{h}')

        results = run_cmd([
            'wmctrl',
            '-ir', wid,
            '-e', f'0,{x},{y},{w},{h}',
        ])

        for r in results:
            log.info(r)

    # The data structure:
    #   [
    #   "0x02600008",  # Window ID (Hex)
    #   "2",           # Desktop number
    #   "70",          # x-offset
    #   "460",         # y-offset
    #   "940",         # width
    #   "500",         # height
    #   "vidar",
    #   "\ud83c\udfe1-parents-only",
    #   "-",
    #   "Discord"
    # ]

    # We are going to use `$ wmctrl -ir wid -e 0,x,y,w,h` to restore the window position

    # ------------
    # -i
    # Interpret  window  arguments  (<WIN>) as a numeric value rather than a string name for the window. If the nu‐
    # meric value starts with the prefix '0x' it is assumed to be a hexadecimal number.


    # -r <WIN>
    #     Specify a target window for an action.

    # -e <MVARG>
    # Resize and move a window that has been specified with a -r action according to the <MVARG> argument.

    # <MVARG>
    # A move and resize argument has the format 'g,x,y,w,h'.  All five components are integers. The first value, g,
    # is the gravity of the window, with 0 being the most common value (the default value for the  window).  Please
    # see the EWMH specification for other values.

    # The  four  remaining values are a standard geometry specification: x,y is the position of the top left corner
    # of the window, and w,h is the width and height of the window, with the exception that the value of -1 in  any
    # position is interpreted to mean that the current geometry value should not be modified.
    # ------------

