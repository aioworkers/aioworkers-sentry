import pytest
from sentry_sdk import Client


@pytest.fixture
def config_yaml():
    return """
    sentry:
        cls: aioworkers_sentry.client.Sentry
        dsn: https://key@localhost/123
        debug: false
        max_breadcrumbs: 5
        traces_sample_rate: 0.9
        tags:
            - process
        integrations:
            - sentry_sdk.integrations.logging.LoggingIntegration
            - sentry_sdk.integrations.logging.LoggingIntegration:
                level: ERROR
    """


@pytest.fixture
def catch_sentry(context, mocker):
    params: dict = {}

    def callback(*args, **kwargs):
        params.update(kwargs, args=args)

    client: Client = context.sentry.client
    mocker.patch.object(client, "capture_event", callback)

    return params
