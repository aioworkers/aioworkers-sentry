import logging

import pytest
from aioworkers.core.config import ValueExtractor
from sentry_sdk import Hub

from aioworkers_sentry.client import Sentry


async def test_config_exc(context):
    sentry = Sentry(context=context)

    with pytest.raises(ValueError):
        sentry.set_config(
            ValueExtractor(
                {
                    "integrations": [1],
                }
            )
        )


def sampler(x):  # no cov
    return 1


async def test_config_factory(context):
    sentry = Sentry(context=context)

    sentry.set_config(
        ValueExtractor(
            {
                "traces_sampler": "tests.test_client.sampler",
            }
        )
    )


async def test_capture_exc(catch_sentry):
    assert not catch_sentry

    try:
        1 / 0
    except ZeroDivisionError:
        Hub.current.capture_exception()

    assert catch_sentry


async def test_logging(catch_sentry):
    assert not catch_sentry
    logging.getLogger().critical("error")
    assert catch_sentry
