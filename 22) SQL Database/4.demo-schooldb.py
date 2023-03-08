# 1- Workbench IDE ile schooldb isminde bir database oluşturup Student tablosunu ekleyiniz.
    # Id,StudentNumber,Name,Surname,Birthdate,Gender

# 2- Database bağlantısını oluşturunuz. (connection.py)

# 3- Aşağıdaki bilgiler için insert sorguları oluşturup kayıtları ekleyiniz.

    # ("301","Ahmet","Yılmaz",datetime(2005, 5, 17),"E"),
    # ("302","Ali","Can",datetime(2005, 6, 17),"E"),
    # ("303","Canan","Tan",datetime(2005, 7, 7),"K"),
    # ("304","Ayşe","Taner",datetime(2005, 9, 23),"K"),
    # ("305","Bahadır","Toksöz",datetime(2004, 7, 27),"E"),
    # ("306","Ali","Cenk",datetime(2003, 8, 25),"E")


import mysql.connector
import datetime

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12u8g6v5",
    database="schooldb"
)

mycursor = connection.cursor()

sql = "insert into students(StudentNumber,Name,Surname,Birthdate,Gender) values (%s,%s,%s,%s,%s)"
ogrenciler = [
    ("101","Ahmet","Yılmaz",datetime.datetime(2005, 5, 17),"E"),
    ("102","Ali","Can",datetime.datetime(2005, 6, 17),"E"),
    ("103","Canan","Tan",datetime.datetime(2005, 7, 7),"K"),
    ("104","Ayşe","Taner",datetime.datetime(2005, 9, 23),"K"),
    ("105","Bahadır","Toksöz",datetime.datetime(2004, 7, 27),"E"),
    ("106","Ali","Cenk",datetime.datetime(2003, 8, 25),"E")
]

mycursor.executemany(sql,ogrenciler)

try:
    connection.commit()
    print(f"{mycursor.rowcount} students' informations has saved")
except mysql.connector.Error as err:
    print("Hata: ", err)
finally:
    connection.close()





