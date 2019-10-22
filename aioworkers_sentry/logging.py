from raven.handlers.logging import SentryHandler


class SentryQueueHandler(SentryHandler):
    def __init__(self, transport=None, **kwargs):
        self.config = kwargs
        super().__init__(**kwargs)
        if transport:
            self.config['transport'] = transport
