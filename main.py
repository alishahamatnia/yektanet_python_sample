from baseAdvertising import BaseAdvertising
import UI as ui


def main():
    base_advertising = BaseAdvertising()
    ui.print_message(base_advertising.describe_me())


if __name__ == '__main__':
    main()