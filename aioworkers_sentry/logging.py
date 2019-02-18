import asyncio
from functools import partial

from raven.handlers.logging import SentryHandler
from raven_aiohttp import QueuedAioHttpTransport


class SentryQueueHandler(SentryHandler):
    def __init__(self, *args, **kwargs):
        kwargs['transport'] = partial(
            QueuedAioHttpTransport,
            **kwargs.get('transport', {}),
            loop=asyncio.get_event_loop(),
        )
        super().__init__(*args, **kwargs)
