import mysql.connector

def getStudents():
    connection = mysql.connector.connect(host="localhost", user="root", password="12u8g6v5", database="schooldb")
    cursor = connection.cursor()

    # cursor.execute("select * from students")
    cursor.execute("select StudentNumber,Name,Surname from students")


    result = cursor.fetchall()

    for student in result:
        # print(f'Student Number:{student[1]} Name:{student[2]} Surname:{student[3]}')
        print(f'Student Number:{student[0]} Name:{student[1]} Surname:{student[2]}')


getStudents()
