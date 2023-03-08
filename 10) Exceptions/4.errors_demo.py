liste = ["1","2","5a","10b","abc","10","50"]

# 1: Liste elemanları içindeki sayısal değerleri bulunuz.
"""
newlist = []

for l in liste:
     try:
          l = int(l)
     except ValueError:
          continue
     else:
          newlist.append(l)
          
print(newlist)
"""
# 2: Kullanıcı 'quit' değerini girmedikçe aldığınız her inputun sayı
# olduğundan emin olunuz aksi halde hata mesajı yazın.
"""
while True:
     x = input("Sayı giriniz: ")
     if x == "quit":
          print("İşlem sonlandırıldı")
          break

     try:
          x = int(x)
          print(f"Girdiğiniz sayı: {x}")
     except ValueError:
          print("Geçersiz bilgi girdiniz")
"""
# 3: Girilen parola içinde türkçe karakter hatası veriniz.
"""
def checkPassword(psw):
     import re
     if re.search("[ıİşğüçöÜŞĞÇÖ]", psw):
          raise Exception("Parola türkçe karakter içermemelidir")
     else:
          print("Şifre kaydedildi")

sifre = input("Parola giriniz: ")

checkPassword(sifre)
"""
# 4: Faktöriyel fonksiyonu oluşturup fonksiyona gelen değer için
# hata mesajları verin.

def faktöriyel(x):
     x = int(x)

     if x < 0:
          raise ValueError("Negatif değer girmeyiniz")

     result = 1

     for i in range(1, x+1):
          result *= i

     return result

for x in [5, 10, 20, -3, '10a']:
     try:
          y = faktöriyel(x)
     except ValueError as err:
          print(err)
          continue  
     print(y)

