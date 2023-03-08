# 1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.
"""
num = int(input("Bir sayı giriniz: "))

if num > 0 and num < 100:
     print("Sayı 0-100 arasında")
else:
     print("Sayı 0-100 arasında değil.")
"""
# 2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.
"""
num = int(input("Bir sayı giriniz: "))

if num > 0 and num % 2 == 0:
    print("Sayı pozitif çift sayıdır")
elif num > 0 and num % 2 == 1:
    print("Sayı pozitif ancak tek")
elif num < 0 and num % 2 == 0:
    print("Sayı çift ancak negatif")
else:
    print("Sayı pozitif çift sayı değildir")
"""
# 3- Email ve parola bilgileri ile giriş kontrolü yapınız.
"""
email = "email@email.com"
password = "1234"

emailinput = input("Email: ")
passwordinput = input("Şifre: ")

if emailinput == email and passwordinput == password:
     print("Giriş başarılı")
elif emailinput == email and not passwordinput == password:
     print("Şifre hatalı")
else:
     print("Email hatalı")
"""
# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.
"""
num1 = int(input("1.sayı: "))
num2 = int(input("2.sayı: "))
num3 = int(input("3.sayı: "))

if num1 > num2 > num3:
     print(f"{num1}>{num2}>{num3}")
elif num1 > num3 > num2:
     print(f"{num1}>{num3}>{num2}")
elif num2 > num1 > num3:
     print(f"{num2}>{num1}>{num3}")
elif num2 > num3 > num1:
     print(f"{num2}>{num3}>{num1}")
elif num3 > num1 > num2:
     print(f"{num3}>{num1}>{num2}")
elif num3 > num2 > num1:
     print(f"{num3}>{num2}>{num1}")
else:
     print("Hatalı veya eşit sayılar girdiniz")
"""
# 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
#    a-) Ortamalama 50 olsa bile final notu en az 50 olmalıdır.
#    b-) Finalden 70 alındığında ortalamanın önemi olmasın.
"""
vize1 = float(input("1.vize notun: "))
vize2 = float(input("2.vize notun: "))
final = float(input("Final notun: "))
ort = (vize1*0.3 + vize2*0.3 + final*0.4)

if ort >= 50:
    if final >= 50:
        print(f"Ortalamanız {ort} ve geçtiniz")
    else:
        print(f"Ortalamanız {ort} ancak final notunuz {final} olduğundan kaldınız")
elif ort < 50 and final >= 70:
     print(f"Ortalamanız {ort} ancak final notunuz {final} olduğundan geçtiniz")
else:
     print(f"Ortalamanız {ort} ve kaldınız")
"""
# 6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
#    Formül: (Kilo / boy uzunluğunun karesi)
#    Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
#    0-18.4    => Zayıf
#    18.5-24.9 => Normal
#    25.0-29.9 => Fazla Kilolu
#    30.0-44.9 => Şişman (Obez)
"""
name = input("Adınız: ")
weight = float(input("Kilonuz: "))
height = float(input("Boyunuz(metre cinsinden): "))
indeks = weight / height**2

if indeks >= 0 and indeks < 18.5:
     print(f"{name} vücut kitle indeksin {indeks} yani zayıfsın")
elif indeks >= 18.5 and indeks < 25:
     print(f"{name} vücut kitle indeksin {indeks} yani ideal kilodasın")
elif indeks >= 25 and indeks < 30:
     print(f"{name} vücut kitle indeksin {indeks} yani fazla kilolusun")
elif indeks >= 30:
     print(f"{name} vücut kitle indeksin {indeks} yani obezsin")
else:
     print(f"{name} hatalı bilgi girdin")
"""

