from pyspark.sql import SparkSession
from pyspark.context import SparkContext
import logging

import colored_traceback
colored_traceback.add_hook(always=True)


sparkSession = SparkSession.builder.appName("example-pyspark-read-and-write").getOrCreate()


#sc = SparkConf().setAppName("Read Text File in Spark").setMaster("local[*]")
#sqlContext = SQLContext(sc)
#df = spark.read.format("com.databricks.spark.csv").load("path_to/data.csv")
df_csv = sparkSession.read.format("csv").csv("hdfs://localhost:9000/countries/*.csv")

df = df_csv.withColumnRenamed("_c0","Country Name") \
.withColumnRenamed("_c1","Country Code") \
.withColumnRenamed("_c2","Indicator Name") \
.withColumnRenamed("_c3","Indicator Code") \
.withColumnRenamed("_c4","1960") \
.withColumnRenamed("_c5","1961") \
.withColumnRenamed("_c6","1962") \
.withColumnRenamed("_c7","1963") \
.withColumnRenamed("_c8","1964") \
.withColumnRenamed("_c9","1965") \
.withColumnRenamed("_c10","1966") \
.withColumnRenamed("_c11","1967") \
.withColumnRenamed("_c12","1968") \
.withColumnRenamed("_c13","1969") \
.withColumnRenamed("_c14","1970") \
.withColumnRenamed("_c15","1971") \
.withColumnRenamed("_c16","1972") \
.withColumnRenamed("_c17","1973") \
.withColumnRenamed("_c18","1974") \
.withColumnRenamed("_c19","1975") \
.withColumnRenamed("_c20","1976") \
.withColumnRenamed("_c21","1977") \
.withColumnRenamed("_c22","1978") \
.withColumnRenamed("_c23","1979") \
.withColumnRenamed("_c24","1980") \
.withColumnRenamed("_c25","1981") \
.withColumnRenamed("_c26","1982") \
.withColumnRenamed("_c27","1983") \
.withColumnRenamed("_c28","1984") \
.withColumnRenamed("_c29","1985") \
.withColumnRenamed("_c30","1986") \
.withColumnRenamed("_c31","1987") \
.withColumnRenamed("_c32","1988") \
.withColumnRenamed("_c33","1989") \
.withColumnRenamed("_c34","1990") \
.withColumnRenamed("_c35","1991") \
.withColumnRenamed("_c36","1992") \
.withColumnRenamed("_c37","1993") \
.withColumnRenamed("_c38","1994") \
.withColumnRenamed("_c39","1995") \
.withColumnRenamed("_c40","1996") \
.withColumnRenamed("_c41","1997") \
.withColumnRenamed("_c42","1998") \
.withColumnRenamed("_c43","1999") \
.withColumnRenamed("_c44","2000") \
.withColumnRenamed("_c45","2001") \
.withColumnRenamed("_c46","2002") \
.withColumnRenamed("_c47","2003") \
.withColumnRenamed("_c48","2004") \
.withColumnRenamed("_c49","2005") \
.withColumnRenamed("_c50","2006") \
.withColumnRenamed("_c51","2007") \
.withColumnRenamed("_c52","2008") \
.withColumnRenamed("_c53","2009") \
.withColumnRenamed("_c54","2010") \
.withColumnRenamed("_c55","2011") \
.withColumnRenamed("_c56","2012") \
.withColumnRenamed("_c57","2013") \
.withColumnRenamed("_c58","2014") \
.withColumnRenamed("_c59","2015") \
.withColumnRenamed("_c60","2016") \
.withColumnRenamed("_c61","2017") \
.withColumnRenamed("_c62","2018") \
.withColumnRenamed("_c63","2019") \
.withColumnRenamed("_c64","2020")
df=df.drop("_c65")
#df.show(200)

liste=["1960","1965","1970","1975","1980","1985","1990","1995","2000","2005","2010","2015","2019","2020"]

for y in liste:
      print(y)
      data = df.select(df["Country Name"],df["Indicator Code"],y)
      data=data.withColumnRenamed(y,"Annee")
      data = data.select(data["Indicator Code"],
        data("Country Name"),
        data("Annee").cast("float"))

      data=data.filter(data("Indicator Code")
        .isin ("SP.POP.TOTL",
        "SP.POP.GROW",
        "IT.NET.SECR.P6",
        "IT.NET.SECR",
        "SP.URB.TOTL.IN.ZS",
        "SP.URB.TOTL",
        "SP.URB.GROW",
        "SM.POP.TOTL.ZS",
        "SM.POP.TOTL",
        "SH.H2O.BASW.ZS",
        "EG.ELC.ACCS.ZS",
        "EG.ELC.ACCS.RU.ZS",
        "IT.CEL.SETS.P2",
        "IT.CEL.SETS",
        "EN.POP.DNST",
        "AG.SRF.TOTL.K2",
        "AG.LND.TOTL.K2",
        "SH.STA.BASS.ZS",
        "IT.MLT.MAIN.P2",
        "IT.MLT.MAIN",
        #"ER.LND.PTLD.ZS",
        "EG.ELC.ACCS.UR.ZS",
        "SE.SEC.ENRL.GC",
        "SE.SEC.ENRL",
        "SE.PRM.ENRL",
        "PA.NUS.ATLS",
        "NY.GDP.PCAP.CN",
        "NY.GDP.PCAP.CD",
        "NY.GDP.MKTP.CN",
        "NY.GDP.MKTP.CD",
        #"ER.PTD.TOTL.ZS",
        "ER.FSH.PROD.MT",
        #"ER.FSH.CAPT.MT",
        #"EN.BIR.THRD.NO",
        "SL.TLF.CACT.NE.ZS",
        "SE.SEC.ENRL.GC.FE.ZS",
        "SE.PRM.ENRL.FE.ZS",
        "SE.PRM.DURS",
        "SE.PRM.AGES",
        "NY.GDP.PCAP.KN",
        "NY.GDP.PCAP.KD.ZG",
        "NY.GDP.MKTP.KN",
        "NY.GDP.MKTP.KD.ZG",
        "NY.GDP.DEFL.ZS",
        "NY.GDP.DEFL.KD.ZG.AD",
        "NY.GDP.DEFL.KD.ZG",
        #"EN.FSH.THRD.NO",
        "SP.DYN.CDRT.IN",
        "SP.DYN.CBRT.IN",
        "SH.TBS.INCD") )

      pivotDF = data.groupBy("Country Name").pivot("Indicator Code").min("Annee")
      pivotDF=pivotDF.na.fill(0).persist()
      pivotDF.show(10)
     
     
    

logging.addLevelName( logging.INFO, "3[1;31m%s3[1;0m" % logging.getLevelName(logging.WARNING))
logging.addLevelName( logging.WARNING, "3[1;41m%s3[1;0m" % logging.getLevelName(logging.ERROR))

