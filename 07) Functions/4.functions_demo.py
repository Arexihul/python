# 1- Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazın.
"""
def yazdır(word = "word", tekrar = 1):
     for x in range(0, tekrar):
          print(word)

yazdır("asa", 3)

def yazdir(kelime, adet):
    print(kelime * adet)

yazdir('Merhaba\n', 10)
"""
# 2- Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyonu yazınız.
"""
# def makelist(*params):
#      print(params)
                         # Bu tuple yapar
# makelist(1,2,3,4,5,6,7)   

def makeList(*par):
     liste = []

     for x in par:
          liste.append(x)

     return liste

random = makeList(1,2,4,6543,57,34,234,"lnmlk","fwgdsfh")
print(random)
"""
# 3- Gönderilen 2 sayı arasındaki tüm asal sayıları bulun.
"""
def asalbul(x,y):
     asallar = []
     for sayi in range(x,y+1):
          if sayi>1:
               for k in range(2,sayi):
                    if sayi%k==0:
                         break
               else:
                    asallar.append(sayi)
     return asallar

print(asalbul(5,17))
"""
# 4- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndürünüz.
"""
def bölenler(x):
     bölenler = []
     for sayi in range(1,x):
          if x%sayi == 0:
               bölenler.append(sayi)
     return bölenler

print(bölenler(15))
"""
