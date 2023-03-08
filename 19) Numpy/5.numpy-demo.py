import numpy as np

# 1- (10,15,30,45,60) değerlerine sahip numpy dizisi oluşturunuz.
print("****Soru 1****")
dizi = np.array([10,15,30,45,60])
print(dizi)
# 2- (5-15) arasındaki sayılarla numpy dizisi oluşturunuz.
print("****Soru 2****")
dizi = np.arange(5,15)
print(dizi)
# 3- (50-100) arasında 5'er 5'er artarak numpy dizisi oluşturunuz.
print("****Soru 3****")
dizi = np.arange(50,100,5)
print(dizi)
# 4- 10 elemanlı sıfırlardan oluşan bir dizi oluşturunuz.
print("****Soru 4****")
dizi = np.zeros(10)
print(dizi)
# 5- 10 elemanlı birlerden oluşan bir dizi oluşturunuz.
print("****Soru 5****")
dizi = np.ones(10)
print(dizi)
# 6- (0-100) arasında eşit aralıklı 5 sayı üretin.
print("****Soru 6****")
dizi = np.linspace(0,100,5)
print(dizi)
# 7- (10-30) arasında rastgele 5 tane tamsayı üretin.
print("****Soru 7****")
dizi = np.random.randint(10,30,5)
print(dizi)
# 8- [-1 ile 1] arasında 10 adet sayı üretin.
print("****Soru 8****")
dizi = np.random.randn(10)
print(dizi)
# 9- (3x5) boyutlarında (10-50) arasında rastgele bir matris oluşturunuz.
print("****Soru 9****")
matris = np.random.randint(10,50,15)
matrisx = matris.reshape(3,5)
print(matrisx)
# 10- Üretilen matrisin satır ve sütun sayıları toplamlarını hesaplayınız ?
print("****Soru 10****")
print(f"Satırlar: {matrisx.sum(axis=1)}")
print(f"Sütunlar: {matrisx.sum(axis=0)}")
# 11- Üretilen matrisin en büyük, en küçük ve ortalaması nedir ?
print("****Soru 11****")
print(matris.max())
print(matris.min())
print(matris.mean())
# 12- Üretilen matrisin en büyük değerinin indeksi kaçtır ?
print("****Soru 12****")
print(matris.argmax())
# 13- (10-20) arasındaki sayıları içeren dizinin ilk 3 elemanını seçiniz.
print("****Soru 13****")
dizi = np.arange(10,20)
print(dizi[:3])
# 14- Üretilen dizinin elemanlarını tersten yazdırın.
print("****Soru 14****")
print(dizi[::-1])
# 15- Üretilen matrisin ilk satırını seçiniz.
print("****Soru 15****")
print(matrisx[0])
# 16- Üretilen matrisin 2.satır 3.sütundaki elemanı hangisidir ?
print("****Soru 16****")
print(matrisx[1,2])
# 17- Üretilen matrisin tüm satırlardaki ilk elemanı seçiniz.
print("****Soru 17****")
print(matrisx[:,0])
# 18- Üretilen matrisin her bir elemanının karesini alınız.
print("****Soru 18****")
print(matrisx**2)
# 19- Üretilen matris elemanlarının hangisi pozitif çift sayıdır ? 
#     Aralığı (-50,+50) arasında yapınız.
print("****Soru 19****")
matrix = np.random.randint(-50,50,15).reshape(3,5)
print(matrix)
ciftler = matrix[matrix%2 == 0]
pozitifMi = ciftler[ciftler > 0]
print(pozitifMi)

