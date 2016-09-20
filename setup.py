#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='OpenShift Flask Example',
    version='0.0.1',
    author='Samuel Gonçalves e Rai Sena',
    author_email='samukasaww@live.com',
    install_requires=['Flask','aiml'],
)
