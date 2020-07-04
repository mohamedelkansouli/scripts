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

import re
from numpy import mean
def now_time():
    now = datetime.now(timezone.utc)
    epoch = datetime(1970, 1, 1, tzinfo=timezone.utc) # use POSIX epoch
    posix_timestamp_micros = (now - epoch) // timedelta(microseconds=1)
    return (posix_timestamp_micros // 1000) # or `/ 1e3` for float

prev=pd.DataFrame()
result =pd.read_csv(r"/home/hduser/Documents/kafka/result/result.csv", header='infer')

while True:
 #time.sleep(5)
 for name in result['Name'].unique():
     # split into input (X) and output (y) variables
        #X, y = result.iloc[:,:-1],result.iloc[:,-1]
        result=result.drop(result[result['Last Price']=='-'].index)
        #result=result.drop(result[result['Name']=='MXN=X'].index)

        X = pd.DataFrame(result.iloc[:,-1][result['Name']==name])

        y = pd.DataFrame(result.iloc[:,1:3][result['Name']==name])
        #y_train = pd.DataFrame(encoder.fit_transform(y),columns=['Last Price'])
        #X_train = pd.DataFrame(encoder.fit_transform(X),columns=['date'])
                
