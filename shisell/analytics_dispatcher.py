from typing import Callable, Any, List, Dict
from .analytics_context import AnalyticsContext
from .analytics_event_model import AnalyticsEventModel

FilterType = Callable[[AnalyticsEventModel], None]
JSON = Dict[str, Any]


class AnalyticsDispatcher:
    def __init__(self, dispatch: Callable[[str, AnalyticsContext], Any], context: AnalyticsContext = None):
        self.__dispatch = dispatch
        self.Context = context or AnalyticsContext()

    def dispatch(self, event_name: str, analytics_context: AnalyticsContext = None):
        context = self.Context if analytics_context is None else self.Context.union(analytics_context)
        return self.__dispatch(event_name, context)

    def with_context(self, analytics_context: AnalyticsContext):
        return AnalyticsDispatcher(self.dispatch, analytics_context)

    def create_scoped(self, scope: str):
        context = AnalyticsContext()
        context.Scopes = [scope]
        return self.with_context(context)

    def with_extras(self, extras: JSON):
        if not isinstance(extras, dict):
            return self

        context = AnalyticsContext()
        context.ExtraData = extras
        return self.with_context(context)

    def with_extra(self, key: str, value: Any):
        return self.with_extras({key: value})

    def with_filters(self, filters: List[FilterType]):
        if not filters:
            return self

        context = AnalyticsContext()
        context.Filters = filters
        return self.with_context(context)

    def with_filter(self, filter: FilterType):
        if not filter:
            return self

        return self.with_filters([filter])

    def with_meta(self, key: str, value: Any):
        context = AnalyticsContext()
        context.MetaData = {key: value}
        return self.with_context(context)

    def with_identities(self, identities: JSON):
        if not isinstance(identities, dict):
            return self

        context = AnalyticsContext()
        context.Identities = identities
        return self.with_context(context)

    def with_identity(self, key: str, value):
        return self.with_identities({key: value})
