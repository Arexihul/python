# CLASS

class Person:
     # CLASS ATTRİBUTES
     address = "no information"

     # CONSTRUCTOR (Yapıcı Metod)
     def __init__(self, name, year):

          # OBJECT ATTRİBUTES          
          self.name = name
          self.year = year
          print("init metodu çalıştı")

     # İNSTANCE METHODS               
     def intro(self):
          print("Hello there I am " + self.name)

     def calculateAge(self):
          return 2020 - self.year


# OBJECT(İNSTANCE)

p1 = Person("Eyüp", 2001)
p2 = Person("Nihal", 2010)

p1.intro()
p2.intro()
print(f"Adım {p1.name} ve yaşım {p1.calculateAge()}")
print(f"Adım {p2.name} ve yaşım {p2.calculateAge()}")

##########################

class Circle:
     # Class Object Attribute
     pi = 3.14

     def __init__(self, yaricap=1):
          self.r = yaricap

     # Methods
     def cevreHesapla(self):
          return 2 * self.pi * self.r

     def alanHesapla(self):
          return self.pi * (self.r**2)


c1 = Circle()
c2 = Circle(5)

print(f"c1 => Alan = {c1.alanHesapla()} Çevre = {c1.cevreHesapla()}")
print(f"c2 => Alan = {c2.alanHesapla()} Çevre = {c2.cevreHesapla()}")

