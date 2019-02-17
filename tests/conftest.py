import asyncio
import logging

import pytest
from aiohttp.test_utils import make_mocked_coro


@pytest.fixture
def context(config, loop):
    # Clear handlers cache
    logger = logging.getLogger()
    logger.handlers = []
    from aioworkers.core.context import Context
    with Context(config, loop=loop) as ctx:
        yield ctx


@pytest.fixture
def config():
    from aioworkers.core.config import Config
    return Config(
        sentry={
            'cls': 'aioworkers_sentry.client.Sentry',
            'dsn': 'https://<key>@sentry.io/<project>',
        },
    )


@pytest.fixture
def wait_for_call(loop):
    async def do(mock, count=1, timeout=5, delay=0.1):
        passed = 0
        while passed < timeout:
            await asyncio.sleep(delay, loop=loop)
            passed += delay
            if mock.call_count >= count:
                return
        assert False, "Cannot reach call count..."

    return do


@pytest.fixture
def post(mocker):
    resp = mocker.stub()
    resp.status = 200
    mock = mocker.patch('aiohttp.client.ClientSession.post', make_mocked_coro(
        return_value=resp
    ))

    return mock
