#!/usr/bin/env python3

import setuptools

setuptools.setup(
    name='sql_helper',
    version='0.0.1',
    packages=['sql_helper'],
    install_requires=['psycopg2-binary==2.8.6'],
    python_requires='>=3.3'
)
