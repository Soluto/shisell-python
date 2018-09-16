from .. import AnalyticsContext, AnalyticsDispatcher


def with_context(context: AnalyticsContext):
    return lambda dispatcher: AnalyticsDispatcher(dispatcher.dispatch, context)
