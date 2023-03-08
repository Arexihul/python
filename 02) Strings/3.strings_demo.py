website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 Saat)"

# 1- 'course' karakter dizisinde kaç karakter bulunmaktadır ? 

result = len(course)

# 2- 'website' içinden www karakterlerini alın

result = website[7:10]

# 3- 'website' içinden com karakterlerini alın

result = website[22:]
result = website[-3:]

length = len(website)
result = website[length-3:length-1]


# 4- 'course' içinden ilk 15 ve son 15 karakterleri alın

result = course[:15]
result = course[-15:]

# 5- 'course' ifadesindeki karakterleri tersten yazdırın

result = course[::-1]

# örnek

# s = "12345" * 5

# print(s)
# print(s[::5])

name, surname, age, job = "Bora", "Yılmaz", 32, "mühendis"

# 6- Yukarıda verilen değişkenlerle aşağıdaki ifadeyi yazdırınız
#      "Benim adım Bora Yılmaz, yaşım 32 ve mesleğim mühendis"

result = "Benim adım {0} {1}, yaşım {2} ve ve mesleğim {3}".format(name, surname, age, job)
result = f"Benim adım {name} {surname}, yaşım {age} ve mesleğim {job}"

# 7- 'Hello world' ifadesindeki 'w' harfini 'W' ile değiştiriniz

x = "Hello world"
x = x[:6] + "W" + x[-4:]

# Kısa yoldan => x.replace("w","W")

print(x)

# 8- 'abc' ifadesini yan yana 3 defa yazdırınız

result = "abc " * 3


print(result)

