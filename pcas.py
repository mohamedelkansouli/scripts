import pandas as pd
import os
from sklearn.cluster import KMeans
import  numpy as np
from sklearn import preprocessing


PATH='C:\world_intelligence\years'

result=pd.DataFrame([])
for root, dirs, files in os.walk(PATH):
    #print (root[28:37])
    
    for fi in files:
        if fi.split(".")[-1] == 'csv':

            print(fi)
            data=pd.read_csv(root+"/"+fi)
            index_c=pd.DataFrame(data['Country Name'],range(len(data)))
            del data['Country Name']
            scaler = preprocessing.StandardScaler().fit(data)
            scaled = scaler.transform(data)
            kmeans = KMeans(n_clusters=10, n_init=1, init='k-means++').fit(scaled)
            pred   = kmeans.predict(scaled)
            pred=pd.DataFrame(pred)
            
            pred = pred.rename(columns={0:root[28:37]})
            result = pd.concat([result.reset_index(drop=True), pred], axis=1)
#           result['CountryName']=index_c['Country Name']
#           pred=pd.DataFrame(np.array(index_c['Country Name']),pred)

            
            result.to_csv('C:/world_intelligence/result_clusters.csv',mode='a',header=True)

            
            #pred.to_csv('C:/world_intelligence/clusters/'+root[28:37]+".csv",mode='a',header=False)



from itertools import permutations  

result_code=pd.read_csv('C:/world_intelligence/result_clusters_codes.csv', sep=';')

cols=list(result_code.columns)
cols.remove("CountryCode")

result_pivot=pd.DataFrame([])
for c in cols:
    
  subdata=result_code.pivot(columns=(c), values="CountryCode").reset_index(drop=True)
  cols_2=list(subdata.columns)
  
  for v in cols_2:
      subdata = subdata.rename(columns={v:c+'_'+str(v)})
  
  result_pivot=pd.concat([result_pivot.reset_index(drop=True), subdata], axis=1)

#result_pivot.to_csv('C:/world_intelligence/result_pivot.csv',mode='a',header=True)


from itertools import combinations 


test=result_pivot['data_1960_0']


test=pd.DataFrame(result_pivot['data_1960_0']).dropna()
test=test.dropna()

cols_2=list(result_pivot.columns)

perm=pd.DataFrame([])

for c in cols_2:
    
    print (c)
    combi=list(combinations(pd.DataFrame(result_pivot[c]).dropna()[c], 2))
    combi_a=pd.DataFrame([])
    for n in combi:
         combi_b='-'.join(n)
         combi_a=combi_a.append(pd.Series(combi_b),ignore_index=True) #pd.concat([combi_a, pd.Series(combi_b)]).reset_index(drop=True)
    
    combi_a=combi_a.rename(columns={0:c})
    perm=pd.concat([perm.reset_index(drop=True), combi_a], axis=1)
    #perm=perm.append(combi_a,ignore_index=True)

col_3=list(perm.columns)
col_3.remove('data_1960_0')    
    
for r in perm['data_1960_0'].unique():
    for c in col_3:
        if r=perm['c']

    
    
    
    

    



  
    









