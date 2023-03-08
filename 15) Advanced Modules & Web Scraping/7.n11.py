import requests
from bs4 import BeautifulSoup

url = "https://www.n11.com/bilgisayar/dizustu-bilgisayar"

html = requests.get(url).content
soup = BeautifulSoup(html,"html.parser")

# print(soup)

liste = soup.find("section",{"class":"group listingGroup resultListGroup import-search-view"}).find("div",{"id":"view"}).find("ul").find_all("li",{"class":"column"})

for laptop in liste:
     name = laptop.find("div",{"class":"columnContent"}).find("div",{"class":"pro"}).find("a").find("h3").text.strip()
     price = laptop.find("div",{"class":"columnContent"}).find("div",{"class":"proDetail"}).find("a",{"class":"newPrice"}).text.strip().strip("TL").strip()
     print(f"{name} => {price} TL")

"""
liste = soup.find_all("li",{"class":"column"})

for li in liste:
    name = li.div.a.h3.text.strip()
    link = li.div.a.get("href")
    oldprice = li.find("div",{"class":"proDetail"}).find_all("a")[0].text.strip().strip('TL')
    newprice = li.find("div",{"class":"proDetail"}).find_all("a")[1].text.strip().strip('TL')

    print(f"name: {name} link: {link} old price: {oldprice} new price: {newprice}")   
""" 
     
