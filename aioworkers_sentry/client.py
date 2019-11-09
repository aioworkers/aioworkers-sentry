from typing import Mapping, Optional

import sentry_sdk
from aioworkers.core.base import AbstractEntity
from aioworkers.utils import import_name


class Sentry(AbstractEntity):
    set_tag = sentry_sdk.set_tag
    set_user = sentry_sdk.set_user

    _client_config_keys = frozenset({
        'dsn', 'release', 'environment',
        'max_breadcrumbs', 'server_name',
        'shutdown_timeout',
        'in_app_include', 'in_app_exclude',
        'default_integrations', 'dist',
        'sample_rate',
        'send_default_pii',
        'http_proxy',
        'https_proxy',
        'ignore_errors',
        'request_bodies',
        'debug',
        'attach_stacktrace',
        'ca_certs',
        'propagate_traces',
        'traces_sample_rate',
        'traceparent_v2',
    })

    def __init__(self, config=None, *args, **kwargs):
        self.client = None  # type: Optional[sentry_sdk.Client]
        super().__init__(config, *args, **kwargs)

    def set_config(self, config):
        super().set_config(config)
        kwargs = {
            k: v for k, v in config.items()
            if k in self._client_config_keys
        }
        integrations = []
        for integr in config.get('integrations', ()):
            if isinstance(integr, str):
                params = {}
                name = integr
            elif isinstance(integr, Mapping):
                name, params = next(iter(integr.items()))
            else:
                continue
            factory = import_name(name)
            integrations.append(factory(**params))
        if integrations:
            kwargs.update(integrations=integrations)
        self.client = sentry_sdk.Client(**kwargs)
        sentry_sdk.Hub.main.bind_client(self.client)
