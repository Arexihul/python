class Soru:
     def __init__(self, metin, siklar, cevap):
          self.metin = metin
          self.siklar = siklar
          self.cevap = cevap


class Test:
     def __init__(self, sorular):
          self.sorular = sorular
          self.puan = 0
          self.index = 0
          print(f"Test {len(sorular)} sorudan oluşmaktadır ve her soru 20 puandır. Başarılar!")

     def soruyuAl(self):
          return self.sorular[self.index]

     def soruyuYaz(self):
          soru = self.soruyuAl()
          print(f"Soru {self.index + 1}: {soru.metin}")

          for s in soru.siklar:
               print(s)

          cevap = input("Cevabınız: ")
          if cevap == soru.cevap:
               self.puan += 20
          self.index += 1

          self.devamEt()

     def devamEt(self):
          if len(sorular) == self.index:
               print(f"Puanınız: {self.puan}")
          else:
               self.soruyuYaz()


s1 = Soru("En iyi programlama dili hangisidir?", ["a) C#", "b) Python", "c) Javascript", "d) Java"], "b")
s2 = Soru("En popüler programlama dili hangisidir?", ["a) C#", "b) Javascript", "c) Java", "d) Python"], "d")
s3 = Soru("En çok kazandıran programlama dili hangisidir?", ["a) Python", "b) Java","c) C#", "d) Javascript"], "a")
s4 = Soru("En basit programlama dili hangisidir?", ["a) Java", "b) Javascript","c) C#", "d) Python"], "d") 
s5 = Soru("En temel programlama dili hangisidir?", ["a) Javascript", "b) C#","c) Python", "d) Java"], "c") 
sorular = [s1,s2,s3,s4,s5]    

test = Test(sorular)

test.soruyuYaz()

