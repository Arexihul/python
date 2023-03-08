website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 Saat)"

# 1- " Hello World " karakter dizisinin baş ve sondaki boşluk karakterlerini silin.

print("Cevap 1".center(40))
print(" Hello World ".strip())
# print(" Hello World ".rstrip())      # sağdaki boşluğu siler
# print(" Hello World ".lstrip())      # soldaki boşluğu siler

# 2- "www.sadikturan.com" içindeki sadikturan bilgisi haricindeki her karakteri silin.

print("Cevap 2".center(20))
print("www.sadikturan.com".strip("w.moc"))

# 3- "course" karakter dizisinin tüm karakterlerini küçük harf yapın.

print("Cevap 3".center(20))
print(course.lower())

# 4- "website" içinde kaç tane 'a' karakteri vardır? (count("a"))

print("Cevap 4".center(20))
print(website.count("a"))

# 5- "website" www ile başlayıp com ile bitiyor mu?

print("Cevap 5".center(20))
print(website.startswith("www"))
print(website.endswith("com"))

# 6- "website" içinde 'com' ifadesi var mı?

print("Cevap 6".center(20))
print(website.count("com"))   #com'un kaç tane olduğunu söyler
print(website.find("com"))    # com'un yerini söyler
print(website.find("com",0,10))    # 0 ile 10. indexler arasında com var mı ona bakar

# find ve index

# print(course.find("Python"))    # baştan başlayarak sayar ve ilk Python'ı bulur
# print(course.rfind("Python"))   # sondan başlayarak sayar ve 2.Python'ı bulur

# print(course.index("Python"))   
# print(course.rindex("Python"))   
# print(course.index("Pythonn"))   # index'de sonuç yoksa -1 vermez hata verir tek fark budur

# 7- "course" içindeki karakterlerin hepsi alfabetik mi? (isalpha,isdigit)

print("Cevap 7".center(20))
print(course.isalpha())
print(course.isdigit())

# 8- "Contents" ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyin.

print("Cevap 8".center(20))
print("Contents".center(50,"*"))
# print("Contents".ljust(50,"*"))
# print("Contents".rjust(50,"*"))

# 9- "course" karakter dizisindeki tüm boşluk karakterlerini "-" ile değiştiriniz.

print("Cevap 9".center(20))
print(course.replace(" ","-"))
# print(course.replace(" ","-",5))   # sadece 5 karakteri değiştirir

# 10- "Hello World" karakter dizisinin "World" ifadesini "There" olarak değiştiriniz.

print("Cevap 10".center(20))
print("Hello World".replace("World","There"))

# 11- "course" karakter dizisini boşluk karakterlerinden ayırınız.

print("Cevap 11".center(20))
print(course.split())
print(course.split(" "))

