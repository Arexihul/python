import mysql.connector

def getStudent():
    connection = mysql.connector.connect(host="localhost", user="root", password="12u8g6v5", database="schooldb")
    cursor = connection.cursor()

    sql = "Select COUNT(*) from students"   # row count
    sql = "Select COUNT(*) from students where StudentNumber > 103"
    sql = "Select AVG(StudentNumber) from students"   # avarage value
    sql = "Select SUM(StudentNumber) from students"
    sql = "Select MIN(StudentNumber) from students"
    sql = "Select MAX(StudentNumber) from students"
    sql = "Select name from students where StudentNumber = (Select MAX(StudentNumber) from students)"


    cursor.execute(sql)

    student = cursor.fetchone()
    print(f'Result: {student[0]}')

getStudent()
