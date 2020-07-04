import pandas as pd
import matplotlib.pyplot as plt

output =pd.read_csv(r"/home/hduser/Documents/kafka/result/output.csv",sep=',', header='infer')
for name in output['Name'].unique():
    for a in output['Last Price']:
     if ',' in a:
      output['Last Price']= [a.replace('.','') for a in output['Last Price']]
      output['Last Price']= [a.replace(',','.') for a in output['Last Price']]

      output['Last Price']=pd.to_numeric(output['Last Price'])


    plt.plot(output['Prev'][output['Name']==name])
    plt.plot(output['Last Price'][output['Name']==name])

    plt.show()
