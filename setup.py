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
from pathlib import Path

README = Path(__file__).parent.joinpath("README.md").read_text()

setup(
    name="hindsight-ubuntu",
    version="0.0.3",
    description="Remember the position, size and virtual desktop of your open windows and restore them at a later point.",
    author="Troy Williams",
    author_email="troy.williams@bluebill.net",
    url="https://github.com/TroyWilliams3687/hindsight",
    long_description=README,
    long_description_content_type="text/markdown",
    license='MIT',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Operating System :: POSIX :: Linux",
        "Topic :: Desktop Environment :: Gnome",
    ],
    python_requires=">=3.9",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        "click",
        "appdirs",
        "pyyaml",
    ],
    entry_points={
        'console_scripts': [
            'hindsight=hindsight.hindsight:main',
        ],
    },
)
