import unittest
import copy
from unittest.mock import Mock

from shisell import AnalyticsDispatcher, AnalyticsContext
from shisell.extenders import create_scoped, with_context, with_extra, with_extras, with_filter, with_identity, with_identities, with_meta

RETURN_VALUE = 'some_return_value'
EVENT_NAME = 'some_event_name'


class ExtendersTestSuite(unittest.TestCase):
    def setUp(self):
        dispatch_mock = Mock(name='dispatch')
        dispatch_mock.return_value = RETURN_VALUE
        self.dispatch_mock = dispatch_mock

        self.dispatcher = AnalyticsDispatcher(dispatch_mock)
        self.original_context = copy.deepcopy(self.dispatcher.Context)

    def test_with_context(self):
        """
        should call dispatch with passed context
        """

        context = AnalyticsContext()
        context.ExtraData = {'extra_key': 'some other data'}
        context.MetaData = {'meta_key': 'some other data'}
        context.Scopes = ['other', 'scope']

        self.dispatcher.extend(with_context(context)).dispatch(EVENT_NAME)

        self.dispatch_mock.assert_called_once_with(EVENT_NAME, context)
        self.assertEqual(self.dispatcher.Context, self.original_context)

    def test_create_scoped(self):
        """
        should call dispatch with passed scope
        """

        scope = "some_scope"
        context = AnalyticsContext()
        context.Scopes.append(scope)

        self.dispatcher.extend(create_scoped(scope)).dispatch(EVENT_NAME)

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

        self.dispatcher.extend(with_extra(key, value)).dispatch(EVENT_NAME)

        self.dispatch_mock.assert_called_once_with(EVENT_NAME, context)
        self.assertEqual(self.dispatcher.Context, self.original_context)

    def test_with_extras(self):
        """
        should call dispatch with all extras
        """

        extras = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
        context = AnalyticsContext()
        context.ExtraData = extras

        self.dispatcher.extend(with_extras(extras)).dispatch(EVENT_NAME)

        self.dispatch_mock.assert_called_once_with(EVENT_NAME, context)
        self.assertEqual(self.dispatcher.Context, self.original_context)

    def test_with_extras_doesnt_throw(self):
        """
        should return same dispatcher if invalid input
        """

        dispatcher = self.dispatcher.extend(with_extras(None))

        self.assertIs(dispatcher, self.dispatcher)

    def test_with_filter(self):
        """
        should call dispatch with passed filter
        """

        filter = 'some_filter'
        context = AnalyticsContext()
        context.Filters.append(filter)

        self.dispatcher.extend(with_filter(filter)).dispatch(EVENT_NAME)

        self.dispatch_mock.assert_called_once_with(EVENT_NAME, context)
        self.assertEqual(self.dispatcher.Context, self.original_context)

    def test_with_filters(self):
        """
        should call dispatch with all filters
        """

        filters = ['filter1', 'filter2']
        context = AnalyticsContext()
        context.Filters = filters

        self.dispatcher.extend(with_filter(*filters)).dispatch(EVENT_NAME)

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

        self.dispatcher.extend(with_meta(key, value)).dispatch(EVENT_NAME)

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

        self.dispatcher.extend(with_identity(key, value)).dispatch(EVENT_NAME)

        self.dispatch_mock.assert_called_once_with(EVENT_NAME, context)
        self.assertEqual(self.dispatcher.Context, self.original_context)

    def test_with_identities(self):
        """
        should call dispatch with all passed identities
        """

        identities = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
        context = AnalyticsContext()
        context.Identities = identities

        self.dispatcher.extend(with_identities(identities)).dispatch(EVENT_NAME)

        self.dispatch_mock.assert_called_once_with(EVENT_NAME, context)
        self.assertEqual(self.dispatcher.Context, self.original_context)

    def test_with_identities_doesnt_throw(self):
        """
        should return same dispatcher if invalid input
        """

        dispatcher = self.dispatcher.extend(with_identities(None))

        self.assertIs(dispatcher, self.dispatcher)


if __name__ == '__main__':
    unittest.main()
