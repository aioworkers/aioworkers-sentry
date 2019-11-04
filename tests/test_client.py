import logging

from sentry_sdk import Hub


async def test_capture_exc(catch_sentry):
    assert not catch_sentry

    try:
        1 / 0
    except ZeroDivisionError:
        Hub.current.capture_exception()

    assert catch_sentry


async def test_logging(catch_sentry):
    assert not catch_sentry
    logging.getLogger().critical('error')
    assert catch_sentry
