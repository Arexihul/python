import pandas as pd
import numpy as np

# data
numbers = [20,30,40,50]     # int64
letters = ["a","b","c","d"] # object
letters = ["a","b","c",20]  # object
dictionary = {"a":10,"b":20,"c":30,"d":40}
random_numbers = np.random.randint(10,100,6)

# pandas_series = pd.Series()
pandas_series = pd.Series(numbers)
pandas_series = pd.Series(letters)
pandas_series = pd.Series(5)
pandas_series = pd.Series(5, [0,1,2,3])
pandas_series = pd.Series(numbers, ["a","b","c","d"])
pandas_series = pd.Series(dictionary)
pandas_series = pd.Series(random_numbers, [1,2,3,4,5,6])

pandas_series = pd.Series([100,201,300,400], ["a","b","c","d"])

result = pandas_series[0]
result = pandas_series[-1]
result = pandas_series[:2]
result = pandas_series[-2:]
result = pandas_series["a"]
result = pandas_series["d"]
result = pandas_series[:"c"]
result = pandas_series["b":]
result = pandas_series["b":"c"]
result = pandas_series[["a","c"]]

result = pandas_series.ndim     # 1 boyutlu
result = pandas_series.dtype
result = pandas_series.shape
result = pandas_series.sum()    # Toplam
result = pandas_series.max()
result = pandas_series.min()
result = pandas_series + pandas_series
result = pandas_series + 50
result = np.sqrt(pandas_series) # karekök
result = pandas_series >= 300
result = pandas_series %2 == 0 
# print(pandas_series[result])    # çift olan sayıları yazdırır

# print(pandas_series)
# print(result)


opel2018 = pd.Series([20,30,40,10],["astra","corsa","mokka","insignia"])
opel2019 = pd.Series([40,30,20,10],["astra","corsa","grandland","insignia"])

total = opel2018 + opel2019

print(total)
print(total["astra"])


