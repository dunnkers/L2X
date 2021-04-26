#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='chen-tabular-synthetic-datasets',
    version='1.0.0',
    description='4 simple customizable synthetic datasets from Chen et al., 2018 (L2X): Orange Skin, XOR, Non-linear Additive and Switch.',
    author='Jianbo Chen',
    url='https://github.com/dunnkers/L2X',
    packages=find_packages(include=['synthetic', 'synthetic.*'])
)
