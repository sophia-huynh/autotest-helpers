#!/usr/bin/env python3

import setuptools
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
requires = [f"{p} @ file://{os.path.join(dir_path, p)}" for p in ('c_helper', 'sql_helper', 'notebook_importer')]

setuptools.setup(
    name='autotest_helpers',
    version='0.0.1',
    install_requires=requires,
    python_requires='>=3.3'
)
