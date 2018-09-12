import copy


class AnalyticsContext:
    def __init__(self):
        self.Scopes = []
        self.ExtraData = {}
        self.MetaData = {}
        self.Filters = []
        self.Identities = {}

    def __eq__(self, other):
        if not isinstance(other, AnalyticsContext):
            return False

        if other is self:
            return True

        return (
                self.Scopes == other.Scopes
                and self.ExtraData == other.ExtraData
                and self.MetaData == other.MetaData
                and self.Filters == other.Filters
                and self.Identities == other.Identities
        )

    def union(self, other):
        union = copy.deepcopy(self)

        if isinstance(other, AnalyticsContext):
            union.Scopes.extend(other.Scopes)
            union.ExtraData.update(other.ExtraData)
            union.MetaData.update(other.MetaData)
            union.Filters.extend(other.Filters)
            union.Identities.update(other.Identities)

        return union
