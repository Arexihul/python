# x = 10 

# if x > 5:
#      raise Exception("x, 5'ten büyük değer alamaz")

def checkPassword(psw):
     import re
     if len(psw) < 8:
          raise Exception("Parola en az 8 karakter olmalıdır")
     elif not re.search("[a-z]", psw):
          raise Exception("Parola küçük harf içermelidir")
     elif not re.search("[A-Z]", psw):
          raise Exception("Parola büyük harf içermelidir")
     elif not re.search("[0-9]", psw):
          raise Exception("Parola rakam içermelidir")
     elif not re.search("[_@$]", psw):
          raise Exception("Parola alpha numeric karakter içermelidir")
     elif re.search(" ", psw):
          raise Exception("Parola boşluk karakteri içermemelidir")


password = "12345 678aA_"

try:
     checkPassword(password)
except Exception as ex:
     print(ex)
else:
     print("Parola geçerli")
finally:
     print("Validation tamamlandı")


class Person:
     def __init__(self, name, year):
          if len(name) > 10:
               raise Exception("İsim 10 karakterden fazla olmamalıdır")
          else:
               self.name = name

p = Person("Abuziddincan", 1233)

