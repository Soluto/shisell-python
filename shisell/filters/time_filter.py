import datetime
from ..analytics_event_model import AnalyticsEventModel


def time_filter(event_model: AnalyticsEventModel):
    event_model.ExtraData["Time"] = datetime.datetime.utcnow().isoformat()
