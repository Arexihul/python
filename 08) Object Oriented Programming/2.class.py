# CLASS

class Person:
     # pass
     # CLASS ATTRİBUTES
     address = "no information"
     # CONSTRUCTOR (Yapıcı Metod)
     def __init__(self, name, year):    # self class'tan üretilen herhangi bir objeyi temsil ediyor (p1, p2 gibi)
          # OBJECT ATTRİBUTES           # yani obje üzerine bir değer aktarılcağında self kullanılır
          self.name = name
          self.year = year
          print("init metodu çalıştı")
     # METHODS               
          

# OBJECT(İNSTANCE)

p1 = Person("Eyüp", 2001)  # p1 objesini Person classında tanımladık
p2 = Person("Nihal", 2010)

# Updating
p1.name = "Ahmet"
p1.address = "Kocaeli"

# Accessing object attributes

print(f"p1 => name:{p1.name} year:{p1.year} address:{p1.address}")
print(f"p2 => name:{p2.name} year:{p2.year} address:{p2.address}")

print(p1)
print(p2)
print(type(p1))
print(type(p2))
print(p1 == p2)

