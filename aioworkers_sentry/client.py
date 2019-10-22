import logging
from functools import partial

from aioworkers.core.base import AbstractEntity
from raven import Client
from raven_aiohttp import QueuedAioHttpTransport

from aioworkers_sentry.logging import SentryQueueHandler


class Sentry(AbstractEntity):
    def __init__(self, config=None, *args, **kwargs):
        super().__init__(config, *args, **kwargs)
        self.handler = None
        self.client = None
        self.sync_remote = None
        for h in logging.getLogger().handlers:
            if isinstance(h, SentryQueueHandler):
                self.handler = h
                self.client = h.client
                self.sync_remote = self.client.remote

    async def init(self):
        if self.client is None:
            return
        cfg = dict(self.config.new_parent(self.handler.config))
        cfg.pop('cls', None)
        cfg.pop('name', None)
        transport = cfg.pop('transport', {})
        client = Client(
            **cfg,
            transport=partial(
                QueuedAioHttpTransport,
                **transport,
                loop=self.loop,
            ),
        )
        self.client.remote = client.remote
        self.context.on_cleanup.append(self.cleanup)

    async def cleanup(self):
        remote = self.client.remote
        self.client.remote = self.sync_remote
        # Stop transport on context disconnect
        await remote.get_transport().close()
