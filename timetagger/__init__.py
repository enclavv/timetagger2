"""
Timetagger - Tag your time, get the insight.
"""

__version__ = "26.1.3+enclavv1"  # enclavv build: a local version label, so pip replaces the PyPI 26.1.3

version_info = tuple(map(int, __version__.split("+")[0].split(".")))


from ._config import config  # noqa
from . import server  # noqa - server logic
from . import common  # noqa - common assets
from . import images  # noqa - image assets
from . import app  # noqa - app assets
from . import pages  # noqa - pages
