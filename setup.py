#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# -----------
# SPDX-License-Identifier: MIT
# Copyright (c) 2021 Troy Williams

# uuid       = ff3c11de-b5b3-11eb-9fb7-a3fe2da49343
# author     = Troy Williams
# email      = troy.williams@bluebill.net
# date       = 2021-05-15
# -----------

"""
This module contains information for properly setting up a package that can
represent md_docs.
"""

# https://hynek.me/articles/testing-packaging/
# https://docs.python.org/3/distutils/setupscript.html


from setuptools import setup, find_packages

setup(
    name="hindsight",
    version="0.1",
    author="Troy Williams",
    author_email="troy.williams@bluebill.net",
    description="Remember the position of your open windows and restore them at a later point.",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        "click",
        "appdirs",
    ],
    entry_points={
        'console_scripts': [
            'hindsight=hindsight.hindsight:main',
        ],
    },
)
