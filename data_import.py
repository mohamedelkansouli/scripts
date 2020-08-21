import requests 
from bs4 import BeautifulSoup 
import pandas as pd
from datetime import datetime, timezone, timedelta
import numpy as np 
import time
import matplotlib.pyplot as plt
import random



url ="https://finance.yahoo.com/cryptocurrencies"
print ('ok')
response=requests.get(url ,verify=False ,timeout=10)
print ('ok')
soup=BeautifulSoup(response.text)
print ('ok')

htmltable = soup.find("table", {'class':'W(100%)'})


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
print (data)
data=data[['Name','Price (Intraday)','Change','% Change']]
data=data.rename(columns={'Price (Intraday)':'Last Price'})
data['date']=now_time()

#data=pd.DataFrame()
names=data['Name']

dfs = {str(name):data[data['Name']==name] for name in names}
#dfs = {'data_' + str(name):data[data['Name']==name] for name in names}
result=pd.DataFrame()

print ("before while")
        
while True:
    
    print ('step')
    #time.sleep(5)
    response=requests.get(url,verify=False ,timeout=10)
    soup=BeautifulSoup(response.text)
    htmltable = soup.find("table", {'class':'W(100%)'})

    list_table = tableDataText(htmltable)

    data = pd.DataFrame(list_table[1:], columns=list_table[0])
    data=data[['Name','Price (Intraday)']]
    data=data.rename(columns={'Price (Intraday)':'Last Price'})
    data['Last Price']=data['Last Price'].str.replace(",","").astype(float)
    data['date']=datetime.now().strftime("%X")
    result=pd.concat([result, data])
    print (result)
    result.to_csv('/home/hduser/Documents/kafka/result/result.csv',mode='a',header=False)
    
    #for name in data['Name']:
    #    plt.plot(result[result['Name']==name]['date'],result[result['Name']==name]['Last Price'])
    #    plt.show()
    
