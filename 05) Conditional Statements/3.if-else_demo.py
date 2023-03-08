# 1- Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme 
#    durumunu kontrol ediniz. Ehliyet alma koşulu en az 18 ve eğitim durumu 
#    lise ya da üniversite olmalıdır. 

"""
name = input("İsminiz: ")
age = int(input("Yaşınız: "))
education = input("Eğitim durumunuz: ")

if age >= 18:
     if education == "lise" or education == "üniversite":
          print("Ehliyet alma koşullarını sağlıyorsunuz")
     else:
          print("Eğitim durumunuz yetersiz")
elif age < 18 and not education == "lise" or education == "üniversite":
     print("Yaşınız ve eğitim durumunuz yetersiz")
else:
     print("Yaşınız yetersiz")
"""

# 2- Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre
#    not aralığına karşılık gelen not bilgisini yazdırınız.
#    0 -24  => 0
#    25-44  => 1
#    45-54  => 2
#    55-69  => 3
#    70-84  => 4
#    85-100 => 5

"""
yazili1 = float(input("1. yazılı notunuz: "))
yazili2 = float(input("2. yazılı notunuz: "))
sozlu = float(input("Sözlü notunuz: "))
ort = (yazili1 + yazili2 + sozlu) / 3

if ort >= 0 and ort < 25:
     print(f"Ortalamanız {ort} ve not bilginiz 0")
elif ort > 25 and ort < 45:
     print(f"Ortalamanız {ort} ve not bilginiz 1")
elif ort > 45 and ort < 55:
     print(f"Ortalamanız {ort} ve not bilginiz 2")
elif ort > 55 and ort < 70:
     print(f"Ortalamanız {ort} ve not bilginiz 3")
elif ort > 70 and ort < 85:
     print(f"Ortalamanız {ort} ve not bilginiz 4")
elif ort > 85 and ort < 100:
     print(f"Ortalamanız {ort} ve not bilginiz 5")
else:
     print("Yanlış bilgi girdiniz.")
"""

# 3- Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere
#    göre hesaplayınız.
#    1. Bakım => 1. yıl     
#    2. Bakım => 2. yıl      
#    3. Bakım => 3. yıl     
#    ** Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayınız..
#    *** datetime modülünü kullanmanız gerekiyor.  
#    (simdi) - (2018/8/1) => gün

import datetime

date = input('Aracınız hangi tarihte trafiğe çıktı (2019/8/9): ')
date = date.split("/")

now = datetime.datetime.now()
datex = datetime.datetime(int(date[0]),int(date[1]),int(date[2]))

days = (now - datex).days

if days > 0 and days <= 365:
     print("1. servis aralığı")
elif days > 365 and days <= 365*2:
     print("2. servis aralığı")
elif days > 365*2 and days <= 365*3:
     print("3. servis aralığı")
else:
     print("Hatalı süre")

