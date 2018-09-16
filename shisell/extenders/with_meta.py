from typing import Any

from .with_context import with_context
from .. import AnalyticsContext


def with_meta(key: str, value: Any):
    context = AnalyticsContext()
    context.MetaData[key] = value
    return with_context(context)
