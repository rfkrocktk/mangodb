#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name = "mangodb",
    version = "1.0.0",
    packages = find_packages('.'),
    package_dir = { '': '.'},
    url = "https://github.com/dcramer/mangodb",
    install_requires = [
        'setuptools',
        'gevent',
    ],
    entry_points = {
        'console_scripts': [
            'mangodb = server'
        ]
    }
)
