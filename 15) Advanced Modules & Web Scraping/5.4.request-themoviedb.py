# themoviedb.org => film ve dizi arşivi
# themoviedb 'nin sunduğu apiyi kullanınız
# Anahtar kelimeye göre arama
# En popüler film listesi
# Viyondaki film listesi

import requests

class Movies:
     def __init__(self):
          pass

     def search(self, query):
          response = requests.get(f"https://api.themoviedb.org/3/search/company?api_key=b6dfaa542e81c3ef828c49627b163c45&query={query}&page=1")
          return response.json()

     def getPopular(self):
          response = requests.get("https://api.themoviedb.org/3/movie/popular?api_key=b6dfaa542e81c3ef828c49627b163c45&language=en-US&page=1")
          return response.json()

     def getNowPlaying(self):
          response = requests.get("https://api.themoviedb.org/3/movie/now_playing?api_key=b6dfaa542e81c3ef828c49627b163c45&language=en-US&page=1")
          return response.json()

test = Movies()

while True:
     secim = input("1- Film Ara\n2- Popüler Filmler\n3- Vizyondaki filmler\n4- Çıkış\nSeçiminiz: ")

     if secim == "4":
          break
     elif secim == "1":
          arama = input("Anahtar kelime giriniz: ")
          result = test.search(arama)
          # print(result)
          sayfalar = result["total_pages"]
          filmler = result["total_results"]
          print("Sayfa sayısı: " + str(sayfalar))
          print("Film sayısı: " + str(filmler))

          page = 1
          while page <= sayfalar:
               response = requests.get(f"https://api.themoviedb.org/3/search/company?api_key=b6dfaa542e81c3ef828c49627b163c45&query={arama}&page={page}")
               result = response.json()

               results = result["results"]
               for i in results:
                              print(i["name"])
               page += 1      
     elif secim == "2":
          result = test.getPopular()
          # print(result)

          sayfalar = result["total_pages"]
          filmler = result["total_results"]
          print("Sayfa sayısı: " + str(sayfalar))
          print("Film sayısı: " + str(filmler))

          results = result["results"]
          for i in results:
               print(f'Başlık: {i["original_title"]}     Popülerlik: {i["popularity"]}     Tarih: {i["release_date"]}')
     elif secim == "3":
          result = test.getNowPlaying()
          # print(result)

          sayfalar = result["total_pages"]
          filmler = result["total_results"]
          print("Sayfa sayısı: " + str(sayfalar))
          print("Film sayısı: " + str(filmler))

          results = result["results"]
          for i in results:
               print(f'Başlık: {i["original_title"]}     Popülerlik: {i["popularity"]}     Tarih: {i["release_date"]}')
     else:
          print("Hatalı bilgi girdiniz.")

