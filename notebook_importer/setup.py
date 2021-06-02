#!/usr/bin/env python3

import setuptools
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(dir_path, 'README.md')) as f:
    long_description = f.read()

setuptools.setup(
    name='notebook_importer',
    version='0.0.1',
    description='Allows jupyter notebooks to be imported as python modules',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['notebook_importer'],
    install_requires=['ipython==7.24.0', 'nbformat==5.1.3'],
    python_requires='>=3.3',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
