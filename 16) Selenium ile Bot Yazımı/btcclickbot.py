import time
from selenium import webdriver
import random
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
driver.maximize_window()
driver.get('https://web.telegram.org/#/login')
time.sleep(1) # Let the user actually see something!
phone = driver.find_element_by_xpath('//*[@id="ng-app"]/body/div[1]/div/div[2]/div[2]/form/div[2]/div[2]/input')
phone.send_keys('5535224323')
phone.submit()
time.sleep(1) # Let the user actually see something!

ok = driver.find_element_by_xpath('//*[@id="ng-app"]/body/div[5]/div[2]/div/div/div[2]/button[2]')
time.sleep(1)
ok.click()

time.sleep(15)
driver.get('https://web.telegram.org/#/im?p=@BitcoinClick_bot')
time.sleep(3)
# visit_sites = driver.find_element_by_xpath('//*[@id="ng-app"]/body/div[1]/div[2]/div/div[2]/div[3]/div/div[3]/div[2]/div/div/div/form/div[4]/div/div/div/div/div[1]/div/div[1]/div[1]/button')
# visit_sites.click()
# time.sleep(3)

go_to_website = driver.find_element_by_xpath('//*[@id="ng-app"]/body/div[1]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[2]/div[21]/div[2]/div/div/div[2]/div/div[4]/div/div/div[1]/div/a')
go_to_website.click()
time.sleep(1)
open_link = driver.find_element_by_xpath('//*[@id="ng-app"]/body/div[6]/div[2]/div/div/div[2]/button[2]')
open_link.click()
time.sleep(5)
window_name = driver.window_handles[0]
driver.switch_to.window(window_name=window_name)
time.sleep(7)
window_name = driver.window_handles[1]
driver.switch_to.window(window_name=window_name)
# time.sleep(1)
driver.close()

i = 24                                             
while(True):                                       
    time.sleep(3)                                  
    go_to_website = driver.find_element_by_xpath('//*[@id="ng-app"]/body/div[1]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[2]/div[24]/div/div/div/div[2]/div/div[4]/div/div/div[1]/div/a')
    go_to_website.click()
    time.sleep(1)
    open_link = driver.find_element_by_xpath('//*[@id="ng-app"]/body/div[6]/div[2]/div/div/div[2]/button[2]')
    open_link.click()
    time.sleep(5)
    window_name = driver.window_handles[0]
    driver.switch_to.window(window_name=window_name)
    time.sleep(7)
    window_name = driver.window_handles[1]
    driver.switch_to.window(window_name=window_name)
    time.sleep(1)
    driver.close()
    i +=3
    

# while(True):
#     view.click()
#     rand = random.uniform(30,35)
#     time.sleep(rand)

