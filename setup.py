#!/usr/bin/env python3
""" generate random passwords mike"""
# -*- coding: utf-8 -*-

import os
from setuptools import setup


def read(fname):
    """Utility function to read the README file. """
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="password-generator",
    version="0.1.0",
    author="Michael Prentiss",
    author_email="andrewjcarter@gmail.com",
    description=("a python password generator"),
    license="MIT",
    keywords="passwords",
    url="http://packages.python.org/an_example_pypi_project",
    packages=['an_example_pypi_project', 'tests'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
