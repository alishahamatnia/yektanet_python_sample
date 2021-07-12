from baseAdvertising import BaseAdvertising


class Advertiser(BaseAdvertising):
    _total_clicks = 0

    def __init__(self, name: str):
        super().__init__()
        self._name = name

    def get_name(self):
        return self._name

    @classmethod
    def get_total_clicks(cls):
        return cls._total_clicks

    def set_name(self, name: str):
        self._name = name

    @staticmethod
    def help():
        return "advertiser class has name, id, views, clicks " \
               "you can interact with an object of this claas by calling its methods"

    def inc_clicks(self, count=1):
        super().inc_clicks()
        type(self)._total_clicks += 1

    def describe_me(self):
        return "this is an object of Advertiser class, you can interact with it by calling its methods"
