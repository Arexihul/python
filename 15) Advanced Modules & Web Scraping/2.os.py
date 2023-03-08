import os
import datetime

# print(dir(os))

"""İşletim Sistemi Öğrenme"""
# print(os.name)         # nt => windows

"""Dizin Değiştirme"""
# os.chdir("C://")         # konumu değiştirir
# os.chdir("..")      # Bir üst dizine geçer
# os.chdir("../..")      # İki üst dizine geçer

"""Klasör Oluşturma"""
# os.mkdir("NewDirectory")      # konumda klasör oluşturur
# os.makedirs("newdirectory/yeniklasör")       # Klasör içinde klasör açar
# os.rename("newdirectory", "yeni klasör")     # Klasörün ismini değiştirir
# os.rmdir("NewDirectory")      # Dosyayı siler
# os.removedirs("yeni klasör/yeniklasör")    # dosyaları siler

"""Listeleme"""
# result = os.listdir()    # Konumdaki dosyaları listeler
# result = os.listdir("C://")
# for dosya in os.listdir("C:\\Users\\User\\Desktop\\python\\1) İntroduction"):
#      if dosya.endswith(".py"):
#           print(dosya)

"""Etkin Dizin Öğrenme"""
result = os.getcwd()     # konumu gösterir

result = os.stat("1) Introduction")
"""st_size => dosyanın byte cinsinden büyüklüğü
st_atime => dosyaya son erişilme zamanı(saniye olarak)
st_mtime => son değiştirilme tarihi
st_ctime => dosyanın oluşturulma zamanı"""

# result = result.st_size / 1024
# result = datetime.datetime.fromtimestamp(result.st_ctime)
# result = datetime.datetime.fromtimestamp(result.st_atime)
# result = datetime.datetime.fromtimestamp(result.st_mtime)

# print(result)

# os.system("notepad.exe")

""" path """

result = os.path.abspath("2.os.py")     # Herhangi bir dosyanın konumunu verir
result = os.path.dirname("C:/Users/User/Desktop/python/2.os.py")      # Tam konumu verilen bir dosyanın dizin ismini verir
result = os.path.dirname(os.path.abspath("1.datetime.py"))
result = os.path.exists("1) Introduction")        # True    # Klasör var mı?
result = os.path.exists("2) Introduction")        # False
result = os.path.exists("C:/Users/User/Desktop/python")     # True
result = os.path.isdir("C:/Users/User/Desktop/python")      # True    # Klasör mü?
result = os.path.isdir("C:/Users/User/Desktop/python/15) Advanced Modules & Web Scraping/2.os.py")   # False
result = os.path.isfile("C:/Users/User/Desktop/python/15) Advanced Modules & Web Scraping/2.os.py")  # True   # Dosya mı?    
result = os.path.join("C:\\","deneme","deneme1")       # Dizinleri birleştirir
result = os.path.split("C:\\deneme")         # Dizinleri ayırır
result = os.path.splitext("2.os.py")         # Dosya adı ve uzantıyı ayırır
# result = result[0]
result = result[1]

print(result)

