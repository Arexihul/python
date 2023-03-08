def notları_oku():
     with open("notlar.txt","r",encoding="utf-8") as file2:
          return file2.read()


def notları_gir():
     ad = input("Ad: ")
     soyad = input("Soyad: ")
     not1 = float(input("Not 1: "))
     not2 = float(input("Not 2: "))
     not3 = float(input("Not 3: "))

     ort = (not1+not2+not3)/3

     if ort>=90 and ort<=100:
          harf = "AA"
     elif ort>=85 and ort<90:
          harf = "BA"
     elif ort>=80 and ort<85:
          harf = "BB"
     elif ort>=75 and ort<80:
          harf = "CB"
     elif ort>=70 and ort<75:
          harf = "CC"
     elif ort>=65 and ort<70:
          harf = "DC"
     elif ort>=60 and ort<65:
          harf = "DD"
     elif ort>=50 and ort<60:
          harf = "FD"
     else:
          harf = "FF"

     with open("notlar.txt", "a", encoding="utf-8") as file:
          file.write(f"--{ad} {soyad}--\nNotlar: {not1}, {not2}, {not3}\nOrtalama: {ort}\nNot: {harf}\n")


from shutil import copyfile

def notları_kaydet():
     with open("notları_kaydet.txt","a",encoding="utf-8"):
          copyfile("notlar.txt", "notları_kaydet.txt")


while True:
     secim = input("1=> Notları Oku\n2=> Notları Gir\n3=> Notları Kaydet\n4=> Uygulamadan Çıkış\n")

     if secim == "1":
          print(notları_oku(),end="")
     elif secim == "2":
          print(notları_gir())
     elif secim == "3":
          print(notları_kaydet())
     else:
          break









