#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
import winsound
import os
import pandas as pd
import time
import calendar, requests
from datetime import datetime
import webbrowser
import sys
from PyQt5 import uic
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
import time
import pybithumb


f = open("D:/key.txt", 'r')
lines = f.readlines()

con_key = lines[0].split('\n')[0]
print(con_key)
sec_key = lines[1]
print(sec_key)
bithumb = pybithumb.Bithumb(con_key, sec_key)

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
        self.timer.timeout.connect(self.setTableWidgetData)
        self.timer.start(1000)
        #self.pushButton.clicked.connect(_print)


    def setTableWidgetData(self):
          ticker = self.comboBox.currentText()
          detail = bithumb.get_market_detail(ticker)
          price_ticker = round(pybithumb.get_current_price(ticker),4)
          balance = bithumb.get_balance(ticker)
          total = round(balance[0] * pybithumb.get_current_price(ticker),1)
          self.price.setText(str(price_ticker))
          self.total.setText(str(total))
          self.rsi_10m.setText(str(rsi(ticker,'10m')))
          self.rsi_30m.setText(str(rsi(ticker,'30m')))
          self.rsi_1h.setText(str(rsi(ticker,'1h')))
          self.rsi_4h.setText(str(rsi(ticker,'4h')))
          self.end_price.setText(str(round(detail[0],4)))
          self.highest.setText(str(round(detail[1],4)))
          self.lowest.setText(str(round(detail[2],4)))
          self.end_price_2.setText(str(round(price_ticker-detail[0],4)))
          self.highest_2.setText(str(round(price_ticker-detail[1],4)))
          self.lowest_2.setText(str(round(price_ticker-detail[2],4)))

    def _buy(self):
        
        buttonReply = QMessageBox.information(
        self, 'Information Title', "Information Message", 
        QMessageBox.Yes| QMessageBox.No, 
        QMessageBox.No
        )

        if buttonReply == QMessageBox.Yes:
            while True :
                try:
                    print('buy')
                    ticker = self.comboBox.currentText()
                    detail = bithumb.get_market_detail(ticker)
                    price_ticker = round(pybithumb.get_current_price(ticker),4)
                    balance = bithumb.get_balance('btc')[2] 
                    bithumb.buy_market_order(ticker,int(balance/price_ticker*0.99))
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
                ticker = self.comboBox.currentText()
                detail = bithumb.get_market_detail(ticker)
                price_ticker = round(pybithumb.get_current_price(ticker),4)
                balance = bithumb.get_balance(ticker)
                total = round(balance[0] * pybithumb.get_current_price(ticker),1)
                print('sell')
                bithumb.sell_market_order(ticker,int(balance[0]))
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




