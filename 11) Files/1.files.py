"""
Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır.
Kullanımı: open(dosyaAdi,dosyaErismeModu)
dosyaErismeModu => Dosyayı hangi amaçla açtığınızı belirler.
"""

"""
"w": (Write) Yazma modu. 
   Dosyayı konumda oluşturur.
   Dosya içeriğini siler ve yeniden ekleme yapar.
"""
# dosya = open("newfile.txt","w")
# print(dosya)
# dosya.close()

# dosya2 = open("C:/Users/User/Desktop/newfile.txt","w")
# print(dosya2)
# dosya2.close()

# file = open("newfile.txt","w",encoding="utf-8")
# file.write("Eyüp Ülgen")
# file.close()

""" 
"a": (Append) Ekleme modu. 
     Dosya konumda yoksa oluşturur.
"""
# file = open("newfile.txt","a",encoding="utf-8")
# file.write("\nEyüp Ülgen")
# file.close()

"""
"x": (Create) Oluşturma modu. 
     Dosya zaten varsa hata verir.
"""

# file = open("newfile2.txt","x",encoding="utf-8")

"""
"r": (Read) Okuma modu. Varsayılan. 
     Dosya konumda yoksa hata verir.
"""

