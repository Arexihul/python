'''
   1-100 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile
   buldurmaya çalışın. (hak = 5)
   ** "random modülü" için "python random" şeklinde arama yapın.
   ** 100 üzerinden puanlama yapın. Her soru 20 puan.
   ** Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı 
      üzerinden hesaplansın.
'''

import random

sayi = random.randint(1,100)
print("Merhaba.\nBu oyunumuzda 1 ile 100 arasında rastgele belirlediğimiz bir sayıyı tahmin etmeye çalışcaksınız.\nHer tahmininizden sonra sayının daha yüksek mi yoksa alçak mı olduğu hakkında sizi bilgilendireceğiz.\nAmacınız mümkün olduğunca az hak kullanarak sayıyı tahmin etmek.\nNe kadar çok hak kullanırsanız puanınız o kadar azalır.\nKendi belirlediğiniz hak sayısına göre her yanlış tahminde puanınız 100 üzerinden bir miktar düşülecektir.\nPuanının 0'ın altına düştüğünde ise oyun sona erecektir.")
hak = int(input("Kaç hakkınızın olmasını istersiniz: "))
gir = int(input("Tahmininiz: "))
puan = 100 - 100/hak

while not gir == sayi:
     if puan <= 0:
          break
     elif gir>sayi:
          gir = int(input("Aşağı: "))
          if not gir == sayi:
               puan -= 100/hak
     elif gir<sayi:
          gir = int(input("Yukarı: "))
          if not gir == sayi:
               puan -= 100/hak

if gir == sayi:
     print(f"Tebrikler sayıyı buldunuz ve puanınız {puan}")

if puan <= 0:
     print(f"Üzgünüm hakkınız bitti. Sayı {sayi} idi.")


input()