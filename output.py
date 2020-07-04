import pandas as pd

while True:
  try:

    result =pd.read_csv(r"/home/hduser/Documents/kafka/result/result.csv", header='infer')

    prev =pd.read_csv(r"/home/hduser/Documents/kafka/result/prev.csv", header='infer')

    output=result.merge(prev, how='inner', left_on=["date","Name"], right_on=["date","Name"])
    output=output[['date','Name','Last Price','Prev']]





    output.to_csv('/home/hduser/Documents/kafka/result/output.csv',header=True)

    #exit()
    #output.to_csv('/home/hduser/Documents/kafka/result/output.csv',header=True)

  except ValueError:
    print ("Erreur")
