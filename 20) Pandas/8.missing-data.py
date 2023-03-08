import pandas as pd
import numpy as np

data = np.random.randint(10,100,15).reshape(5,3)

df = pd.DataFrame(data, index=["a","c","e","f","h"], columns=["column1", "column2", "column3"])

df = df.reindex(["a","b","c","d","e","f","g","h"])

newColumn = [np.nan,30,np.nan,51,np.nan,30,np.nan,10]
df["column4"] = newColumn

result = df
result = df.drop("column1",axis=1)
result = df.drop(["column1","column2"],axis=1)
result = df.drop("a",axis=0)
result = df.drop(["b","d","g"],axis=0)

result = df.isnull()    # NaN olanlar True
result = df.notnull()   # NaN olmayanlar True
result = df.isnull().sum()      # nullları sayar
result = df["column1"].isnull().sum()    # column1'deki null sayısını verir
result = df[df["column1"].isnull()]      # column1'in null olduğu satırları verir
result = df[df["column1"].isnull()]["column1"]
result = df[df["column1"].notnull()]["column1"]

result = df.dropna()    # varsayılan axis=0 => NaN olan satırları siler
result = df.dropna(axis=1)  # axis=1 => NaN olan sütunları siler
result = df.dropna(how="any")   # NaN olan satırları siler - varsayılan
result = df.dropna(how="all")   # Tüm satır NaN ise silinir
result = df.dropna(subset=["column1","column2"])    # column1 ve/veya column2'de NaN varsa satırı siler
result = df.dropna(subset=["column1","column2"],how="all")    # column1 ve column2'de NaN varsa satırı siler
result = df.dropna(thresh=2)    # En az 2 veri olanları silmez
result = df.dropna(thresh=1)    # En az 1 veri olanları silmez

result = df.fillna(value="no input")    # Nan verileri value ile doldurur
result = df.fillna(value=1)

result = df.sum().sum()
result = df.size
result = df.isnull().sum().sum()    # tüm nullların sayısı

def ortalama(df):
    toplam = df.sum().sum()
    adet = df.size - df.isnull().sum().sum()
    return toplam/adet

result = df.fillna(value=int(ortalama(df)))

print(result)
