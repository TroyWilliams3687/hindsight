#!/bin/bash

# -----------
# SPDX-License-Identifier: MIT
# Copyright (c) 2021 Troy Williams

# uuid       = e79faa2a-b88f-11eb-96c0-41de2ca30456
# author     = Troy Williams
# email      = troy.williams@bluebill.net
# date       = 2021-05-19
# -----------

# Set the script to halt on errors
# set -e

# saner programming env: these switches turn some bugs into errors
# source: https://stackoverflow.com/questions/192249/how-do-i-parse-command-line-arguments-in-bash
# set -o errexit -o pipefail -o noclobber -o nounset

# Code:

# https://superuser.com/questions/205334/how-do-you-get-ubuntu-to-automatically-run-a-program-every-time-the-screen-is-un
# https://superuser.com/a/411124

# Change the path to the full, absolute path
EXE=~/repositories/projects/hindsight/.venv/bin/hindsight

dbus-monitor --session "type='signal',interface='org.gnome.ScreenSaver',member='ActiveChanged'" | while read line ; do
    if [ x"$(echo "$line" | grep 'boolean true')" != x ] ; then

        # runs once when screensaver comes on...
        echo "Screen locked detected - saving window positions..."
        ${EXE} save

    fi
    if [ x"$(echo "$line" | grep 'boolean false')" != x ] ; then

        # runs once when screensaver goes off...
        echo "Screen unlocked detected - restoring window positions..."
        ${EXE} restore

    fi
done