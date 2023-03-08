import mysql.connector
import datetime
from school.connection import connection

mycursor = connection.cursor()

class Student:
    connection = connection
    mycursor = connection.cursor()

    def __init__(self,studentNumber,name,surname,birthDate,gender):
        if id is None:
            self.id = 0
        else:
            self.id = id
        self.studentNumber = studentNumber
        self.name = name
        self.surname = surname
        self.birthDate = birthDate
        self.gender = gender

    def saveStudent(self):
        sql = "INSERT INTO students (StudentNumber,Name,Surname,Birthdate,Gender) values (%s,%s,%s,%s,%s)"
        value = (self.studentNumber,self.name,self.surname,self.birthDate,self.gender)

        Student.mycursor.execute(sql,value)

        try:
            Student.connection.commit()
            print("Student added.")
        except mysql.connector.Error as err:
            print("Error: ", err)
        finally:
            Student.connection.close()
            print("Connection has ended.")

    @staticmethod
    def saveStudents(liste):
        sql = "INSERT INTO students (StudentNumber,Name,Surname,Birthdate,Gender) values (%s,%s,%s,%s,%s)"
        values = liste

        Student.mycursor.executemany(sql,values)

        try:
            Student.connection.commit()
            print(f"{Student.mycursor.rowcount} students added.")
        except mysql.connector.Error as err:
            print("Error: ", err)
        finally:
            Student.connection.close()
            print("Connection has ended.")



# ahmet = Student("124","Ahmet","Yılmaz",datetime.datetime(2005, 5, 17),"E")
# ahmet.saveStudent()

ogrenciler = [
    ("201","Ahmet","Yılmaz",datetime.datetime(2005, 5, 17),"E"),
    ("202","Ali","Can",datetime.datetime(2005, 6, 17),"E"),
    ("203","Canan","Tan",datetime.datetime(2005, 7, 7),"K"),
    ("204","Ayşe","Taner",datetime.datetime(2005, 9, 23),"K"),
    ("205","Bahadır","Toksöz",datetime.datetime(2004, 7, 27),"E"),
    ("206","Ali","Cenk",datetime.datetime(2003, 8, 25),"E")
]

Student.saveStudents(ogrenciler)
