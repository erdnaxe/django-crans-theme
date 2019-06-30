# -*- mode: python; coding: utf-8 -*-
# Copyright (C) 2016-2019 by Cr@ns
# SPDX-License-Identifier: GPL-2.0-or-later
# This file is part of django-crans-theme.

import re
import sys

from setuptools import find_packages, setup


# Calculate the version number without importing the postorius package.
with open('src/crans_theme/__init__.py') as fp:
    for line in fp:
        mo = re.match("__version__ = '(?P<version>[^']+?)'", line)
        if mo:
            __version__ = mo.group('version')
            break
    else:
        print('No version number found')
        sys.exit(1)


setup(
    name="django-crans-theme",
    version=__version__,
    description="A Cr@ns theme for Django",
    long_description=open('README.md').read(),
    maintainer="Cr@ns",
    license='GPLv2',
    keywords='django crans theme',
    url="https://github.com/erdnaxe/django-crans-theme",
    classifiers=[
        "Framework :: Django",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Programming Language :: Python :: 3",
    ],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=[
        'Django>=1.11,<2.3',
    ],
    tests_require=[],
)
