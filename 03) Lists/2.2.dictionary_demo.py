"""
ogrenciler =  {
     "120" : {
          "ad" : "Ali",
          "soyad" : "Yılmaz",
          "telefon" : "532 000 00 01",
     },
     "125" : {
          "ad" : "Can",
          "soyad" : "Korkmaz",
          "telefon" : "532 000 00 02",
     },
     "128" : {
          "ad" : "Volkan",
          "soyad" : "Yükselen",
          "telefon" : "532 000 00 03",
      }, 
} 

1- Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle dictionary içinde saklayınız.

2- Öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösterin.

"""


# number1 = input("1. öğrenci numaranı gir : ")
# name1 = input(" Adını gir : ")
# surname1 = input(" Soyadını gir : ")
# phone1 = input(" Telefon numaranı gir : ")

# number2 = input("2. öğrenci numaranı gir : ")
# name2 = input(" Adını gir : ")
# surname2 = input(" Soyadını gir : ")
# phone2 = input(" Telefon numaranı gir : ")

# number3 = input("3. öğrenci numaranı gir : ")
# name3 = input(" Adını gir : ")
# surname3 = input(" Soyadını gir : ")
# phone3 = input(" Telefon numaranı gir : ")

# ogrenciler =  {
#      number1 : {
#           "ad" : name1,
#           "soyad" : surname1,
#           "telefon" : phone1,
#      },
#      number2 : {
#           "ad" : name2,
#           "soyad" : surname2,
#           "telefon" : phone2,
#      },
#      number3 : {
#           "ad" : name3,
#           "soyad" : surname3,
#           "telefon" : phone3,
#       },
# }

# print(ogrenciler)

# no = input("No gir : ")

# print(ogrenciler[no])


ogrenciler = {}

number = input("öğrenci no: ")
name = input("öğrenci adı: ")
surname = input("öğrenci soyadı: ")
phone = input("öğrenci telefonu: ")

# # ogrenciler[no] = {
# #      "ad" : name,
# #      "soyad" : surname,
# #      "telefon" : phone
# # }

# # veya update edilebilir

ogrenciler.update({
    number: {
        "ad": name,
        "soyad": surname,
        "telefon": phone
    }
})

number = input("öğrenci no: ")
name = input("öğrenci adı: ")
surname = input("öğrenci soyadı: ")
phone = input("öğrenci telefonu: ")

ogrenciler.update({
    number: {
        "ad": name,
        "soyad": surname,
        "telefon": phone
    }
})

number = input("öğrenci no: ")
name = input("öğrenci adı: ")
surname = input("öğrenci soyadı: ")
phone = input("öğrenci telefonu: ")

ogrenciler.update({
    number: {
        "ad": name,
        "soyad": surname,
        "telefon": phone
    }
})

print(ogrenciler)

print("*"*50)

ogrNo = input("Öğrenci no giriniz: ")
ogrenci = ogrenciler[ogrNo]

print(ogrenciler[ogrNo])

# print(f"{ogrNo} numaralı öğrencinin adı {ogrenci["ad"]}, soyadı {ogrenci["soyad"]} ve telefon numarası {ogrenci["telefon"]}")

# hata veriyo bu anlamadım

