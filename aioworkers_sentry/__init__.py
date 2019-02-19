from pathlib import Path

try:
    from .version import __version__
except ImportError:
    __version__ = 'dev'


configs = Path(__file__).parent / 'sentry.ini',
