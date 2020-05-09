import multiprocessing
from typing import Any, Dict, Mapping, Optional

import sentry_sdk
from aioworkers.core.base import AbstractEntity
from aioworkers.core.config import ValueExtractor
from aioworkers.utils import import_name

TAG_PROCESS = 'process'


class Sentry(AbstractEntity):
    set_tag = sentry_sdk.set_tag
    set_user = sentry_sdk.set_user
    set_extra = sentry_sdk.set_extra
    start_span = sentry_sdk.start_span
    capture_event = sentry_sdk.capture_event
    capture_message = sentry_sdk.capture_message
    capture_exception = sentry_sdk.capture_exception
    add_breadcrumb = sentry_sdk.add_breadcrumb
    last_event_id = sentry_sdk.last_event_id

    _client_config_keys = frozenset({
        'dsn', 'release', 'environment',
        'with_locals',
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

    def __init__(self, *args, **kwargs):
        self.client = None  # type: Optional[sentry_sdk.Client]
        super().__init__(*args, **kwargs)

    def set_config(self, config: ValueExtractor):
        super().set_config(config)
        kwargs = {
            k: v for k, v in config.items()
            if k in self._client_config_keys
        }
        if not kwargs.get('dsn'):
            return None
        integrations = []
        for integr in config.get('integrations', ()):
            if isinstance(integr, str):
                params = {}  # type: Dict[str, Any]
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

    async def init(self):
        await super().init()
        tags = self.config.get('tags')
        if isinstance(tags, list):
            if TAG_PROCESS in tags:
                sentry_sdk.set_tag(
                    TAG_PROCESS, multiprocessing.current_process().name,
                )
