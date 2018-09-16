from multiprocessing.pool import ThreadPool

from .analytics_event_model import AnalyticsEventModel
from .analytics_context import AnalyticsContext
from .analytics_dispatcher import AnalyticsDispatcher
from .filters import default_filters
from .extenders import with_filter


def create_event_model(event_name: str, context: AnalyticsContext):
    event_model = AnalyticsEventModel()
    event_model.Name = event_name
    event_model.Scope = "_".join(context.Scopes)
    event_model.ExtraData = context.ExtraData.copy()
    event_model.MetaData = context.MetaData.copy()
    event_model.Identities = context.Identities.copy()

    for f in context.Filters:
        f(event_model)

    return event_model


def create_root_dispatcher(event_model_writer, root_context: AnalyticsContext = None):
    pool = ThreadPool(processes=1)

    def dispatch(name, context):
        event_model = create_event_model(name, context)
        return event_model_writer(event_model)

    def dispatch_in_background(name, context):
        return pool.apply_async(dispatch, (name, context))

    return AnalyticsDispatcher(dispatch_in_background, root_context).extend(with_filter(*default_filters))
