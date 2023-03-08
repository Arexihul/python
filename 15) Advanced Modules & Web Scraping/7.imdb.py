import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"

# response = requests.get(url)

# print(response)            # => <Response [200]>
# print(response.content)  # => sayfa kaynağı

html = requests.get(url).content
soup =BeautifulSoup(html, "html.parser") 

liste = soup.find("tbody", {"class":"lister-list"}).find_all("tr",limit=25)
# print(liste)

count = 1
for tr in liste:
     title = tr.find("td",{"class":"titleColumn"}).find("a").text
     year = tr.find("td",{"class":"titleColumn"}).find("span").text   # .strip("()") eklersek yıl bilgisi parantezsiz gösterilir
     rating = tr.find("td",{"class":"ratingColumn imdbRating"}).find("strong").text

     print(count,title,year,rating)
     count += 1 