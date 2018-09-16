from .with_context import with_context
from .. import AnalyticsContext


def create_scoped(scope: str):
    context = AnalyticsContext()
    context.Scopes.append(scope)
    return with_context(context)
