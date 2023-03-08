# 1- Girilen 2 sayıdan hangisi büyüktür?

# sayi1 = input("1.sayıyı gir: ")
# sayi2 = input("2.sayıyı gir: ")

# result1 = (sayi1 > sayi2)
# print(f"1.sayı {sayi1} 2.sayı {sayi2}'den büyüktür: {result1}")   

# 2- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#      Eğer ortalama 50 ve üstünde ise geçti değilse kaldı yazdırınız.

# note1 = float(input("1.vize notunu gir: "))
# note2 = float(input("2.vize notunu gir: "))
# note3 = float(input("Final notunu gir: "))

# ort = (note1 * 0.3) + (note2 * 0.3) + (note3 * 0.4)
# # print("Ortalamanız: " + str(ort))

# result2 = ort >= 50
# # print("Geçme durumunuz: " + str(result2))

# print(f"Not ortalamanız: {ort} ve dersten geçme durumunuz: {result2}")

# 3- Girilen bir sayının tek mi çift mi olduğunu yazdırınız. 

# sayi = int(input("Bir sayı giriniz: "))

# tekcift = sayi % 2 == 0

# print(f"Girdiğiniz {sayi} sayısının çiftlik durumu: {tekcift}")

# 4- Girilen bir sayının negatif mi pozitif mi olduğunu yazdırınız.

# sayi = int(input("Bir sayı giriniz: "))

# qwe = sayi > 0 

# print(f"Girdiğiniz sayının pozitiflik durumu: {qwe}")

# 5- Parola ve e-mail bilgisini isteyip doğruluğunu kontrol ediniz.
#      (email: email@sadikturan.com  parola:abc123 )

email = "email@sadikturan.com"
parola = "abc123"

x = input("email gir: ")
y = input("parola gir: ")

a = x == email
b = y == parola

print(f"Girdiğiniz email {a}, parola {b}")

