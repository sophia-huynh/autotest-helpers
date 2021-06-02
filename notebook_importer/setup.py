#!/usr/bin/env python3

import setuptools

setuptools.setup(
    name='notebook_importer',
    version='0.0.1',
    packages=['notebook_importer'],
    install_requires=['ipython==7.24.0', 'nbformat==5.1.3'],
    python_requires='>=3.3'
)
