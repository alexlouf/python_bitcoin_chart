from statistics import mean
import matplotlib.pyplot as plt
import requests


def print_bitcoin_price(start, end):
    res = requests.get('https://api.coindesk.com/v1/bpi/historical/close.json?start=' + start + '&end=' + end)
    # print(res.json()['bpi'].keys())
    x = list(res.json()['bpi'].keys())
    y = list(res.json()['bpi'].values())
    plt.plot(x, y)
    j = 0
    for i in y:
        if j > 4:
            # print(mean(y[j-5:j]))
            if i < mean(y[j - 5:j]):
                # print("inférieur")
                plt.scatter(x[j], y[j], color="red")
            else:
                # print("supérieur")
                plt.scatter(x[j], y[j], color="green")
            # print(i)
        j += 1
    plt.show()


print_bitcoin_price("2018-03-01", "2018-04-01")
