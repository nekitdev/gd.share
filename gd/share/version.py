from versions.versioned import get_version

from gd import share

__all__ = ("version_info",)

version_info = get_version(share)  # type: ignore
