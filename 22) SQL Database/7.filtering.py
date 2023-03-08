import mysql.connector

# def getStudents():
#     connection = mysql.connector.connect(host="localhost", user="root", password="12u8g6v5", database="schooldb")
#     cursor = connection.cursor()

#     # cursor.execute("select * from students where name='Ali'")
#     # cursor.execute("select * from students where name='Ali' and Surname='Can'")
#     # cursor.execute("select * from students where name='Ali' or StudentNumber='104'")
#     # cursor.execute("select * from students where name LIKE '%e%'")
#     cursor.execute("select * from students where name LIKE '%e%' or Surname='Toksöz'")


#     result = cursor.fetchall()

#     for student in result:
#         print(f'Student Number:{student[1]} Name:{student[2]} Surname:{student[3]}')

# getStudents()


def getStudentById(id):
    connection = mysql.connector.connect(host="localhost", user="root", password="12u8g6v5", database="schooldb")
    cursor = connection.cursor()

    sql = "Select * from students Where id=%s"
    params= (id,)

    cursor.execute(sql,params)

    student = cursor.fetchone()
    print(f'Student Number:{student[1]} Name:{student[2]} Surname:{student[3]}')

getStudentById(3)
