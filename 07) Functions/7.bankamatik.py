# Bankamatik Uygulaması

SadikHesap = {
     "ad" : "Sadık Turan",
     "hesapno" : "12345678",
     "bakiye" : 4000,
     "ekhesap" : 2000
}

AliHesap = {
     "ad" : "Ali Turan",
     "hesapno" : "87654321",
     "bakiye" : 3000,
     "ekhesap" : 1000
}

def bakiyeSorgula(hesap):
     print(f"{hesap['hesapno']} nolu hesabınızda {hesap['bakiye']}TL bakiye bulunmaktadır. Ek hesap limitiniz ise {hesap['ekhesap']}TL'dir.")

def paracek(hesap, miktar):
     print(f"Merhaba {hesap['ad']}")

     total = hesap["bakiye"] + hesap["ekhesap"] 

     if hesap["bakiye"] >= miktar:
          hesap["bakiye"] -= miktar
          print(f"Paranızı alabilirsiniz.")
          bakiyeSorgula(hesap)

     elif total >= miktar:
          ek = input("Hesabınızda yeterli bakiye bulunmamaktadır. Ek hesabınızı kullanmak ister misiniz (Evet/Hayır): ")

          if ek == "Evet":
               hesap["ekhesap"] = total - miktar
               hesap["bakiye"] = 0
               
               print(f"Paranızı alabilirsiniz. Bakiyeniz tükenmiştir ve kalan ek hesap limitiniz {hesap['ekhesap']}TL'dir.")
          
          else:
               print("Ek hesabınızı kullanmak istemediğinizden dolayı para çekme işleminizi gerçekleştiremiyoruz.")
               bakiyeSorgula(hesap)
     else:
          print("Bakiyenizdeki ve hatta ek hesabınızdaki miktar çekmek istediğiniz paranın altında.")
          bakiyeSorgula(hesap)


paracek(SadikHesap, 7000)

