"""Sharing Geometry Dash levels through CLI."""

__description__ = "Sharing Geometry Dash levels through CLI."
__url__ = "https://github.com/nekitdev/gd.share"

__title__ = "share"
__author__ = "nekitdev"
__license__ = "MIT"
__version__ = "1.0.0"

from gd.share.main import share
from gd.share.version import version_info

__all__ = ("share", "version_info")
