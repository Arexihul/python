"""
   Bir müşterinin aşağıdaki bilgileri için değişken oluşturunuz.

   Müşteri Adı
   Müşteri Soyadı
   Müşteri Ad Soyad
   Müşteri Cinsiyet
   Müşteri TC Kimlik No
   Müşteri Doğum Yılı
   Müşteri Adres Bilgisi
   Müşteri Yaşı

"""
costumerName = "Cabbar"
costumerSurname = "Cabbaroğlu"
costumerFullname = costumerName + " " + costumerSurname
costumerGender = True #Erkek
costumerTCKNo = "14894023810"
costumerBirthDate = 1987
costumerAdress = "Bahçelievler / İstanbul"
costumerAge = 2020 - costumerBirthDate

print(costumerName)
print(costumerSurname)
print(costumerFullname)
print(costumerGender)
print(costumerTCKNo)
print(costumerBirthDate)
print(costumerAdress)
print(costumerAge)

"""
   Aşağıdaki siparişlerin toplam bilgisini hesaplayınız.

   Sipariş 1 => 110 TL
   Sipariş 2 => 1100.5 TL
   Sipariş 3 => 356.95 TL

"""
print(110 + 1100.5 + 356.95)

order1 = 110
order2 = 1100.5
order3 = 356.95

print(order1 + order2 + order3)

total = order1 + order2 + order3

print("Total = ", total)

