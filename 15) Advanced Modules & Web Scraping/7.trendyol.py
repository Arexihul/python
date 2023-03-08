import requests
from bs4 import BeautifulSoup

url = "https://www.trendyol.com/laptop/lenovo"

html = requests.get(url).content
soup = BeautifulSoup(html,"html.parser")

# print(soup)

liste = soup.find("div",{"class":"prdct-cntnr-wrppr"}).find_all("div",{"class":"p-card-wrppr add-to-bs-card"})

for i in liste:
     info = i.find("div",{"class":"p-card-chldrn-cntnr"}).find("a").find("div",{"class":"prdct-desc-cntnr-wrppr with-basket-button"})
     brand = info.find("div",{"class":"prdct-desc-cntnr"}).find("div",{"class":"prdct-desc-cntnr-ttl-w"}).find("span").text
     model = info.find("div",{"class":"prdct-desc-cntnr"}).find("div",{"class":"prdct-desc-cntnr-ttl-w"}).find("span",{"class":"prdct-desc-cntnr-name"}).text
     price = info.find("div",{"class":"product-price"}).find("div",{"class":"prc-box-sllng"}).text
     
     print(brand,model,price)
     