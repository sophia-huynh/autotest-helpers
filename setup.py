#!/usr/bin/env python3

import setuptools
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
requires = [f"{p} @ file://{os.path.join(dir_path, p)}" for p in ('c_helper', 'sql_helper', 'notebook_importer')]

with open(os.path.join(dir_path, 'README.md')) as f:
    long_description = f.read()

setuptools.setup(
    name='autotest_helpers',
    version='0.0.1',
    description='Various python packages designed for use as helpers when writing test scripts',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/MarkUsProject/autotest-helpers.git',
    install_requires=requires,
    python_requires='>=3.3',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
