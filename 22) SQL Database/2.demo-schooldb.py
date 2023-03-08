# 1- Workbench IDE ile schooldb isminde bir database oluşturup Student tablosunu ekleyiniz.
# Columns => Id, StudentNumber, Name, Surname, Birthdate, Gender

# 2- Database bağlantısını oluşturunuz.

import mysql.connector

mydb = mysql.connector.connect(
    user = "root",
    host = "localhost",
    password = "12u8g6v5",
    database = "schooldb"
)

mycursor = mydb.cursor()

mycursor.execute("Show Databases")

for i in mycursor:
    print(i)
