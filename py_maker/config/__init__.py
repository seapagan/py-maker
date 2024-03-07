"""Settings module."""

from typing import Any

from .settings import Settings


def get_settings(*args: Any, **kwargs: Any) -> Settings:  # noqa: ANN401
    """Return a singleton instance of the Settings class."""
    return Settings.get_instance("pymaker", *args, **kwargs)


__all__ = ["Settings", "get_settings"]
