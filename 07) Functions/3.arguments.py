def changeName(n):
     n = "Ada"

name = "Yiğit"

changeName(name)
print(name)

def change(n):
     n[0] = "İstanbul"

cities = ["Ankara", "İzmir"]
x = cities[:]  # slicing / copy

change(cities)
print(cities)
print(x)

def add(a, b):
     return sum((a,b))

print(add(15,20))

def add2(a, b, c = 0):
     return sum((a,b,c))

print(add2(15,10))
print(add2(15,20,35))

def add3(*params):
     print(params)
     print(params[1])
     return sum((params))

print(add3(26,4))
print(add3(32,20,13))
print(add3(12,37,8,64,23,92))

# # sum fonksiyonunu kullanmak istemezsek

def add4(*params):
     print(type(params))
     num = 0
     for x in params:
          num += x
     return num

print(add4(26,4))
print(add4(32,20,13))
print(add4(12,37,8,64,23,92))

def displayUser(**args):
     print(type(args))
     for key, value in args.items():
          print(f"{key} is {value}")

displayUser(name = "Çınar", age = 2, city = "İstanbul")
displayUser(name = "Ada", age = 12, city = "Kocaeli", phone = "123123")
displayUser(name = "Yiğit", age = 14, city = "Ankara", phone = "321321", email = "yigit@gmail.com")

def myfunc(a, b, *args, **kwargs):
     print(a)
     print(b)
     print(args)
     print(kwargs)

myfunc(10,20,30,40,50, key1 = "value1", key2 = "value2")

