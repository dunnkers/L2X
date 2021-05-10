#!/usr/bin/env python

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    LONG_DESC = fh.read()
    setup(
        name="l2x-synthetic",
        version="2.0.0",
        description="4 simple customizable synthetic datasets from Chen et al., 2018 (L2X): Orange Skin, XOR, Non-linear Additive and Switch.",
        license="MIT",
        long_description=LONG_DESC,
        long_description_content_type="text/markdown",
        author="Jianbo Chen. Distributed by Jeroen Overschie.",
        url="https://github.com/dunnkers/L2X",
        packages=find_packages(include=["l2x_synthetic", "l2x_synthetic.*"]),
        install_requires=["numpy==1.20.2", "pandas==1.2.4"],
        setup_requires=["black==21.4b2", "pytest-runner==5.3.0"],
        tests_require=["pytest==6.2.3"],
    )
