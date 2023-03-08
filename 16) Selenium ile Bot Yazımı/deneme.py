from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()

time.sleep(2)

driver.get("https://discord.com/channels/912459806571393074/914144919998836746")
time.sleep(30)
message = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/main/form/div[1]/div/div/div[1]/div/div[1]/input')
message.send_keys('hi everyone')
time.sleep(2)
message.send_keys('hi everyone')
time.sleep(2)
message.send_keys('hi everyone')
time.sleep(2)
