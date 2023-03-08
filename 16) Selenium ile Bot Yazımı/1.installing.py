# Selenium bir web otomasyon kütüphanesidir.
# Selenium ile bir web sitesini ziyaret edip etkileşimde bulunabilirsiniz.

# terminal => pip install selenium 

from selenium import webdriver

driver = webdriver.Chrome()

url = "http://sadikturan.com"

driver.get(url)

