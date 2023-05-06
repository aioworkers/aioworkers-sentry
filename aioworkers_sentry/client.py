import multiprocessing
from typing import Any, Dict, Mapping, Optional

import sentry_sdk
from aioworkers.core.base import AbstractEntity
from aioworkers.core.config import ValueExtractor
from aioworkers.utils import import_name

TAG_PROCESS = "process"


class Sentry(AbstractEntity):
    set_tag = staticmethod(sentry_sdk.set_tag)
    set_user = staticmethod(sentry_sdk.set_user)
    set_extra = staticmethod(sentry_sdk.set_extra)
    start_span = staticmethod(sentry_sdk.start_span)
    capture_event = staticmethod(sentry_sdk.capture_event)
    capture_message = staticmethod(sentry_sdk.capture_message)
    capture_exception = staticmethod(sentry_sdk.capture_exception)
    add_breadcrumb = staticmethod(sentry_sdk.add_breadcrumb)
    last_event_id = staticmethod(sentry_sdk.last_event_id)
    start_transaction = staticmethod(sentry_sdk.start_transaction)
    set_measurement = staticmethod(sentry_sdk.set_measurement)

    _client_config_keys = frozenset(
        {
            "ca_certs",
            "dist",
            "dsn",
            "environment",
            "http_proxy",
            "https_proxy",
            "ignore_errors",
            "in_app_exclude",
            "in_app_include",
            "proxy_headers",
            "release",
            "request_bodies",
            "server_name",
            "traceparent_v2",
        }
    )
    _client_config_bool = frozenset(
        {
            "attach_stacktrace",
            "auto_enabling_integrations",
            "auto_session_tracking",
            "debug",
            "default_integrations",
            "enable_tracing",
            "include_local_variables",
            "propagate_traces",
            "send_default_pii",
            "with_locals",  # old
        }
    )
    _client_config_int = frozenset(
        {
            "max_breadcrumbs",
            "transport_queue_size",
        }
    )
    _client_config_float = frozenset(
        {
            "profiles_sample_rate",
            "sample_rate",
            "shutdown_timeout",
            "traces_sample_rate",
        }
    )
    _client_config_factory = frozenset(
        {
            "traces_sampler",
        }
    )

    def __init__(self, *args, **kwargs):
        self.client: Optional[sentry_sdk.Client] = None
        super().__init__(*args, **kwargs)

    def set_config(self, config: ValueExtractor):
        super().set_config(config)

        kwargs = {}
        for k in self.config:
            if k in self._client_config_bool:
                kwargs[k] = self.config.get_bool(k)
            elif k in self._client_config_int:
                kwargs[k] = self.config.get_int(k)
            elif k in self._client_config_float:
                kwargs[k] = self.config.get_float(k)
            elif k in self._client_config_factory:
                kwargs[k] = import_name(self.config.get(k))
            elif k in self._client_config_keys:
                kwargs[k] = self.config.get(k)

        integrations = []
        for integr in config.get("integrations", ()):
            if isinstance(integr, str):
                params: Dict[str, Any] = {}
                name = integr
            elif isinstance(integr, Mapping):
                name, params = next(iter(integr.items()))
            else:
                raise ValueError(integr)
            factory = import_name(name)
            integrations.append(factory(**params))
        if integrations:
            kwargs.update(integrations=integrations)
        self.client = sentry_sdk.Client(**kwargs)
        sentry_sdk.Hub.main.bind_client(self.client)

    async def init(self):
        await super().init()
        tags = self.config.get("tags")
        if isinstance(tags, list):
            if TAG_PROCESS in tags:
                sentry_sdk.set_tag(
                    TAG_PROCESS,
                    multiprocessing.current_process().name,
                )
