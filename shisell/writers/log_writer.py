import json
import logging
from ..analytics_event_model import AnalyticsEventModel

__log = logging.getLogger('shisell')


def log_writer(event_model: AnalyticsEventModel):
    __log.info(json.dumps(event_model))
