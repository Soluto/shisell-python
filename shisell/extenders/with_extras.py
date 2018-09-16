from typing import Any, Dict

from .with_context import with_context
from .. import AnalyticsContext

Extras = Dict[str, Any]


def with_extras(extras: Extras):
    if not isinstance(extras, dict):
        return lambda x: x

    context = AnalyticsContext()
    context.ExtraData.update(extras)
    return with_context(context)


def with_extra(key: str, value: Any):
    return with_extras({key: value})

