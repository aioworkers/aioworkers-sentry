from pathlib import Path

try:
    # true
    from .version import __version__
except ImportError:
    __version__ = '0.0.0.dev0'


configs = Path(__file__).parent / 'sentry.ini',
