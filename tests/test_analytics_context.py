import unittest
import copy

from shisell import AnalyticsContext


class AnalyticsContextTestSuite(unittest.TestCase):
    def setUp(self):
        context = AnalyticsContext()
        context.ExtraData['extra'] = 'value'
        context.MetaData['meta'] = 'data'
        context.Identities['identity'] = 'id'
        context.Scopes.append('some_scope')
        context.Filters.append('some_filter')
        self.context = context

    def test_union_returns_copy(self):
        union = self.context.union(None)

        self.assertIsNot(union, self.context)
        self.assertEqual(union, self.context)

    def test_union_returns_union(self):
        original_context = copy.deepcopy(self.context)

        new_context = AnalyticsContext()
        new_context.ExtraData['other_extra'] = 'other_value'
        new_context.MetaData['other_meta'] = 'other_data'
        new_context.Identities['other_identity'] = 'other_id'
        new_context.Scopes.append('other_scope')
        new_context.Filters.append('other_filter')

        expected_context = AnalyticsContext()
        expected_context.ExtraData = {**self.context.ExtraData, **new_context.ExtraData}
        expected_context.MetaData = {**self.context.MetaData, **new_context.MetaData}
        expected_context.Identities = {**self.context.Identities, **new_context.Identities}
        expected_context.Scopes = self.context.Scopes + new_context.Scopes
        expected_context.Filters = self.context.Filters + new_context.Filters

        union = self.context.union(new_context)
        self.assertEqual(union, expected_context)
        self.assertEqual(self.context, original_context)
