from InstagramUserInfo import username, password
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

class Instagram:
     def __init__(self, username, password):
          self.username = username
          self.password = password
          self.browser = webdriver.Chrome()

     def signIn(self):
          self.browser.get("https://www.instagram.com/accounts/login/")
          time.sleep(2)

          usernameInput = self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input')
          passwordInput = self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input')

          usernameInput.send_keys(self.username)
          passwordInput.send_keys(self.password)
          passwordInput.send_keys(Keys.ENTER)
          time.sleep(2)

          # self.browser.get('https://www.instagram.com/')
          # time.sleep(2)

     def getFollowers(self, maximum):
          time.sleep(2)
          self.browser.get(f"https://www.instagram.com/{self.username}")
          time.sleep(2)
          self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
          time.sleep(2)

          dialog = self.browser.find_element_by_css_selector("div[role=dialog] ul")
          followerCount = len(dialog.find_elements_by_css_selector("li"))

          print(f"First Count: {followerCount}")

          action = webdriver.ActionChains(self.browser)     # aksiyonun gerçekleştirileceği yer

          while followerCount < maximum:
               dialog.click()
               action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()    # Space tuşuna basmış olduk
               time.sleep(2)
               
               newCount = len(dialog.find_elements_by_css_selector("li"))

               if followerCount != newCount:
                    followerCount = newCount
                    print(f"Updated Count: {newCount}")
                    time.sleep(2)
               else:
                    break

          followers = dialog.find_elements_by_css_selector("li")

          followerList = []
          i = 0
          for user in followers:
               link = user.find_element_by_tag_name("a").get_attribute("href")
               followerList.append(link)
               i+=1
               if i == maximum:
                    break

          with open("followers.txt", "w", encoding="UTF-8") as dosya:
               for item in followerList:
                    dosya.write(item + "\n")


     def followUser(self, follow):
          time.sleep(2)
          self.browser.get(f"https://www.instagram.com/{follow}")

          followButton = self.browser.find_element_by_tag_name('button')

          if followButton.text == "Takip Et":
               followButton.click()
          else:
               print("Zaten takiptesiniz")

     def unFollowUser(self, unfollow):
          time.sleep(2)
          self.browser.get(f"https://www.instagram.com/{unfollow}")
          time.sleep(2)

          unf = self.browser.find_element_by_css_selector("header section button")

          if unf.text == "Mesaj Gönder":
               self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/span/span[1]/button').click()
               time.sleep(2)

               self.browser.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[1]').click()
               time.sleep(2)
          elif unf.text == "Takip Et":
               print("Zaten takip etmiyorsunuz")

          self.browser.close()


test = Instagram(username, password)

test.signIn()
test.getFollowers(15)
# test.unFollowUser("lolturkiye")

