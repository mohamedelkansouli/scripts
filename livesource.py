import requests 
from bs4 import BeautifulSoup 
import pandas as pd
from datetime import datetime, timezone, timedelta
import numpy as np 
import time
import matplotlib.pyplot as plt
import random



url ="https://www.livecoinwatch.com/"
print ('ok')
response=requests.get(url ,verify=False ,timeout=10)
print ('ok')
soup=BeautifulSoup(response.text)
print ('ok')

htmltable = soup.find("table", {'class':'lcw-table layout-fixed'})


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


def now_time():
    now = datetime.now(timezone.utc)
    epoch = datetime(1970, 1, 1, tzinfo=timezone.utc) # use POSIX epoch
    posix_timestamp_micros = (now - epoch) // timedelta(microseconds=1)
    return pd.to_datetime((posix_timestamp_micros // 1000), unit='ms') # or `/ 1e3` for float


list_table = tableDataText(htmltable)

data = pd.DataFrame(list_table[1:], columns=list_table[0])

data=data[['Coin','Price']]
data=data.rename(columns={'Price':'Last Price'})
data['date']=now_time()

#data=pd.DataFrame()
names=data['Coin']

dfs = {str(name):data[data['Coin']==name] for name in names}
#dfs = {'data_' + str(name):data[data['Name']==name] for name in names}
result=pd.DataFrame()

print ("before while")
        
while True:
    
    print ('step')
    
    response=requests.get(url,verify=False ,timeout=10)
    soup=BeautifulSoup(response.text)
    htmltable = soup.find("table", {'class':'lcw-table layout-fixed'})

    list_table = tableDataText(htmltable)

    data = pd.DataFrame(list_table[1:], columns=list_table[0])
    data=data[['Coin','Price']]
    data=data.rename(columns={'Price':'Last Price'})
    data['Last Price']=data['Last Price'].str.replace("$","").astype(float)
    data['date']=datetime.now().strftime("%X")
    result=pd.concat([result, data])
    time.sleep(60)
    #result.to_csv('/home/hduser/Documents/kafka/result/result.csv',mode='a',header=False)
    
    for name in data['Coin']:
        plt.plot(result[result['Coin']==name]['date'],result[result['Coin']==name]['Last Price'])
        plt.show()
    