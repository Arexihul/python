# Fonksiyondan Fonksiyon Döndürme

def usalma(number):

     def inner(power):
          return number ** power

     return inner

two = usalma(2)     # two fonksiyonu inner fonksiyonunu temsil ediyor
print(two(5))

three = usalma(3)
print(three(4))

def yetki_sorgula(page):

     def inner(role):
          if role == "Admin":
               return f"{role} rolü {page} sayfasına ulaşabilir."
          else:
               return f"{role} rolü {page} sayfasına ulaşamaz."

     return inner

sorgu = yetki_sorgula("Product Edit")
print(sorgu("Admin"))
print(sorgu("User"))


def islem(islem_adi):

     def toplama(*args):
          toplam = 0
          for i in args:
               toplam +=i
          return toplam

     def carpma(*args):
          carpim = 1
          for i in args:
               carpim*=i
          return carpim

     if islem_adi == "toplama":
          return toplama
     elif islem_adi == "carpma":
          return carpma
     else:
          return "Hatalı işlem girdiniz"

result = islem("toplama")
print(result(2,5,8))

result = islem("carpma")
print(result(2,5,8))

