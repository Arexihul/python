import pandas as pd
import numpy as np

data = {
    "Column1":[1,2,3,4,5],
    "Column2":[10,20,13,20,25],
    "Column3":["abc","bcaa","ade","cb","dea"]
}

df = pd.DataFrame(data)

def kareal(x):
    return x*x

kareal2 = lambda x: x*x

result = df
result = df["Column2"].unique()     # Columnda aynı elemanlar varsa tekrarlamadan yazdırır
result = df["Column2"].nunique()    # Eşsiz elemanların sayısını yazdırır
result = df["Column2"].value_counts()    # Elemanların kaç kez tekrarlandığını yazdırır
result = df["Column1"] * 2      # Her eleman 2 ile çarpılır
result = df["Column1"].apply(kareal)    # Her eleman için kareal fonksiyonu çalıştırılır
result = df["Column1"].apply(kareal2)   # Her eleman için kareal2 fonksiyonu çalıştırılır
result = df["Column1"].apply(lambda x: x*x)
result = df["Column3"].apply(len)   # Elemanların karakter sayısını verir (Her elemanın string olması gerek)
df["Column4"] = df["Column3"].apply(len)

result = df.columns         # Index(['Column1', 'Column2', 'Column3', 'Column4'], dtype='object')
result = len(df.columns)    # 4
result = df.index           # RangeIndex(start=0, stop=5, step=1)
result = len(df.index)      # 5
result = df.info

result = df.sort_values("Column2")      # Artan şekilde sayıları sıralar
result = df.sort_values("Column3")      # Artan şekilde string ifadeleri alfabetik sıralar
result = df.sort_values("Column2",ascending=False)      # Azalan şekilde sayıları sıralar
result = df.sort_values("Column3",ascending=False)      # Azalan şekilde string ifadeleri alfabetik sıralar

# print(df)
# print(result)


data = {
    "Ay": ["Mayıs","Haziran","Nisan","Mayıs","Haziran","Nisan","Mayıs","Haziran","Nisan"],
    "Kategori": ["Elektronik","Elektronik","Elektronik","Kitap","Kitap","Kitap","Giyim","Giyim","Giyim"],
    "Gelir": [20,30,15,14,32,42,12,36,52]
}

df = pd.DataFrame(data)
df = df.pivot_table(index="Ay",columns="Kategori",values="Gelir")

# print(df)
