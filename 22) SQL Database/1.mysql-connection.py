# pip install mysql-connector

import mysql.connector

"""
mydb = mysql.connector.connect(
    host = "localhost", # ücretli kullanımda internet tabanlı database kursaydık 192.23.45.56 gibi bir adres alırdık
    user = "root",
    password = "12u8g6v5"
)

# print(mydb)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE mydatabase")      # SQL scripti yazma
mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)
# => ('information_schema',)
#    ('mydatabase',)
#    ('mysql',)
#    ('node-app',)
#    ('performance_schema',)
#    ('sys',)
"""


mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "12u8g6v5",
    database = "mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")    # SQL script ile table oluşturma

