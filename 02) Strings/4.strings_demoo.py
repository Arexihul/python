website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 Saat)"

# 1- 'course' karakter dizisinde kaç karakter bulunmaktadır ? 

print("1- " + str(len(course)))

# 2- 'website' içinden www karakterlerini alın

print("2- " + website[7:10])

# 3- 'website' içinden com karakterlerini alın

print("3- " + website[len(website)-3:])

# 4- 'course' içinden ilk 15 ve son 15 karakterleri alın

print("4- İlk 15: " + website[:15] + "  Son 15: " + website[-15:])

# 5- 'course' ifadesindeki karakterleri tersten yazdırın

print("5- " + course[::-1])

# 7- 'Hello world' ifadesindeki 'w' harfini 'W' ile değiştiriniz

x = "Hello world"

x = x[:6] + "W" + x[-4:]

print(x)

