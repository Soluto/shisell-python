from typing import Any, Dict

from .with_context import with_context
from .. import AnalyticsContext

Identities = Dict[str, Any]


def with_identities(identities: Identities):
    if not isinstance(identities, dict):
        return lambda x: x

    context = AnalyticsContext()
    context.Identities.update(identities)
    return with_context(context)


def with_identity(key: str, value):
    return with_identities({key: value})
