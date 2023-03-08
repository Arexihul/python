def my_decorator(func):
     def wrapper():
          print("Fonksiyondan önceki işlemler")
          func()
          print("Fonksiyondan sonraki işlemler")
     return wrapper

# def sayHello():
#      print("Hello")

# sayHello = my_decorator(sayHello)
# sayHello()

# veya kısaca:

# @my_decorator
# def sayHello():
#      print("Hello")

# sayHello()


import math
import time

# def usalma(a,b):
#      start = time.time()
#      time.sleep(1)
#      print(math.pow(a,b))
#      finish = time.time()
#      print(f"Fonksiyon {finish - start} saniye sürdü")

# usalma(2,5)

# def faktoriyel(num):
#      start = time.time()
#      time.sleep(1)
#      print(math.factorial(num))
#      finish = time.time()
#      print(f"Fonksiyon {finish - start} saniye sürdü")

# faktoriyel(6)

def calculate_time(func):
     def inner(*args,**kwargs):
          start = time.time()
          time.sleep(1)
          func(*args,**kwargs)
          finish = time.time()
          print(f"Fonksiyon {func.__name__} {finish - start} saniye sürdü")
     return inner

@calculate_time
def usalma(a,b):
     print(math.pow(a,b))

@calculate_time
def faktoriyel(num):
     print(math.factorial(num))

@calculate_time
def toplama(a,b):
     print(a+b)

usalma(2,5)
faktoriyel(6)
toplama(13,68)

