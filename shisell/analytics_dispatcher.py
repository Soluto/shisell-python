from typing import Callable, Any

from .analytics_context import AnalyticsContext


class AnalyticsDispatcher:
    def __init__(self, dispatch: Callable[[str, AnalyticsContext], Any], context: AnalyticsContext = None):
        self.__dispatch = dispatch
        self.Context = context or AnalyticsContext()

    def dispatch(self, event_name: str, analytics_context: AnalyticsContext = None):
        context = self.Context if analytics_context is None else self.Context.union(analytics_context)
        return self.__dispatch(event_name, context)

    def extend(self, *args):
        result = self

        for extend in args:
            result = extend(result)

        return result
