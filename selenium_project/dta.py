import pandas as pd
import requests

action = dict({})

def get_data( inits ): #pass in initials of the stock
    for initials in inits:
        url = "http://nepalstockinfo.com/iframe_page.php?symbol={}&action=price_history".format(initials)
        data = requests.get(url).json()

        df = pd.DataFrame.from_dict(data) 

        ticker = df['close_price']
        ticker = ticker.apply(pd.to_numeric)

        exp1 = ticker.ewm(span=12, adjust=False).mean()
        exp2 = ticker.ewm(span=26, adjust=False).mean()
        macd = exp1 - exp2


        exp1 = ticker.ewm(span=12, adjust=False).mean()
        exp2 = ticker.ewm(span=26, adjust=False).mean()
        macd = exp1 - exp2

        signal = macd.ewm(span=9, adjust=False).mean()

        macd = macd.iloc[-1]
        signal = signal.iloc[-1]

        if macd>signal:
            action[initials] = "Buy"
        else:
            action[initials] = "Sell"

        

    return action

dta = ['NABIL','UMHL']
print(get_data(dta))