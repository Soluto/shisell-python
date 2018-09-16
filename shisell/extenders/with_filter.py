from typing import Callable, List

from .with_context import with_context
from .. import AnalyticsEventModel, AnalyticsContext

Filter = Callable[[AnalyticsEventModel], None]


def with_filter(*filters: Filter):
    context = AnalyticsContext()
    context.Filters.extend(filters)
    return with_context(context)
