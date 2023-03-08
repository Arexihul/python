import pandas as pd
import numpy as np

data = np.random.randint(10,100,75).reshape(15,5)
df = pd.DataFrame(data, columns=["Column1","Column2","Column3","Column4","Column5",])

result = df
result = df.columns     # DataFrame içerisindeki column isimlerini getirir
result = df.head()      # İlk 5 kaydı alır
result = df.head(10)    # İlk 10 kaydı alır
result = df.tail()      # Son 5 kaydı alır
result = df.tail(10)    # Son 10 kaydı alır
result = df["Column1"].head()   # Bu ikisi | böyle yazarsan daha anlaşılır olur
result = df.Column1.head()      # aynı şey |
result = df[["Column1","Column2"]].head(7)  
result = df[3:15][["Column1","Column2"]].head(10)  

result = df > 50
result = df[df > 50]
result = df[df %2== 0]
result = df[df %2== 0][df>50]
result = df["Column1"] > 50
result = df[df["Column1"] > 50]
result = df[df["Column1"] > 50][["Column1", "Column2"]]
result = df[(df["Column1"] > 50) & (df["Column1"] <= 70)]
result = df[(df["Column1"] > 50) & (df["Column2"] <= 70)]
result = df[(df["Column1"] > 50) | (df["Column2"] <= 30) | (df["Column3"] > 90)]
result = df.query("Column1 >= 50 & Column1 %2 == 0")
result = df.query("Column1 >= 50 & Column1 %2 == 0")[["Column1", "Column2"]]
result = df.query("Column1 >= 50 | Column1 %2 == 0")[["Column1", "Column2"]]

print(result)

