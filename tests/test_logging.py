import logging

import pytest


@pytest.fixture
def config():
    from aioworkers.core.config import Config
    return Config(
        sentry={
            'cls': 'aioworkers_sentry.client.Sentry',
            'dsn': 'https://<key>@sentry.io/<project>',
            'handler': {'level': 'ERROR'}
        },
    )


async def test_logging(context, post, wait_for_call):
    logging.error(f"error")

    await wait_for_call(post)
