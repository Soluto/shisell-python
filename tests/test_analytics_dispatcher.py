import unittest
import copy
from unittest.mock import Mock

from shisell import AnalyticsDispatcher, AnalyticsContext

RETURN_VALUE = 'some_return_value'
EVENT_NAME = 'some_event_name'


class AnalyticsDispatcherTestSuite(unittest.TestCase):
    def setUp(self):
        dispatch_mock = Mock(name='dispatch')
        dispatch_mock.return_value = RETURN_VALUE
        self.dispatch_mock = dispatch_mock

        self.dispatcher = AnalyticsDispatcher(dispatch_mock)
        self.original_context = copy.deepcopy(self.dispatcher.Context)

    def test_dispatch_values(self):
        """
        should call dispatch with given values
        """

        context = AnalyticsContext()
        context.ExtraData['key'] = 'value'

        result = self.dispatcher.dispatch(EVENT_NAME, context)

        self.dispatch_mock.assert_called_once_with(EVENT_NAME, context)
        self.assertEqual(result, RETURN_VALUE)

    def test_dispatch_no_context(self):
        """
        should not throw if context is undefined
        """

        result = self.dispatcher.dispatch(EVENT_NAME)

        self.dispatch_mock.assert_called_once_with(EVENT_NAME, self.dispatcher.Context)
        self.assertEqual(result, RETURN_VALUE)

    def test_extend(self):
        """
        should call extender
        """

        expected_result = 'some_dispatcher'
        extender = Mock(name='extender')
        extender.return_value = expected_result

        result = self.dispatcher.extend(extender)
        extender.assert_called_once_with(self.dispatcher)

        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
