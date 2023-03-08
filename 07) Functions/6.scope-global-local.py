# global scope
x = "global x"

def func():
     # local scope
     x = "local x"
     print(x)

func()
print(x)

#########################

# global
name = "Çınar"

def changeName(new_name):
     # local
     name = new_name
     print(name)

changeName("Ada")
print(name)

########################

name = "global string"

def greeting():
     # name = "Çınar"

     def hello():
          name = "Ada"
          print("hello " + name)

     hello()

greeting()
print(name)

#############################

x = 50

def test(x):
     print(f"x: {x}")

     x = 100
     print(f"x changed to {x}")

test(x)
print(x)


def testt():
     global x
     print(f"x: {x}")

     x = 100
     print(f"x changed to {x}")

testt()
print(x)

