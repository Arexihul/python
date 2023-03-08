import pandas as pd

customers = {
    "CostumerID" : [1,2,3,4],
    "FirstName" : ["Ahmet", "Ali", "Hasan", "Canan"],
    "LastName" : ["Yılmaz", "Korkmaz", "Çelik", "Toprak"]
}

orders = {
    "OrderID" : [10,11,12,13],
    "CostumerID" : [1,2,5,7],
    "OrderDate" : ["2010-07-04","2010-08-04","2010-03-06","2010-07-01"]
} 

df_costumers = pd.DataFrame(customers, columns= ["CostumerID","FirstName","LastName"])
df_orders = pd.DataFrame(orders, columns= ["OrderID","CostumerID","OrderDate"])

print(df_costumers)
print(df_orders)

result = pd.merge(df_costumers,df_orders,how="inner")   # Order bilgisi bulunan Costumer'ları getirir.
result = pd.merge(df_costumers,df_orders,how="left")    # Soldakileri(df_costumers) getirir(siparişi olmasa dahi)
result = pd.merge(df_costumers,df_orders,how="right")   # Tam tersi (mantıklı olmasa da örnek amaçlı)
result = pd.merge(df_costumers,df_orders,how="outer")   # Bütün kayıtlar getirilir

print(result)


customersA = {
    "CostumerID" : [1,2,3,4],
    "FirstName" : ["Ahmet", "Ali", "Hasan", "Canan"],
    "LastName" : ["Yılmaz", "Korkmaz", "Çelik", "Toprak"]
}

customersB = {
    "CostumerID" : [4,5,6,7],
    "FirstName" : ["Yağmur", "Çınar", "Cengiz", "Can"],
    "LastName" : ["Bilge", "Turan", "Yılmaz", "Turan"]
}

df_customersA = pd.DataFrame(customersA, columns=["CostumerID","FirstName","LastName"])
df_customersB = pd.DataFrame(customersB, columns=["CostumerID","FirstName","LastName"])

result = pd.concat([df_customersA,df_customersB])   # varsayılan axis=0
# columnlar alt alta birleşir
result = pd.concat([df_customersA,df_customersB],axis=1)
# columnlar yan yana getirilir

# print(result)
