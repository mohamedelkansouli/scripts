import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime, timezone, timedelta
import numpy as np
import time
import matplotlib.pyplot as plt
import random

import xgboost as xgb
from sklearn.metrics import mean_squared_error
from sklearn import preprocessing


url ="https://finance.yahoo.com/currencies"
print ('ok')
response=requests.get(url ,verify=False ,timeout=10)
print ('ok')
soup=BeautifulSoup(response.text)
print ('ok')

htmltable = soup.find("table", {'class':'yfinlist-table W(100%) BdB Bdc($tableBorderGray)'})


result=pd.DataFrame()
def tableDataText(table):
    rows = []
    trs = table.find_all('tr')
    headerow = [td.get_text(strip=True) for td in trs[0].find_all('th')] # header row
    if headerow: # if there is a header row include first
        rows.append(headerow)
        trs = trs[1:]
    for tr in trs: # for every table row
        rows.append([td.get_text(strip=True) for td in tr.find_all('td')]) # data row
    return rows


                       
