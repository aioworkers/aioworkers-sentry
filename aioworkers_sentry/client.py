from functools import partial

from aioworkers.core.base import AbstractEntity
from raven import Client
from raven.conf import setup_logging
from raven.handlers.logging import SentryHandler
from raven_aiohttp import QueuedAioHttpTransport


class Sentry(AbstractEntity):
    def __init__(self, config=None, *, context=None, loop=None):
        super().__init__(config, context=context, loop=loop)
        self.client = Client(
            config.dsn,
            transport=partial(
                QueuedAioHttpTransport,
                **config.get('transport', {}),
            )
        )
        self.handler = SentryHandler(
            self.client,
            **config.get('handler', {})
        )
        self.context.on_stop.append(self.on_stop)

    async def on_stop(self):
        # Stop transport on context stop
        await self.client.remote.get_transport().close()

    async def init(self):
        setup_logging(self.handler)
