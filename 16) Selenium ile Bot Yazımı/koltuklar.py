from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

class Koltuk:
     def __init__(self):
          self.browser = webdriver.Chrome()

     def getInfo(self):
          products = self.browser.find_elements_by_class_name("product-name")

          prices = self.browser.find_elements_by_class_name("last-price")

          links = self.browser.find_elements_by_css_selector(".product-link a")

          x = 0
          y = 0

          while x < len(products):
               with open("koltuklar.txt", "a", encoding="UTF-8") as dosya:
                    dosya.write(f"{products[x].text} => Fiyat: {prices[x].text} => Ürün Linki: {links[y].get_attribute('href')}\n")
               x+=1
               y+=2

     def yolla(self):
          self.browser.get("https://www.vivense.com/koltuk-takimlari-mobilyalari.html")
          time.sleep(2)
          # self.browser.find_element_by_xpath('//*[@id="searchForm"]/div/div/div[1]/ul/li[3]/a').click()
          # self.browser.find_element_by_xpath('//*[@id="searchForm"]/div/div/div[2]/div[3]/div/ul/li[1]/div/label').click()
          # self.browser.find_element_by_xpath('//*[@id="searchForm"]/div/div/div[2]/div[6]/a').click()

          self.getInfo()

          pages = self.browser.find_elements_by_css_selector(".pagination_ul li")

          i = 2

          while i <= len(pages):
               self.browser.get(f"https://www.vivense.com/koltuk-takimlari-mobilyalari.html?page={i}")
               time.sleep(1)
               i += 1

               self.getInfo()

          self.browser.close()


test = Koltuk()

test.yolla()

