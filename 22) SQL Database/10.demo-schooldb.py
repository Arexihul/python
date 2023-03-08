
# 1- Tüm öğrenci kayıtlarını alınız
# 2- Tüm öğrencilerin sadece öğrenci no, ad ve soyad bilgilerini alınız
# 3- Sadece kız öğrencilerin ad ve soyad bilgilerini alınız
# 4- 2003 doğumlu olan öğrenci bilgilerini alınız
# 5- İsmi Ali ve doğum tarihi 2005 olan öğrenci bilgilerini alınız
# 6- Ad ve soyadı içerisinde 'an' ifadesi geçen kayıtları alınız
# 7- Kaç erkek öğrenci vardır
# 8- Kız öğrencileri harf sırasına göre getiriniz

import mysql.connector
import datetime
from school.connection import connection

mycursor = connection.cursor()

class Student:
    connection = connection
    mycursor = connection.cursor()

    def __init__(self,id,studentNumber,name,surname,birthDate,gender):
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
            print("Hata: ", err)
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
            print("Hata: ", err)
        finally:
            Student.connection.close()
            print("Connection has ended.")

    @staticmethod
    def StudentInfo():
        sql = "select * from students"
        sql = "select StudentNumber,name,surname from students"
        sql = "select StudentNumber,name,surname from students where gender='K'"
        sql = "select * from students where YEAR(birthdate) = 2003"
        sql = "select * from students where YEAR(birthdate) = 2005 and name='ali'"
        sql = "select * from students where name like '%an%'"   # %an -> an ile biten, an% -> an ile başlayan, %an% -> içinde an geçen
        sql = "select COUNT(*) from students where gender='E'"
        sql = "select StudentNumber,name,surname from students where gender='K' order by name,surname"


        Student.mycursor.execute(sql)

        try:
            results = Student.mycursor.fetchall()

            for result in results:
                print(result)
        
        except mysql.connector.Error as err:
            print('hata', err)
        finally:
            Student.connection.close() 

    @staticmethod
    def getStudentById(id):
        sql = "select * from students where id=%s"
        value = (id,)

        Student.mycursor.execute(sql,value)

        try:
            obj = Student.mycursor.fetchone()
            return Student(obj[0],obj[1],obj[2],obj[3],obj[4],obj[5])
        except mysql.connector.Error as err:
            print('Error', err)

    def updateStudent(self):
        sql = "update students set studentnumber=%s,name=%s,surname=%s,birthdate=%s,gender=%s where id=%s"
        values = (self.studentNumber,self.name,self.surname,self.birthDate,self.gender,self.id)
        Student.mycursor.execute(sql,values)

        try:
            Student.connection.commit()
            print(f'{Student.mycursor.rowcount} tane kayıt güncellendi')
        except mysql.connector.Error as err:
            print('Hata:',err)

    @staticmethod
    def updateStudents(liste):
        sql = "update students set studentnumber=%s,name=%s,surname=%s,birthdate=%s,gender=%s where id=%s"
        values = []
        order = [1,2,3,4,5,0]

        for item in liste:
            item = [item[i] for i in order]
            values.append(item)

        Student.mycursor.executemany(sql,values)

        try:
            Student.connection.commit()
            print(f'{Student.mycursor.rowcount} tane kayıt güncellendi')
        except mysql.connector.Error as err:
            print('Hata:',err)
    
    @staticmethod
    def getStudentsGender(gender):
        sql = "select * from students where gender=%s"
        value = (gender,)

        Student.mycursor.execute(sql,value)

        try:
            return Student.mycursor.fetchall()
        except mysql.connector.Error as err:
            print('Error', err)    


# student = Student.getStudentById(5)

# student.name = 'Çınar'
# student.surname = 'Turan'

# student.updateStudent()

students = Student.getStudentsGender('E')
print(students)

liste = []
for std in students:
    std = list(std)
    std[2] = 'Mr ' + std[2]
    liste.append(std)

Student.updateStudents(liste)
