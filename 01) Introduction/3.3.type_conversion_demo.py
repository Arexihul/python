"""
Daire Alanı : pi*(r**2)
Daire Çevresi : 2*pi*r

Yarıçapı verilen bir dairenin alan ve çevresini hesaplayınız. ( pi = 3.14 )

"""

r = float(input("Yarıçapı giriniz :"))   # input bize str verir o yüzden number'a çevirmeliyiz

alan = 3.14 * (r**2)
print(type(alan))

cevre = 2 * 3.14 * r
print(type(cevre))

print("Alan: " + str(alan))   # alan ve cevre number olduğundan str'e cevirmeliyiz
print("Çevre: " + str(cevre))

