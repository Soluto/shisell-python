import datetime
import unittest
from unittest.mock import Mock

from shisell import create_root_dispatcher, AnalyticsEventModel
from shisell.extenders import create_scoped, with_identity, with_filter
from .mock_datetime import mock_datetime_now, real_datetime_class

RETURN_VALUE = 'some_return_value'
EVENT_NAME = 'some_event_name'
EVENT_TIME = real_datetime_class(2017, 1, 1)


def create_event_model():
    event_model = AnalyticsEventModel()
    event_model.Name = EVENT_NAME
    event_model.ExtraData['Time'] = EVENT_TIME.isoformat()
    return event_model


@mock_datetime_now(EVENT_TIME, datetime)
class CreateRootDispatcherTestSuite(unittest.TestCase):
    def setUp(self):
        event_model_writer = Mock()
        event_model_writer.return_value = RETURN_VALUE
        self.event_model_writer = event_model_writer

        self.dispatcher = create_root_dispatcher(event_model_writer)

    def test_scopes(self):
        """
        should concatenate scopes with _
        """
        scope1 = 'scope1'
        scope2 = 'scope2'
        event_model = create_event_model()
        event_model.Scope = scope1 + '_' + scope2

        result = self.dispatcher.extend(create_scoped(scope1), create_scoped(scope2)).dispatch(EVENT_NAME)

        self.assertEqual(result.get(), RETURN_VALUE)
        self.event_model_writer.assert_called_once_with(event_model)

    def test_identities(self):
        """
        should copy identities
        """
        key = 'some_key'
        value = 'some_value'
        event_model = create_event_model()
        event_model.Identities[key] = value

        result = self.dispatcher.extend(with_identity(key, value)).dispatch(EVENT_NAME)

        self.assertEqual(result.get(), RETURN_VALUE)
        self.event_model_writer.assert_called_once_with(event_model)

    def test_run_all_filters(self):
        """
        should run all filters
        """

        def filter1(model: AnalyticsEventModel):
            model.ExtraData["key1"] = "value1"

        def filter2(model: AnalyticsEventModel):
            model.ExtraData["key2"] = "value2"

        event_model = create_event_model()
        filter1(event_model)
        filter2(event_model)

        result = self.dispatcher.extend(with_filter(filter1, filter2)).dispatch(EVENT_NAME)

        self.assertEqual(result.get(), RETURN_VALUE)
        self.event_model_writer.assert_called_once_with(event_model)

    def test_run_filters_sequentially(self):
        """
        should run filters sequentially
        """
        def first_filter(model: AnalyticsEventModel):
            model.ExtraData["key"] = "firstFilter"

        def last_filter(model: AnalyticsEventModel):
            model.ExtraData["key"] = "lastFilter"

        event_model = create_event_model()
        last_filter(event_model)

        result = self.dispatcher.extend(with_filter(first_filter), with_filter(last_filter)).dispatch(EVENT_NAME)

        self.assertEqual(result.get(), RETURN_VALUE)
        self.event_model_writer.assert_called_once_with(event_model)


if __name__ == '__main__':
    unittest.main()
