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

Basic config example:

.. code-block:: yaml

    sentry:
        cls: aioworkers_sentry.client.Sentry
        dsn: <your sentry dsn>
        handler:
            level: ERROR
            tags:
                env: PROD
        transport:
            workers: 1
            qsize: 500



Development
-----------

Install dev requirements:


.. code-block:: shell

    pipenv install --dev --skip-lock


Run tests:

.. code-block:: shell

    pytest