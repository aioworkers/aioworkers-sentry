import pytest

from aioworkers_sentry.logging import SentryQueueHandler


@pytest.mark.parametrize('kwargs', [
    {},
    dict(dsn='https://<key>@sentry.io/<project>'),
])
def test_create_handler(kwargs, mocker):
    mocker.patch('asyncio.get_event_loop', lambda: None)
    assert SentryQueueHandler(**kwargs)
