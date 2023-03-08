from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
url = "https://web.telegram.org/#/im?p=@BTC_Ads_nl_bot"
driver.get(url)

phoneClick = driver.find_element_by_xpath('//*[@id="ng-app"]/body/div[1]/div/div[2]/div[2]/form/div[2]/div[2]/label')
time.sleep(2)
phoneClick.click()
time.sleep(2)
phoneInput = driver.find_element_by_xpath('//*[@id="ng-app"]/body/div[1]/div/div[2]/div[2]/form/div[2]/div[2]/input')
time.sleep(2)
phoneInput.send_keys("5535224323")


