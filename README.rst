aioworkers-sentry
=================

.. image:: https://img.shields.io/pypi/v/aioworkers-sentry.svg
  :target: https://pypi.org/project/aioworkers-sentry

.. image:: https://github.com/aioworkers/aioworkers-sentry/workflows/Tests/badge.svg
  :target: https://github.com/aioworkers/aioworkers-sentry/actions?query=workflow%3ATests

.. image:: https://codecov.io/gh/aioworkers/aioworkers-sentry/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/aioworkers/aioworkers-sentry
  :alt: Coverage

.. image:: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v0.json
  :target: https://github.com/charliermarsh/ruff
  :alt: Code style: ruff

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
  :target: https://github.com/psf/black
  :alt: Code style: black

.. image:: https://img.shields.io/badge/types-Mypy-blue.svg
  :target: https://github.com/python/mypy
  :alt: Code style: Mypy

.. image:: https://readthedocs.org/projects/aioworkers-sentry/badge/?version=latest
  :target: https://github.com/aioworkers/aioworkers-sentry#readme
  :alt: Documentation Status

.. image:: https://img.shields.io/pypi/pyversions/aioworkers-sentry.svg
  :target: https://pypi.org/project/aioworkers-sentry
  :alt: Python versions

.. image:: https://img.shields.io/pypi/dm/aioworkers-sentry.svg
  :target: https://pypi.org/project/aioworkers-sentry

.. image:: https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg
  :alt: Hatch project
  :target: https://github.com/pypa/hatch


aioworkers plugin to work with Sentry. Creates Sentry client and handler according configuration
and setup logging.

Usage
-----

Install plugin:

.. code-block:: shell

    pip install aioworkers-sentry


Add to your config:

.. code-block:: yaml

    sentry:
        dsn: <your sentry dsn>
        release: 1.0.0
        environment: DEV
        integrations:
          - sentry_sdk.integrations.aiohttp.AioHttpIntegration


Development
-----------

Check code:

.. code-block:: shell

    hatch run lint:all


Format code:

.. code-block:: shell

    hatch run lint:fmt


Run tests:

.. code-block:: shell

    hatch run pytest


Run tests with coverage:

.. code-block:: shell

    hatch run cov
