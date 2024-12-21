import pybithumb
import time
import winsound
import os
import pandas as pd
import time
import calendar, requests
from datetime import datetime
import webbrowser
def rsi(name,time):
    now = datetime.now()


    unixtime = calendar.timegm(now.utctimetuple())

    urlcheck = 'https://api.bithumb.com/public/candlestick/'+name+'_KRW/'+time

    res = requests.get(urlcheck)
    data = res.json()

    df = pd.DataFrame(data)

    df['timestamp'] = df['data'].str[0]

    df['open'] = df['data'].str[1].astype(float)

    df['close'] = df['data'].str[2].astype(float)

    df['high'] = df['data'].str[3].astype(float)

    df['low'] = df['data'].str[4].astype(float)

    df['volume'] = df['data'].str[5].astype(float)

    df = df.reset_index()

    df['timestamp'].iloc[-1]

  

    def _rsi(ohlc: pd.DataFrame, period: int = 14):
        ohlc["close"] = ohlc["close"]
        delta = ohlc["close"].diff()

        up, down = delta.copy(), delta.copy()
        up[up < 0] = 0
        down[down > 0] = 0

        _gain = up.ewm(com=(period - 1), min_periods=period).mean()
        _loss = down.abs().ewm(com=(period - 1), min_periods=period).mean()

        RS = _gain / _loss
        return pd.Series(100 - (100 / (1 + RS)), name="RSI")


    r = round(_rsi(df, 14).iloc[-1],1)

    return r


f = open("./key.txt", 'r')
lines = f.readlines()

con_key = lines[0].split('\n')[0]
print(con_key)
sec_key = lines[1]
print(sec_key)
bithumb = pybithumb.Bithumb(con_key, sec_key)

won = 0
class coin:
    def __init__(self,name ,high_price, low_price): # 생성자, 초기자
        self.name = name
        self.high_price = high_price
        self.low_price = low_price 
    


#_coin.append(coin('XEC',0.070,0.064))
#_coin.append(coin('BTC',200000000,100000000))




# for ticker in pybithumb.get_tickers() :
while True:

    try:

        f2 = open("./data.txt", 'r')

        lines = f2.readlines()

        _coin = []

        for line in lines:
            tmp = line.split(' ')
            _coin.append(coin(tmp[0],float(tmp[1]),float(tmp[2])))

    except:
        pass

    for c in _coin:
        ticker = c.name
        price_ticker = round(pybithumb.get_current_price(ticker),4)
        try:
            if price_ticker > c.high_price:
                print('!!! high')
                print(c.name,' ','high_price :',price_ticker)
                winsound.Beep(262, 1000)

            if price_ticker < c.low_price:
                print('!!! low')
                print(c.name,' ','low_price :',price_ticker)
                winsound.Beep(470, 1000)
                if price_ticker < c.low_price * 0.95:
                    print('!!! panic')

        except:
            pass

        try :
            a = rsi(ticker,'10m')
            b = rsi(ticker,'1h')
            c = rsi(ticker,'4h')    
            print(ticker,price_ticker,a,b,c) 
            balance = bithumb.get_balance(ticker)
            if balance[0] > 0 :
                print(ticker, "-", "p", round(balance[0] * pybithumb.get_current_price(ticker),1), "a", round(balance[0],1))
                won = won + balance[0] * pybithumb.get_current_price(ticker)
        except:
            pass
    time.sleep(2)

