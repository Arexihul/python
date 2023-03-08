# Inheritance: Kalıtım - Miras alma

# Person => name, lastname, age, eat(), run(), drink()
# Student(Person), Teacher(Person)

# Animal => Dog(Animal), Cat(Animal)

class Person():
     def __init__(self, fname, lname):
          self.firstName = fname
          self.lastName = lname
          print("Person created")

     def whoami(self):
          print("I am a person")

     def eat(self):
          print("I am eating")

# class Studenttt(Person):
#      pass

# class Studentt(Person):
#      def __init__(self):
#           print("Student created")

class Student(Person):
     def __init__(self, fname, lname, number):
          Person.__init__(self, fname, lname)
          self.studentNumber = number
          print("Student created")

     # override
     def whoami(self):
          print("I am a student")

     def sayHello(self):
          print("Hello there")

class Teacher(Person):
     def __init__(self, fname, lname, branch):
          super().__init__(fname, lname)  # super methodu sayesinde self yazmak zorunda değiliz
          self.branch = branch

     def whoami(self):
          print(f"I am a {self.branch} teacher")

p1 = Person("Ali", "Yılmaz")
s1 = Student("Çınar", "Turan", 1818)
t1 = Teacher("Serkan", "Aydın", "Math")

print(p1.firstName + " " + p1.lastName)
print(s1.firstName + " " + s1.lastName + " " + str(s1.studentNumber))

p1.whoami()
s1.whoami()
p1.eat()
s1.eat()
s1.sayHello()
t1.whoami()

