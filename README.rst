aioworkers-sentry
=================

.. image:: https://travis-ci.org/aioworkers/aioworkers-sentry.svg?branch=master
  :target: https://travis-ci.org/aioworkers/aioworkers-sentry

.. image:: https://img.shields.io/pypi/v/aioworkers-sentry.svg
  :target: https://pypi.python.org/pypi/aioworkers-sentry


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
