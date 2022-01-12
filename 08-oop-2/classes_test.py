class ApiCall:
    def who(self):
        return 'ApiCall'

    def run(self):
        return [1, 2, 3]


class CanCountMixin:
    def who(self):
        return 'CanCountMixin'

    def count(self):
        return 5


class ApplesCall(CanCountMixin, ApiCall):
    pass


class OrangesCall(CanCountMixin, ApiCall):
    pass


class MilkCall(ApiCall):
    pass


a = ApplesCall()
print(a.count())
print(a.run())
print(a.who())

ApplesCall.mro()