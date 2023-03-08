"""
"r": (Read) Okuma modu. Varsayılan. 
     Dosya konumda yoksa hata verir.
"""

# try:
#      dosya = open("reading.txt","r")
# except FileNotFoundError:
#      print("Dosya bulunamadı")
# finally:
#      print("Dosya kapandı")
#      dosya.close()

dosyam = open("reading.txt","r",encoding="utf-8")

# for döngüsü ile okuma

# for i in dosyam:
#      print(i, end="")

# dosyam.close()


# ********** read() fonksiyonu ile okuma

# content1 = dosyam.read()

# print("İçerik 1")
# print(content1)

# content2 = dosyam.read()

# print("İçerik 2")
# print(content2)     # Dosya içeriğini yazdıramaz çünkü content1 okunduktan sonra dosyada kürsör en sona gider. 
#                     # content2 ise kürsörden sonrasını okucağı için bir şey okumaz.


# print(dosyam.read(4))
# print(dosyam.read(6))
# print(dosyam.read(10))

# ********** readline() fonksiyonu => her seferinde 1 satırı okur

# print(dosyam.readline(), end="")
# print(dosyam.readline(), end="")
# print(dosyam.readline(), end="")
# print(dosyam.readline(), end="")
# print(dosyam.readline())
# print(dosyam.readline())

# ********** readlines() fonksiyonu

# liste = dosyam.readlines()

# print(liste)
# print(liste[0])
# print(liste[1])


dosyam.close()

