import pandas as pd

"""
df = pd.DataFrame()
df = pd.DataFrame([1,2,3,4])

print(df)
"""
"""
s1 = pd.Series([3,2,0,1])
s2 = pd.Series([0,3,7,2])

data = dict(apples = s1, oranges = s2)

df = pd.DataFrame(data)

print(df)
"""

liste = [["Ahmet",50],["Ali",80],["Yağmur",65],["Çınar",70]]
dicti = {"Name":["Ahmet","Ali","Yağmur","Çınar"], "Grade":[50,80,65,70]}
dict_list = [{"Name":"Ahmet","Grade":"50"},
             {"Name":"Ali","Grade":"80"},   
             {"Name":"Yağmur","Grade":"65"},   
             {"Name":"Çınar","Grade":"70"},   
            ]

df = pd.DataFrame(liste, columns = ["Name","Grade"], index = [1,2,3,4], dtype = float)
df = pd.DataFrame(dicti, index=[1,2,3,4], dtype=float)
df = pd.DataFrame(dict_list, index = ["No: 242","No: 417","No: 185","No: 303"])

print(df)

