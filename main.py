from baseAdvertising import BaseAdvertising
from advertiser_file import Advertiser
from ad import Ad
import UI as ui


def main():
    base_advertising = BaseAdvertising()
    advertiser1 = Advertiser('name1')
    advertiser2 = Advertiser('name2')
    ad1 = Ad('title1', 'img_url1', 'link1', advertiser1)
    ad2 = Ad('title2', 'img_url2', 'link2', advertiser2)

    ui.print_message(base_advertising.describe_me())
    ui.print_message(advertiser1.describe_me())

    ad1.inc_views()
    ad1.inc_views()
    ad1.inc_views()
    ad1.inc_views()
    ad2.inc_views()

    ad1.inc_clicks()
    ad1.inc_clicks()
    ad2.inc_clicks()

    ui.print_message(advertiser2.get_name())
    advertiser2.set_name('new name')
    ui.print_message(advertiser2.get_name())
    ui.print_message(ad1.get_clicks())
    ui.print_message(advertiser2.get_clicks())
    ui.print_message(Advertiser.get_total_clicks())
    ui.print_message(Advertiser.help())


if __name__ == '__main__':
    main()
