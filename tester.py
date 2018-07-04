import settings as settings
import time

pair = settings.n
buy = settings.nb
sell = settings.ns
trading_fees = settings.na
data = []


def loop():
    a = settings.fcoin.get_market_ticker(pair)['data']['ticker'][2]
    b = settings.fcoin.get_market_ticker(pair)['data']['ticker'][4]
    print(a)
    print(b)
    print(b - a)

    print("Purchase amount {}".format(((sell * b) - (buy * a))))
    print("Cost of doing business {}".format((((sell * b) + (buy * a)) * trading_fees)))
    print('Profit is {}'.format(((sell * b) - (buy * a)) - (((sell * b) + (buy * a)) * trading_fees)))
    print(((sell * b) - (buy * a)) > (((sell * b) + (buy * a)) * trading_fees))

    while (sell * b - buy * a) > (((sell * b) + (buy * a)) * trading_fees):
        a = settings.fcoin.get_market_ticker(pair)['data']['ticker'][2]
        b = settings.fcoin.get_market_ticker(pair)['data']['ticker'][4]
        data.append((((sell * b) - (buy * a)) - (((sell * b) + (buy * a)) * trading_fees)))
        print(a)
        print(b)
        print(b - a)

        print("Purchase amount {}".format(((sell * b) - (buy * a))))
        print("Cost of doing business {}".format((((sell * b) + (buy * a)) * trading_fees)))
        print('Profit is {}'.format(((sell * b) - (buy * a)) - (((sell * b) + (buy * a)) * trading_fees)))
        print(((sell * b) - (buy * a)) > (((sell * b) + (buy * a)) * trading_fees))

        if ((sell * b - buy * a) > (((sell * b) + (buy * a)) * trading_fees)) is False:
            break

    print('We should have had {} potential trades'.format(len(data) * 2))
    print(data)


def restart():
    while True:
        try:

            loop()

        except Exception as e:
            print(e)
            time.sleep(0.1)

        time.sleep(0.2)

        print(' ')
        print('*********************************************')
        print('+++++++++++++++++++++++++++++++++++++++++++++')
        print(' ')


if __name__ == '__main__':
    restart()
