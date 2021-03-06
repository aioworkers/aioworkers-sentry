import pytest
from sentry_sdk import Client


@pytest.fixture
def config_yaml():
    return """
    sentry:
        cls: aioworkers_sentry.client.Sentry
        dsn: https://key@localhost/123
        integrations:
            - sentry_sdk.integrations.aiohttp.AioHttpIntegration
            - sentry_sdk.integrations.logging.LoggingIntegration:
                level: ERROR
    """


@pytest.fixture
def catch_sentry(context, mocker):
    params = {}

    def callback(*args, **kwargs):
        params.update(kwargs, args=args)

    client = context.sentry.client  # type: Client
    mocker.patch.object(client.transport, 'capture_event', callback)

    return params
