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

    async def init(self):
        setup_logging(self.handler)
