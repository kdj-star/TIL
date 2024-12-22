#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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
from PyQt5.QtWidgets import *
import time
import pybithumb

f = open("./key.txt", 'r')
lines = f.readlines()

con_key = lines[0].split('\n')[0]
print(con_key)
sec_key = lines[1]
print(sec_key)
bithumb = pybithumb.Bithumb(con_key, sec_key)

form_class = uic.loadUiType("./241221.ui")[0]
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
        self.timer.timeout.connect(self.setTableWidgetData)
        self.timer.start(1000)
        #self.pushButton.clicked.connect(_print)


    def setTableWidgetData(self):
          ticker = self.comboBox.currentText()
          price_ticker = round(pybithumb.get_current_price(ticker),4)
          balance = bithumb.get_balance(ticker)
          total = round(balance[0] * pybithumb.get_current_price(ticker),1)
          self.lineEdit_6.setText(str(price_ticker))
          self.lineEdit_7.setText(str(total))
          self.lineEdit_2.setText(str(rsi('floki','10m')))
          self.lineEdit_3.setText(str(rsi('floki','30m')))
          self.lineEdit_4.setText(str(rsi('floki','1h')))
          self.lineEdit_5.setText(str(rsi('floki','4h')))
          
        
        



    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
   
    




# In[ ]:





# In[ ]:





# In[ ]:




