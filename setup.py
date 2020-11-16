#!/usr/bin/env python

import pathlib
import sys

from setuptools import find_packages, setup

version = __import__('aioworkers_sentry').__version__

requirements = [
    'aioworkers>=0.13',
    'sentry_sdk>=0.14.3',
]

if sys.version_info < (3, 7):
    requirements.append('aiocontextvars')

test_requirements = [
    'pytest',
    'pyyaml',
    'pytest-runner',
    'pytest-mock',
    'pytest-aioworkers',
    'pytest-flake8',
    'pytest-isort',
    'pytest-mypy',
]

readme = pathlib.Path('README.rst').read_text()


setup(
    name='aioworkers-sentry',
    version=version,
    description='aioworkers plugin for Sentry',
    long_description=readme,
    author='Alexander Bogushov',
    author_email='abogushov@gmail.com',
    url='https://github.com/aioworkers/aioworkers-sentry',
    packages=find_packages(include=['aioworkers_sentry']),
    include_package_data=True,
    install_requires=requirements,
    python_requires='>=3.5.3',
    license='Apache Software License 2.0',
    keywords='aioworkers sentry',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Framework :: AsyncIO',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    test_suite='tests',
    tests_require=test_requirements,
)
