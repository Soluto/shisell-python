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

        return self.__dict__ == other.__dict__
