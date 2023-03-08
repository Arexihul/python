def asalbul(num1,num2):
    asallar = []
    for i in range(num1,num2+1):
        if i>1:
            for j in range(2,i):
                if i%j ==0:
                    break
            else:
                asallar.append(i)
    return asallar

print(asalbul(0,100))

def bölenler(sayi):
    liste = []
    for i in range(1,sayi+1):
        if sayi%i == 0:
            liste.append(i)
    return liste

print(bölenler(18))

import random
rand = random.uniform(30,35)
print(rand)