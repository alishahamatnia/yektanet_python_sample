from baseAdvertising import BaseAdvertising
from advertiser_file import Advertiser


class Ad(BaseAdvertising):

    def __init__(self, title: str, img_url: str, link: str, advertiser: Advertiser):
        super().__init__()
        self._title = title
        self._img_url = img_url
        self._link = link
        self._advertiser = advertiser

    def get_title(self):
        return self._title

    def get_img_url(self):
        return self._img_url

    def get_link(self):
        return self._link

    def get_advertiser(self):
        return self._advertiser

    def set_title(self, title: str):
        self._title = title

    def set_img_url(self, img_url: str):
        self._img_url = img_url

    def set_link(self, link: str):
        self._link = link

    def set_advertiser(self, advertiser: Advertiser):
        self._advertiser = advertiser

    def inc_clicks(self, count=1):
        super().inc_clicks()
        self._advertiser.inc_clicks()

    def inc_views(self, count=1):
        super().inc_views()
        self._advertiser.inc_views()

    def describe_me(self):
        return "this is n object from Ad class. this class designed to model an ad and make it easy to" \
               "manage user activities this object has id: " + str(self.get_id())
