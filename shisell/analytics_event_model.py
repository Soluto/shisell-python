class AnalyticsEventModel:
    def __init__(self):
        self.Scope = ""
        self.Name = ""
        self.MetaData = {}
        self.ExtraData = {}
        self.Identities = {}

    def __eq__(self, other):
        if not isinstance(other, AnalyticsEventModel):
            return False

        if other is self:
            return True

        return (
                self.Scope == other.Scope
                and self.Name == other.Name
                and self.MetaData == other.MetaData
                and self.ExtraData == other.ExtraData
                and self.Identities == other.Identities
        )
