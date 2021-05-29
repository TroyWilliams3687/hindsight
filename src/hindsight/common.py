#!/usr/bin/env python3
#-*- coding:utf-8 -*-

# -----------
# SPDX-License-Identifier: MIT
# Copyright (c) <year> <copyright holders>

# uuid       =
# author     = Troy Williams
# email      = troy.williams@bluebill.net
# date       =
# -----------

"""
This is a template python script for use in creating other classes and applying
a standard to them
"""

# ------------
# System Modules - Included with Python

import sys
import logging
import subprocess
import json

# ------------
# 3rd Party - From pip

# ------------
# Custom Modules


# -------------
# Logging

# Assign the variable
log = logging.getLogger(__name__)
# -------------


def write_json(path, items):
    """

    Write the items to a .json file.

    # Parameters

    path - pathlib.Path
        - the path to the file to write the data too

    items - object
        - data structure to serialize to json

    # NOTE

    It is expected that items contains objects that json can serialize

    """

    with path.open("w", encoding="utf-8") as fo:
        print(json.dumps(items,
                         sort_keys=False,
                         indent=2), file=fo)


def read_json(path):
    """
    Read items from a .json file, returning python objects. This is
    the pair of the "write_json" method.

    # Parameters

    path - pathlib.Path
        - the path to the file to write the date to

    # Note

    The deserialized objects may need further processing

    """

    # the path isn't set or doesn't exist...
    if path is None or not path.exists():
        return None

    with path.open("r", encoding="utf-8") as f:
        return json.loads(f.read())

def run_cmd(cmd, **kwargs):
    """
    Takes the list of arguments, cmd, and executes them via subprocess. It prints
    stdout to the terminal to report on progress or issues.

    # Parameters

    cmd: list[str]
        - The command and list of switches to execute

    # Parameters (kwargs)

    cwd:pathlib.Path
        - The path to change the current working directory too
        - Default - None

    # NOTE

    Reference: https://docs.python.org/3/library/subprocess.html

    >>> import shlex, subprocess
    >>> command_line = input()
    /bin/vikings -input eggs.txt -output "spam spam.txt" -cmd "echo '$MONEY'"
    >>> args = shlex.split(command_line)
    >>> print(args)
    ['/bin/vikings', '-input', 'eggs.txt', '-output', 'spam spam.txt', '-cmd', "echo '$MONEY'"]
    >>> p = subprocess.Popen(args) # Success!

    Using shlex and pasting the command into repl can make this process much easier to work with.

    """

    cwd = kwargs["cwd"] if "cwd" in kwargs else None

    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, universal_newlines=True, cwd=cwd)

    # Gather the output from stdout to a list
    output = [l.strip() for l in p.stdout]

    # # Send the output to the logger
    # for l in output:
    #     log.info(l)

    return output
