import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np

pd.set_option('display.max_columns',None)
pd.set_option('display.width',500)

df = pd.read_csv('datasets/persona.csv')
df.head(10)
df.info()
df.shape

# Kaç unique source vardır,frekansları nelerdir ?
df['SOURCE'].nunique()
df['SOURCE'].value_counts()
# Kaç unique price vardır ?
df['PRICE'].nunique()
# Hangi PRICE'dan kaçar tane satış gerçekleştirilmiştir ?
df['PRICE'].value_counts()
# Hangi Ülkeden kaçar tane satış gerçekleştirilmiştir ?
df['COUNTRY'].value_counts()
# Ülkelere göre Satışlardan toplam ne kadar kazanılmış ?
df.groupby('COUNTRY').agg({"PRICE" : "sum"})
# SOURCE türlerine göre satış sayıları nedir ?
df.groupby('SOURCE').agg({"PRICE" : "count"})
# Ülkelere göre PRICE ortalamaları nedir ?
df.groupby("COUNTRY").agg({"PRICE" : "mean"})
# SOURCE'lara göre PRICE ortalamaları nedir ?
df.groupby("SOURCE").agg({"PRICE" : "mean"})
# COUNTRY - SOURCE kırılımında PRICE ortalamaları nedir ?
df.groupby(["COUNTRY","SOURCE"]).agg({"PRICE" : "mean"})

# Görev 2
# COUNTRY, SOURCE, SEX, AGE kırılımında ortalama kazançlar nedir ?
agg_df = df.groupby(["SOURCE", "COUNTRY", "SEX" , "AGE"]).agg({"PRICE" : "mean"})
agg_df.sort_values(by = "PRICE" , ascending= False)
agg_df = agg_df.reset_index()

agg_df.head(20)

bins = [0, 18, 23, 30, 40, agg_df['AGE'].max()]
labels = ["0-18","19-23","24-30","31-40", "41-" + str(df["AGE"].max())]
agg_df["AGE_CAT"] = pd.cut(df["AGE"] , bins = bins, labels = labels)

for row in agg_df.values:
    print(row)

agg_df["customers_level_based"] = [row[0].upper() + "_" + row[1].upper() + "_" +  row[2].upper() + "_" + row[5].upper() for row in agg_df.values ]
agg_df = agg_df[["customers_level_based", "PRICE"]]
agg_df.groupby("customers_level_based").agg({"PRICE": "mean"})
agg_df["SEGMENT"] = pd.qcut(agg_df["PRICE"] , 4 , labels = ["D", "C", "B", "A"])
agg_df.groupby("SEGMENT").agg({"PRICE" : ["mean","sum","max"]})
agg_df = agg_df.groupby(["customers_level_based"]).agg({"PRICE": "mean"})
agg_df.value_counts()


new_user = "ANDROID_TUR_FEMALE_31-40"
new_user = "IOS_FRA_FEMALE_31-40"
agg_df[agg_df["customers_level_based"] == new_user]
agg_df = agg_df.reset_index()
agg_df
agg_df.value_counts()

