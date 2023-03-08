from githubUserInfo import username, password
from selenium import webdriver
import time


class Github:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.browser = webdriver.Chrome()
        self.followers = []

    def signIn(self):
        self.browser.get("https://github.com/login")

        usernameinput = self.browser.find_element_by_xpath("//*[@id='login_field']")
        passwordinput = self.browser.find_element_by_xpath("//*[@id='password']")

        usernameinput.send_keys(self.username)
        passwordinput.send_keys(self.password)

        self.browser.find_element_by_xpath('//*[@id="login"]/form/div[4]/input[9]').click()

    def addListFollowers(self):
        items = self.browser.find_elements_by_css_selector(".d-table.table-fixed")

        for i in items:
            self.followers.append(i.find_element_by_css_selector(".link-gray").text)

    def getFollowers(self,username = username):
        self.browser.get(f"https://github.com/{username}?tab=followers")

        self.addListFollowers()

        while True:
            links = self.browser.find_element_by_class_name("pagination").find_elements_by_tag_name("a")

            if len(links) == 1:
                if links[0].text == "Next":
                    links[0].click()
                    self.addListFollowers()
                else:
                    break
            else:
                for link in links:
                    if link.text == "Next":
                        link.click()
                        self.addListFollowers()
                    else:
                        continue


test = Github(username, password)

test.signIn()

test.getFollowers("sadikturan")

print(len(test.followers))
print(test.followers)

