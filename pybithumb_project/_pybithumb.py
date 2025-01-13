#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time
import winsound
import os
import pandas as pd
import calendar, requests
from datetime import datetime
import webbrowser
import sys
from PyQt5 import uic
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
import pybithumb
import ccxt
import jwt 
import uuid
f = open("D:/_key.txt", 'r')
lines = f.readlines()

accessKey = lines[0].split('\n')[0]
print(len(accessKey))
secretKey = lines[1].split('\n')[0]
print(len(secretKey))

apiUrl = 'https://api.bithumb.com'


def currency_info(name):
    _name=name.upper()
    url = "https://api.bithumb.com/v1/ticker?markets=KRW-"+_name
    
    headers = {"accept": "application/json"}
    
    response = requests.get(url, headers=headers)
    
    return response.json()[0]



def get_info(name):

    
    # Generate access token
    payload = {
        'access_key': accessKey,
        'nonce': str(uuid.uuid4()),
        'timestamp': round(time.time() * 1000)
    }
    jwt_token = jwt.encode(payload, secretKey)
    authorization_token = 'Bearer {}'.format(jwt_token)
    headers = {
      'Authorization': authorization_token
    }
    
    try:
        # Call API
        response = requests.get(apiUrl + '/v1/accounts', headers=headers)
        # handle to success or fail
        tmp = response.json()
    
        for t in tmp:
            if name == t['currency']:
                return t
        
    except Exception as err:
        # handle exception
        return 'none'


form_class = uic.loadUiType("D:/241221.ui")[0]


def rsi(name,time):
    now = datetime.now()


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

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.timer = QtCore.QTimer()
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.buy.clicked.connect(self._buy)
        self.sell.clicked.connect(self._sell)
        self.timer.timeout.connect(self.setWidgetData)
        self.timer.start(1000)
        #self.pushButton.clicked.connect(_print)


    def setWidgetData(self):
        
          ticker = self.comboBox.currentText()
          price_ticker = currency_info(ticker)['trade_price']
          balance = ""
          avg_buy_price =""
          try:
              avg_buy_price = get_info(ticker.upper())['avg_buy_price']
          except:
              avg_buy_price ="none"
          try:
              balance = float(get_info(ticker.upper())['balance'])
          except:
              balance = 0      
          try:
              gap =  round(price_ticker - float(avg_buy_price),2)
          except:
              gap =0

          total = round(balance * price_ticker,1)

          gap_percent = ''
          tmp = 0
        
          if avg_buy_price != 'none':
            tmp = float(price_ticker) - float(avg_buy_price)
            tmp = round(tmp / float(avg_buy_price)*100,2)
            gap_percent = str(tmp) + '%'
        
          try:
              self.gap_price.setText(str(round(float(price_ticker) - float(avg_buy_price),4)))
          except:
              pass
          self.gap_percent.setText(gap_percent)
          if tmp < 0 :
            self.gap_price.setStyleSheet("Color : blue")
            self.gap_percent.setStyleSheet("Color : blue")
          elif tmp == 0:
            self.gap_price.setStyleSheet("Color : black")
            self.gap_percent.setStyleSheet("Color : black")
          else :
            self.gap_price.setStyleSheet("Color : red")
            self.gap_percent.setStyleSheet("Color : red")
              
          self.avg_price.setText(avg_buy_price)
          self.price.setText(str(round(price_ticker,5)))
          if avg_buy_price != 'none':
              if price_ticker < float(avg_buy_price):
                   self.price.setStyleSheet("Color : blue")
              elif price_ticker == float(avg_buy_price):
                   self.price.setStyleSheet("Color : black")
              else :
                   self.price.setStyleSheet("Color : red")
                  
          self.total.setText(str(total))
          self.rsi_10m.setText(str(rsi(ticker,'10m')))
          self.rsi_30m.setText(str(rsi(ticker,'30m')))
          self.rsi_1h.setText(str(rsi(ticker,'1h')))
          self.rsi_4h.setText(str(rsi(ticker,'4h')))
          self.end_price.setText(str(round(currency_info(ticker)['opening_price'],4)))
          self.highest.setText(str(round(currency_info(ticker)['high_price'],4)))
          self.lowest.setText(str(round(currency_info(ticker)['low_price'],4)))
          self.end_price_2.setText(str(round(price_ticker-currency_info(ticker)['opening_price'],4)))
          if price_ticker < float(round(currency_info(ticker)['opening_price'],4)):
               self.end_price_2.setStyleSheet("Color : blue")
          elif price_ticker == float(round(currency_info(ticker)['opening_price'],4)):
               self.end_price_2.setStyleSheet("Color : black")
          else :
               self.end_price_2.setStyleSheet("Color : red")
          self.highest_2.setText(str(round(price_ticker-currency_info(ticker)['high_price'],4)))
          if price_ticker < float(round(currency_info(ticker)['high_price'],4)):
               self.highest_2.setStyleSheet("Color : blue")
          elif price_ticker == float(round(currency_info(ticker)['high_price'],4)):
               self.highest_2.setStyleSheet("Color : black")
          else :
               self.highest_2.setStyleSheet("Color : red")
          
          self.lowest_2.setText(str(round(price_ticker-currency_info(ticker)['low_price'],4)))
          if price_ticker < float(round(currency_info(ticker)['low_price'],4)):
               self.lowest_2.setStyleSheet("Color : blue")
          elif price_ticker == float(round(currency_info(ticker)['low_price'],4)):
               self.lowest_2.setStyleSheet("Color : black")
          else :
               self.lowest_2.setStyleSheet("Color : red")
          

    
    def _buy(self):
        
        buttonReply = QMessageBox.information(
        self, 'Information Title', "Information Message", 
        QMessageBox.Yes| QMessageBox.No, 
        QMessageBox.No
        )

        if buttonReply == QMessageBox.Yes:
            while True :
                try:
                    break
                except:
                    pass
        else:
            print('No clicked.')
            
        
       
    
    def _sell(self):
     buttonReply = QMessageBox.information(
        self, 'Information Title', "Information Message", 
        QMessageBox.Yes| QMessageBox.No, 
        QMessageBox.No
        )
        
        
     if buttonReply == QMessageBox.Yes:
        while True :
            try:
                break
            except:
                pass
     else:
        print('No clicked.')
            


     
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
   
    




# In[ ]:



 



# In[ ]:





# In[ ]:




