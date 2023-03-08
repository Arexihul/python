# 1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.
"""
x = int(input("Bir sayı giriniz: "))

result = (x > 0 ) and (x < 100)

print(f"Sayının 0- 100 arasında bir sayı olma durumu: {result}" )
"""
# 2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.
"""
x = int(input("Bir sayı giriniz: "))

result = (x > 0 ) and (x % 2 == 0 )

print(f"Sayının pozitif çift sayı olma durumu: {result}" )
"""
# 3- Email ve parola ile giriş kontrolü yapınız.
"""
email = "abc@email.com"
password = "asd123"

emailinput = input("Email giriniz: ")
passwordinput = input("Şifre giriniz: ")

result = (emailinput == email) and (passwordinput == password)

print(f"Giriş başarılı mı: {result}")
"""
# 4- Girilen 3 sayıdan en büyüğünü bulunuz.
"""
x = int(input("1. sayıyı giriniz: "))
y = int(input("2. sayıyı giriniz: "))
z = int(input("3. sayıyı giriniz: "))

result = (x > y) and (x > z)
print(f"1.sayı en büyük sayı mı {result}")

result = (y > x) and (y > z)
print(f"2.sayı en büyük sayı mı {result}")

result = (z > x) and (z > y)
print(f"3.sayı en büyük sayı mı {result}")
"""
# 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#      Eğer ortalama 50 ve üstündeyse geçti, değilse kaldı yazdırın.
#      A-) Ortalama 50 olsa bile final notu en az 50 olmalıdır.
#      B-) Finalden 70 alındığında ortalamanın bi önemi olmasın.
"""
vize1 = float(input("1.vize notunuz: "))
vize2 = float(input("2.vize notunuz: "))
final = float(input("Final notunuz: "))
ort = vize1*0.3 + vize2*0.3 + final*0.4

result = ((ort >= 50) and (final >= 50)) or (final >= 70)
print(f"Ortalamanız {ort} ve Geçme durumunuz: {result}")
"""
# 6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
#      (Formül: Kilo / Boy uzunluğunun karesi)
#      Aşağıdaki tabloya göre kişi hangi gruba girmektedir?
#      0 - 18.4 => Zayıf
#      18.5 - 24.9 => Normal
#      25.0 - 29.9 => Fazla Kilolu
#      30.0 - 34.9 => Şişman(Obez)
"""
kg = float(input("Kilonuzu giriniz: "))
m = float(input("Boyunuzu giriniz: "))
indeks = kg/m**2

result = (indeks > 0) and (indeks < 18.5)
print(f"Zayıf mısın: {result}")

result = (indeks > 18.5) and (indeks < 25)
print(f"Normal kilolu musun: {result}")

result = (indeks > 25) and (indeks < 30)
print(f"Fazla kilolu musun: {result}"),

result = (indeks > 30) 
print(f"Obez misin: {result}")
"""

