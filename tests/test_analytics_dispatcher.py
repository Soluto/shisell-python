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

    def test_dispatch(self):
        """
        should call dispatch with given values
        """

        result = self.dispatcher.dispatch(EVENT_NAME)

        self.dispatch_mock.assert_called_once_with(EVENT_NAME, self.dispatcher.Context)
        self.assertEqual(result, RETURN_VALUE)

    def test_with_context(self):
        """
        should call dispatch with passed context
        """

        context = AnalyticsContext()
        context.ExtraData = {'extra_key': 'some other data'}
        context.MetaData = {'meta_key': 'some other data'}
        context.Scopes = ['other', 'scope']

        self.dispatcher.with_context(context).dispatch(EVENT_NAME)

        self.dispatch_mock.assert_called_once_with(EVENT_NAME, context)
        self.assertEqual(self.dispatcher.Context, self.original_context)

    def test_create_scoped(self):
        """
        should call dispatch with passed scope
        """

        scope = "some_scope"
        context = AnalyticsContext()
        context.Scopes.append(scope)

        self.dispatcher.create_scoped(scope).dispatch(EVENT_NAME)

        self.dispatch_mock.assert_called_once_with(EVENT_NAME, context)
        self.assertEqual(self.dispatcher.Context, self.original_context)

    def test_with_extra(self):
        """
        should call dispatch with passed extra data
        """

        key = 'some_key'
        value = 'some_value'
        context = AnalyticsContext()
        context.ExtraData[key] = value

        self.dispatcher.with_extra(key, value).dispatch(EVENT_NAME)

        self.dispatch_mock.assert_called_once_with(EVENT_NAME, context)
        self.assertEqual(self.dispatcher.Context, self.original_context)

    def test_with_extras(self):
        """
        should call dispatch with all extras
        """

        extras = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
        context = AnalyticsContext()
        context.ExtraData = extras

        self.dispatcher.with_extras(extras).dispatch(EVENT_NAME)

        self.dispatch_mock.assert_called_once_with(EVENT_NAME, context)
        self.assertEqual(self.dispatcher.Context, self.original_context)

    def test_with_filter(self):
        """
        should call dispatch with passed filter
        """

        filter = 'some_filter'
        context = AnalyticsContext()
        context.Filters.append(filter)

        self.dispatcher.with_filter(filter).dispatch(EVENT_NAME)

        self.dispatch_mock.assert_called_once_with(EVENT_NAME, context)
        self.assertEqual(self.dispatcher.Context, self.original_context)

    def test_with_filters(self):
        """
        should call dispatch with all filters
        """

        filters = ['filter1', 'filter2']
        context = AnalyticsContext()
        context.Filters = filters

        self.dispatcher.with_filters(filters).dispatch(EVENT_NAME)

        self.dispatch_mock.assert_called_once_with(EVENT_NAME, context)
        self.assertEqual(self.dispatcher.Context, self.original_context)

    def test_with_metadata(self):
        """
        should call dispatch with passed meta data
        """

        key = 'some_key'
        value = 'some_value'
        context = AnalyticsContext()
        context.MetaData[key] = value

        self.dispatcher.with_meta(key, value).dispatch(EVENT_NAME)

        self.dispatch_mock.assert_called_once_with(EVENT_NAME, context)
        self.assertEqual(self.dispatcher.Context, self.original_context)

    def test_with_identity(self):
        """
        should call dispatch with passed identity
        """

        key = 'some_key'
        value = 'some_value'
        context = AnalyticsContext()
        context.Identities[key] = value

        self.dispatcher.with_identity(key, value).dispatch(EVENT_NAME)

        self.dispatch_mock.assert_called_once_with(EVENT_NAME, context)
        self.assertEqual(self.dispatcher.Context, self.original_context)

    def test_with_identities(self):
        """
        should call dispatch with all passed identities
        """

        identities = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
        context = AnalyticsContext()
        context.Identities = identities

        self.dispatcher.with_identities(identities).dispatch(EVENT_NAME)

        self.dispatch_mock.assert_called_once_with(EVENT_NAME, context)
        self.assertEqual(self.dispatcher.Context, self.original_context)


if __name__ == '__main__':
    unittest.main()
