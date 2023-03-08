import mysql.connector

def getStudentsByName():
    connection = mysql.connector.connect(host="localhost", user="root", password="12u8g6v5", database="schooldb")
    cursor = connection.cursor()

    cursor.execute("select * from students order by name")
    # cursor.execute("select * from students order by name DESC")     # Azalan şekilde sıralar. Tersi ASC

    try:
        result = cursor.fetchall()
        for student in result:
            print(f'Student Number:{student[1]} Name:{student[2]} Surname:{student[3]}')
    except mysql.connector.Error as err:
        print("Hata: ", err)
    finally:
        connection.close()    
        print("Database connection disabled")


getStudentsByName()
