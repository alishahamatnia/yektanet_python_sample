from baseAdvertising import BaseAdvertising
from advertiser import Advertiser
import UI as ui


def main():
    base_advertising = BaseAdvertising()
    advertiser1 = Advertiser('name1')
    advertiser2 = Advertiser('name2')

    ui.print_message(base_advertising.describe_me())
    ui.print_message(advertiser1.describe_me())
    advertiser2.set_name('new name')
    ui.print_message(advertiser2.get_name())
    ui.print_message(advertiser2.get_clicks())
    ui.print_message(Advertiser.get_total_clicks())
    ui.print_message(Advertiser.help())


if __name__ == '__main__':
    main()
