def sayHello():
     print("Hello")

sayHello()

def sayHello2(name = "User"):
     print("Hello " + name)

sayHello2()
sayHello2("Eyüp")

def sayHello3(name = "User"):
     return "Hello " + name

msg = sayHello3("Nihal")

print(msg)

def total(num1, num2):
     return num1 + num2

result = total(10,20)

print(result)

def yasHesapla(dogumYili):
     return 2020 - dogumYili

ageEyüp = yasHesapla(2001)
ageNihal = yasHesapla(2010)

print(ageEyüp, ageNihal)

def EmekliligeKacYilKaldi(dogumYili, isim):
     """
     DOCSTRING: Dogum yiliniza göre emekliliginize kac yil kaldi
     INPUT: Dogum yili
     OUTPUT: Hesaplana yil bilgisi 
     """
     yas = yasHesapla(dogumYili)
     emeklilik = 65 - yas

     if emeklilik > 0:
          print(f"Emekliliğinize {emeklilik} yıl kaldı")
     else:
          print("Zaten emekli oldunuz")

EmekliligeKacYilKaldi(1983, "Ali")
EmekliligeKacYilKaldi(1950, "Ahmet")
EmekliligeKacYilKaldi(1962, "Yağmur")

print(help(EmekliligeKacYilKaldi))

liste = [1,2,3]

print(help(list.append))

