from bs4 import BeautifulSoup

html_doc = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
     <title>My First Web Page</title>
</head>
<body>

<h1 id="header">
          Python Kursu
     </h1>

     <div class="grup1">
          <h2>
               Programlama
          </h2>
          <ul>      <!-- liste -->
               <li>Menü 1</li>     <!-- liste elemanları -->
               <li>Menü 2</li>
               <li>Menü 3</li>
          </ul>
     </div>

     <div class="grup2">
          <h2>
               Modüller
          </h2>
          <ul>
               <li>Menü 1</li>
               <li>Menü 2</li>
               <li>Menü 3</li>
          </ul>
     </div>
     <img src="ornek.jpg" alt="">

     <a class="sister" href="http://example1.com/elsie" id="link1">Elsie</a>
     <a class="sister" href="http://example2.com/elsie" id="link1">Elsie</a>
     <a class="sister" href="http://example3.com/elsie" id="link1">Elsie</a>

</body>
</html>
"""

soup = BeautifulSoup(html_doc, "html.parser")

result = soup.prettify()      # Karışık olan dökümanı düzenler
result = soup.title      # title etiketli kısım gelir
result = soup.head       # head kısmı gelir
result = soup.body       # body kısmı gelir

result = soup.title.name      # title etiketinin ismi gelir
result = soup.title.string    # title içindeki string gelir

result = soup.h1    # h1 etiketli kısım gelir
result = soup.h2    # ilk h2 etiketli kısım gelir
result = soup.h2.name    # etiketin adı (h2) gelir
result = soup.h2.string    # h2 etiketi içindeki string gelir

result = soup.find_all("h2")       # Dökümandaki tüm h2 etiketli kısımları liste içinde getirir
result = soup.find_all("h2")[0]    # Listeden ilk h2'yi getirir
result = soup.find_all("h2")[1]    # Listeden ikinci h2'yi getirir

result = soup.div        # İlk div gelir
result = soup.find_all("div")[1]        # 2. div gelir
result = soup.find_all("div")[1].ul        # 2. div altındaki ul etiketli kısım gelir
result = soup.find_all("div")[1].ul.li        # 2. div altındaki ul etiketli kısım altındaki ilk li gelir
result = soup.find_all("div")[1].ul.find_all("li")        # 2. div altındaki ul etiketli kısım altındaki li'ler gelir

result = soup.div.findChildren()        # İlk div altındaki her şeyi getirir
result = soup.div.findNextSibling()     # İkinci div altındaki her şeyi getirir
result = soup.div.findNextSibling().findPreviousSibling()     # İlk div altındaki her şeyi getirir

result = soup.find_all("a")

for link in result:
     print(link.get("href"))

print(result)

