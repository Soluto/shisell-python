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

        return self.__dict__ == other.__dict__

    def union(self, other):
        union = copy.deepcopy(self)

        if isinstance(other, AnalyticsContext):
            union.Scopes.extend(other.Scopes)
            union.ExtraData.update(other.ExtraData)
            union.MetaData.update(other.MetaData)
            union.Filters.extend(other.Filters)
            union.Identities.update(other.Identities)

        return union
