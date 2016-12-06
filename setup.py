#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='stix2-patterns',
    version='0.2.0',
    packages=find_packages(),
    description='Validate STIX 2 Patterns.',
    install_requires=[
        "antlr4-python2-runtime==4.5.3 ; python_version < '3'",
        "antlr4-python3-runtime==4.5.3 ; python_version >= '3'",
        "enum34 ; python_version ~= '3.3.0'",
        "six",
    ],
    entry_points={
        'console_scripts': [
            'validate-patterns = stix2patterns.validator:main',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
