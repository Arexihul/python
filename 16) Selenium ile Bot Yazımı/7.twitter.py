from twitterUserInfo import username, password
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

class Twitter:
     def __init__(self, username, password):
          self.username = username
          self.password = password
          self.browserProfile = webdriver.ChromeOptions()
          self.browserProfile.add_experimental_option("prefs", {"intl.accept_languages": "en, en_US"})
          self.browser = webdriver.Chrome("chromedriver.exe", options=self.browserProfile)   
          # Chrome ingilizce açılacak
          
     def signIn(self):
          self.browser.get("https://twitter.com/login")
          time.sleep(2)
          self.browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div[2]/div/input').send_keys(self.username)
          self.browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input').send_keys(self.password)
          self.browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input').send_keys(Keys.ENTER)
          time.sleep(2)

     def search(self, hashtag):
          searchBtn = self.browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div[2]/input')
          searchBtn.send_keys(hashtag)
          searchBtn.send_keys(Keys.ENTER)
          time.sleep(2)

          tweets = []

          elements = self.browser.find_elements_by_xpath("//div[@data-testid='tweet']/div[2]/div[2]/div[1]")
          time.sleep(2)
          print(f"Count: {len(elements)}")

          for element in elements:
               tweets.append(element.text)

          loopCounter = 0
          lastHeight = self.browser.execute_script("return document.documentElement.scrollHeight")

          while True:
               if loopCounter > 3:
                    break
               self.browser.execute_script("window.scrollTo(0,document.documentElement.scrollHeight)")
               time.sleep(2)

               newHeight = self.browser.execute_script("return document.documentElement.scrollHeight")
               if lastHeight == newHeight:
                    break
               lastHeight = newHeight
               loopCounter += 1

               elements = self.browser.find_elements_by_xpath("//div[@data-testid='tweet']/div[2]/div[2]/div[1]")
               time.sleep(2)
               print(f"Count: {len(elements)}")

               for element in elements:
                    tweets.append(element.text)

          count = 1
          with open("tweets.txt","w",encoding="utf-8") as dosya:
               for tweet in tweets:
                    dosya.write(f"{count} => {tweet}\n")
                    count += 1


test = Twitter(username, password)

test.signIn()
test.search("ayasofya")

