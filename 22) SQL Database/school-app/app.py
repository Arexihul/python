from dbmanager import DbManager
from students import Student
import datetime

class App:
    def __init__(self):
        self.db = DbManager()

    def initApp(self):
        msg = "*****\n1- Student List\n2- Add Student\n3- Edit Student\n4- Delete Student\n5- Add Teacher\n6- Lessons by Classes\n7- Exit(e)"
        while(True):
            print(msg)
            task = input("Choice: ")
            if task == '1':
                self.displayStudents()
            elif task == '2':
                self.addStudent()
            elif task == '3':
                self.editStudent()
            elif task == '4':
                self.deleteStudent()
            elif task == 'e':
                break
            else:
                print("Wrong choice")

    def displayClasses(self):
        classes = self.db.getClasses()
        for c in classes:
            print(f'{c.id}: {c.name}')

    def displayStudents(self):
        self.displayClasses()

        classid = int(input("Which class: "))

        students = self.db.getStudentsByClassId(classid)
        print("Student List")
        for std in students:
            print(f'{std.id}- {std.name} {std.surname}')

        return classid

    def addStudent(self):
        self.displayClasses()

        classid = int(input("Which class: "))
        studentNumber = input("Student Number: ")
        name = input("Name: ")
        surname = input("Surname: ")
        print("Birthdate: ")
        year = int(input("Year: "))
        month= int(input("Month: "))
        day = int(input("Day: "))
        birthdate = datetime.date(year, month, day)
        gender = input("Gender(M/F): ")

        student = Student(None, studentNumber, name, surname, birthdate, gender, classid)
        self.db.addStudent(student)

    def editStudent(self):
        classid = self.displayStudents()
        studentid = int(input("Student Id: "))

        student = self.db.getStudentById(studentid)

        student[0].name = input("Name: ") or student[0].name
        student[0].surname = input("Surame: ") or student[0].surname
        student[0].gender = input("Gender(M/F): ") or student[0].gender
        student[0].classid = input("Class: ") or student[0].classid

        year = input("Year: ") or student[0].birthDate.year
        month = input("Month: ") or student[0].birthDate.month
        day = input("Day: ") or student[0].birthDate.day
        student[0].birthDate = datetime.date(year,month,day)

        self.db.editStudent(student[0])

    def deleteStudent(self):
        classid = self.displayStudents()
        studentid = int(input('Student id: '))

        self.db.deleteStudent(studentid)


app = App()
app.initApp()