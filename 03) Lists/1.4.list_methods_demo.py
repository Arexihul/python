names = ["Ali", "Yağmur", "Hakan", "Deniz"]
years = [1998, 2000, 1998, 1987]

# 1- "Cenk" ismini listenin sonuna ekleyiniz.

# names.append("Cenk")
# print(names)

# 2- "Sena" değerini listenin başına ekleyiniz.

# names.insert(0, "Sena")
# print(names)

# 3- "Deniz" ismini listeden siliniz.

# names.remove("Deniz")
# print(names)

# 4- "Deniz" isminin indexi nedir ? 

print(names.index("Deniz"))

# 5- "Ali" listenin bir elemanı mıdır ?

# print(names.count("Ali"))
# print(names.index("Ali"))
result = "Ali" in names
print(result)

# 6-  Liste elemanlarını terse çevirin.

names.reverse()
print(names)

# 7- Liste elemanlarını alfabetik olarak sıralayınız.

names.sort()
print(names)

# 8- years listesini rakamsal büyüklüklerine göre sıralayınız.

years.sort()
print(years)

# 9- str = "Chevrolet, Dacia" karakter dizisini listeye çeviiniz.

str = "Chevrolet, Dacia"
cars = str.split(",")
print(cars)

# 10- years dizinin en büyük ve en küçük rakamsal değerleri nelerdir ?

MAX = max(years)
MİN = min(years)

print(MAX, MİN)

# 11- years dizisinde kaç tane 1998 değeri vardır ?

print(years.count(1998))

# 12- years dizisinin tüm elemanlarını siliniz.

years.clear()
print(years)

# 13- Kullanıcıdan alacağınız üç tane marka bilgisini birlistede saklayınız.

# brand1 = input("1. markayı giriniz.")
# brand2 = input("2. markayı giriniz.")
# brand3 = input("3. markayı giriniz.")

# brands = [brand1, brand2, brand3]
# print(brands)

brands = []

brand = input("Marka: ")
brands.append(brand)

brand = input("Marka: ")
brands.append(brand)

brand = input("Marka: ")
brands.append(brand)

print(brands)

