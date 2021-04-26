#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='l2x_synthetic',
    version='1.0.0',
    description='4 simple customizable synthetic datasets from Chen et al., 2018 (L2X): Orange Skin, XOR, Non-linear Additive and Switch.',
    author='Jianbo Chen. Distributed by Jeroen Overschie.',
    url='https://github.com/dunnkers/L2X',
    packages=find_packages(include=['l2x_synthetic', 'l2x_synthetic.*']),
    install_requires=[
        'numpy',
        'pandas'
    ],
    setup_requires=['flake8', 'pytest-runner'],
    tests_require=['pytest']
)
