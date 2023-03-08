""""
Girilen bir sayının asal olup olmadığını bulun.
     Asal sayı 1 ve kendisi hariç başka böleni olmayan sayılara denir.
"""

sayi = int(input("Sayı giriniz: "))
asalmi = True

if sayi == 1:
     asalmi = False

for x in range(2,sayi):
     if sayi%x == 0:
          asalmi = False
          break

if asalmi:
     print(f"{sayi} sayısı asaldır")
else:
     print(f"{sayi} sayısı asal değildir")

