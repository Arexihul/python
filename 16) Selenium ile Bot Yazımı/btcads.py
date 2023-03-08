import time
from selenium import webdriver
import random

driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
driver.get('https://web.telegram.org/#/login')
time.sleep(3) # Let the user actually see something!
phone = driver.find_element_by_xpath('//*[@id="ng-app"]/body/div[1]/div/div[2]/div[2]/form/div[2]/div[2]/input')
phone.send_keys('5535224323')
phone.submit()
time.sleep(3) # Let the user actually see something!

ok = driver.find_element_by_xpath('//*[@id="ng-app"]/body/div[5]/div[2]/div/div/div[2]/button[2]')
time.sleep(2)
ok.click()
time.sleep(30)
driver.get('https://web.telegram.org/#/im?p=@BTC_Ads_nl_bot')
time.sleep(5)
view = driver.find_element_by_xpath('//*[@id="ng-app"]/body/div[1]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[2]/div[21]/div[2]/div/div/div[2]/div/div[4]/div/div/div[1]/div/button')

while(True):
    view.click()
    rand = random.uniform(30,35)
    time.sleep(rand)


# driver.quit()