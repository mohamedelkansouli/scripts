# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 21:51:08 2021

@author: DELL
"""

import pandas as pd
import os
from sklearn.cluster import KMeans
import  numpy as np
from sklearn import preprocessing


PATH='C:\world_intelligence\years'


for root, dirs, files in os.walk(PATH):
    #print (root[28:37])
    
    for fi in files:
        if fi.split(".")[-1] == 'csv':
            print(fi)
            data=pd.read_csv(root+"/"+fi)
            index_c=pd.DataFrame(data['Country Name'],range(len(data)))
            del data['Country Name']
            scaler = preprocessing.StandardScaler().fit(data)
            scaled=scaler.transform(data)
            kmeans = KMeans(n_clusters=10, n_init=1, init='k-means++').fit(scaled)
            pred = kmeans.predict(scaled)
            
            
            pred=pd.DataFrame(np.array(index_c['Country Name']),pred)
            pred.to_csv('C:/world_intelligence/clusters/'+root[28:37]+".csv",mode='a',header=False)



            
            
