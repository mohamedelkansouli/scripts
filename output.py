import pandas as pd

while True:
  try:

    result =pd.read_csv(r"/home/hduser/Documents/kafka/result/result.csv", header='infer')

    result.columns = ['index','Name','Last Price','Date']
    prev =pd.read_csv(r"/home/hduser/Documents/kafka/result/prev.csv" ,names=['Prev','Date','Name'])
    prev=prev.drop_duplicates()

    output=result.merge(prev, how='inner', left_on=["Date","Name"], right_on=["Date","Name"])
    output=output[['Date','Name','Last Price','Prev']]
    output['Last Price_org']=output['Last Price']
    

    

    output['erreur absolue']=(abs(output['Last Price']-output['Prev'])/output['Last Price'])*100
    
    #print (output.dtypes)
    
    output=output.drop_duplicates()

    output.to_csv('/home/hduser/Documents/kafka/result/output.csv',mode='a',header=False)
    #del result 
    #del prev 
    #exit()
    #output.to_csv('/home/hduser/Documents/kafka/result/output.csv',header=True)

  except ValueError:
    print (ValueError)  
