import mysql.connector
from datetime import datetime
from connection import connection
from students import Student
from teacher import Teacher
from lesson import Lesson
from classs import Class

class DbManager:
    def __init__(self):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def getStudentById(self,id):
        sql = "select * from students where id=%s"
        value=(id,)
        self.cursor.execute(sql,value)
        try:
            obj = self.cursor.fetchone()
            return Student.CreateStudent(obj)
        except mysql.connector.Error as err:
            print("Error:",err)

    def getStudentsByClassId(self,classid):
        sql = "select * from students where classid=%s"
        value=(classid,)
        self.cursor.execute(sql,value)
        try:
            obj = self.cursor.fetchall()
            return Student.CreateStudent(obj)
        except mysql.connector.Error as err:
            print("Error:",err)

    def getClasses(self):
        sql = "select * from class"
        self.cursor.execute(sql)
        try:
            obj = self.cursor.fetchall()
            return Class.createClass(obj)
        except mysql.connector.Error as err:
            print("Error:",err)

    def addStudent(self, student: Student):
        sql = "INSERT INTO students (StudentNumber,Name,Surname,Birthdate,Gender,ClassId) values (%s,%s,%s,%s,%s,%s)"
        value = (student.studentNumber,student.name,student.surname,student.birthDate,student.gender,student.classid)
        self.cursor.execute(sql,value)

        try:
            self.connection.commit()
            print("Student added.")
        except mysql.connector.Error as err:
            print("Error: ", err)

    def editStudent(self, student: Student):
        sql = "update students set studentnumber=%s,name=%s,surname=%s,birthdate=%s,gender=%s,classid=%s where id=%s"
        values = (student.studentNumber,student.name,student.surname,student.birthDate,student.gender,student.classid,student.id)
        self.cursor.execute(sql,values)

        try:
            self.connection.commit()
            print('kayıt güncellendi')
        except mysql.connector.Error as err:
            print('Hata:',err)

    def deleteStudent(self, studentid):
        sql = "delete from students where id=%s"
        value = (studentid,)
        self.cursor.execute(sql,value)

        try:
            self.connection.commit()
            print("Student deleted.")
        except mysql.connector.Error as err:
            print("Error: ", err)

    def addTeacher(self, teacher: Teacher):
        pass

    def editTeacher(self, teacher: Teacher):
        pass

    def __del__(self):
        self.connection.close()
        print("Database connection ended")

db = DbManager()

# student = db.getStudentById(2)
# print(student[0].name)
# print(student[0].surname)

# students = db.getStudentsByClassId(1)
# print(students[0].name)
# print(students[4].name)

# student = db.getStudentById(2)
# student[0].name = "Çınar"
# student[0].surname = "Turan"
# student[0].studentNumber = 501
# db.addStudent(student[0])

student = db.getStudentById(2)
student[0].name = "Ahmet"
db.editStudent(student[0])
