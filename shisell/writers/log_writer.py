import json
import logging

from ..analytics_event_model import AnalyticsEventModel


def create_log_writer(log_name='shisell'):
    logger = logging.getLogger(log_name)

    def writer(event_model: AnalyticsEventModel):
        logger.info(json.dumps(event_model.__dict__))

    return writer


log_writer = create_log_writer()
