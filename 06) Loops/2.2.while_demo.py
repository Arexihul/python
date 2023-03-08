sayilar = [1,3,5,7,9,12,19,21]

# 1: sayilar listesini while ile ekrana yazdırın.
"""
i = 0

while i < len(sayilar):
     print(sayilar[i])
     i += 1
"""
# 2: Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm
#    tek sayıları ekrana yazdırın.
"""
start = int(input("Başlangıç Değeri: "))
end = int(input("Bitiş Değeri: "))

while start < end:
     if start %2 == 1:
          print(start)
     start += 1
"""
# 3: 1-100 arasındaki sayıları azalan şekilde yazdırın.
"""
x = 100

while x > 0:
     print(x)
     x -= 1
"""
# 4: Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdırın.
"""
i = 0
liste = []

while i<5:
     x = int(input("Sayı: "))
     liste.append(x)
     i += 1

liste.sort()
print(liste)
"""
# 5: Kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesi içinde saklayınız.
#    ** ürün sayısını kullanıcıya sorun.
#    ** dictionary listesi yapısı (name, price) şeklinde olsun.
#    ** ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin.
"""
urunler = []

x = int(input("Ürün sayısını giriniz: "))
i = 0

while i<x:
     a = input("Ürün adı:")
     b = input("Ürün fiyatı: ")
     urunler.append({
          "name" : a,
          "price" : b
     })
     i += 1

y = 0

while y<x:
     print(f"Ürün: {urunler[y]['name']}  Fiyat: {urunler[y]['price']}")
     y += 1
"""

