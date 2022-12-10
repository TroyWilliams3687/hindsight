#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# -----------
# SPDX-License-Identifier: MIT
# Copyright (c) 2022 Troy Williams

# uuid:   c3a2fcbe-771a-11ed-9e21-04cf4bfb0bc5
# author: Troy Williams
# email:  troy.williams@bluebill.net
# date: {% now 'utc', '%Y-%m-%d' %}
# -----------

import os
import fnmatch
import functools
import itertools
import configparser

from pathlib import Path

config = configparser.ConfigParser()
config.read('.sconstruct.ini')

env = Environment(ENV=os.environ)

# Read the values from the ini file:
env['PY'] = Path(config['environment']['PY']).resolve()
env['BIN'] = Path(config['environment']['BIN']).resolve()

#NOTE: Typically these are targets used in actions and can be resolved
#by using the $PY...

# --------
# methods and functions

def PhonyTargets(env=None, **kw):
    """
    Create a Phony i.e. a task that doesn't really build/compile
    anything.

    source: https://github.com/SCons/scons/wiki/PhonyTargets
    """

    if not env:
        env = DefaultEnvironment()

    for target, action in kw.items():
        env.AlwaysBuild(env.Alias(target, [], action))


def find_target_paths(
        start:str=None,
        patterns:[str]=None,
        folders_only:bool=False,
        folder_ignores:[str]=None,
    ) -> [str]:
    """
    Returns a generator yielding files matching the given patterns

    start - Directory to search for files/directories under. Defaults
    to current dir.

    patterns - Patterns of files to search for. Defaults to
    ["*"]. Example: ["*.json", "*.xml"]

    folders_only - Indicates we only want to return folders. Otherwise
    only return files

    folder_ignores - a list of folder names to ignore ['.venv'].

    """

    # setup the defaults
    path = start or "."
    path_patterns = patterns or ["*"]
    ignore_paths = folder_ignores or []

    for root_dir, dir_names, file_names in os.walk(path):

        # Check to see if we have any ignore folders to ignore
        if any([ip in root_dir for ip in ignore_paths]):
            # print(f'{root_dir} -> ignored')
            break

        # setup the filter by pre-populating the items with a partial function
        filter_partial = functools.partial(fnmatch.filter, file_names)

        if folders_only:
            filter_partial = functools.partial(fnmatch.filter, dir_names)

        for item in itertools.chain(*map(filter_partial, path_patterns)):
            yield os.path.join(root_dir, item)


# ----
# Builders

# pip_install = Builder(action="$BIN/python -m pip install -r $TARGET")
# env.Append(BUILDERS={"Pipinstaller": pip_install})

# ----
# Help

Help("""
      Type: `scons` - Create a venv if it doesn't exist and install packages
            `scons venv` - Create a venv if it doesn't exist
            `scons packages` - Install the python packages into the existing vevn
            `scons remove` -  Delete the venv
            `scons clean` - Remove any python caches, bytecode files, or other remnants
            `scons test` - Run the test harness(es)
            `scons lint` - Run the linter(s)
      """)

# ----
# Alias

# give new or alternative names to commands or groups of commands
# https://scons.org/doc/production/HTML/scons-user.html

env.Alias('venv', ['.venv', env.Alias('packages')])
env.Alias('remove', [env.Alias('remove_venv'), env.Alias('clean')])

# Default Command - $ scons <- this is equivalent to $scons venv
env.Default(env.Alias('venv'))


# ----
# Dependency Graph - Commands

# ----
# $scons .venv

# Create the virtual environment

env.Command(
    target='.venv',
    source= None,
    action=[
        "$PY -m virtualenv $TARGET",
        Touch("$TARGET"),
    ],
)

# ----
# $scons packages

# install the packages into the virtual environment

PhonyTargets(env=env, packages=[
        "$BIN/python -m pip install --upgrade -r requirements.txt",
        "$BIN/python -m pip install --upgrade -r dev-requirements.txt",
        "$BIN/python -m pip install -e .", # only required if this is a package
    ],
)

# NOTE: If you want to reinstall everything, use `scons remove` and `scons`.

#----
# scons clean

# clean up all the support files

PhonyTargets(
    env=env,
    clean=[
        Delete(list(find_target_paths(patterns=["*.pyc"], folder_ignores=['.venv']))),
        Delete(list(find_target_paths(patterns=[
                    "*.egg-info",
                    "__pycache__",
                    ".pytest_cache",
                    ".ipynb_checkpoints"
                ], folders_only=True, folder_ignores=['.venv']))),
    ]
)


# ----
# scons remove

# remove the virtual environment

PhonyTargets(
    env=env,
    remove_venv=[
        Delete(".venv"),
    ],
)


# ----
# scons test

PhonyTargets(
    env=env,
    test=[
        "$BIN/pytest",
    ],
)

# ----
# scons black

PhonyTargets(
    env=env,
    format=[
        "$BIN/black ./src",
    ],
)

# ----
# scons lint

PhonyTargets(
    env=env,
    lint=[
        "$BIN/flack8 ./src",
    ],
)
