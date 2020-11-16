aioworkers-sentry
=================

.. image:: https://github.com/aioworkers/aioworkers-sentry/workflows/Tests/badge.svg
  :target: https://github.com/aioworkers/aioworkers-sentry/actions?query=workflow%3ATests

.. image:: https://codecov.io/gh/aioworkers/aioworkers-sentry/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/aioworkers/aioworkers-sentry

.. image:: https://img.shields.io/pypi/v/aioworkers-sentry.svg
  :target: https://pypi.org/project/aioworkers-sentry

.. image:: https://img.shields.io/pypi/pyversions/aioworkers-sentry.svg
  :target: https://pypi.org/project/aioworkers-sentry
  :alt: Python versions


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

Install dev requirements:


.. code-block:: shell

    pipenv install --dev --skip-lock


Run tests:

.. code-block:: shell

    pipenv run pytest
