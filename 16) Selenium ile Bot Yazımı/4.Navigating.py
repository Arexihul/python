"""
Locating Elements

https://selenium-python.readthedocs.io/locating-elements.html

find_element_by_id
find_element_by_name
find_element_by_xpath
find_element_by_link_text
find_element_by_partial_link_text
find_element_by_tag_name
find_element_by_class_name
find_element_by_css_selector

To find multiple elements (these methods will return a list):

find_elements_by_name
find_elements_by_xpath
find_elements_by_link_text
find_elements_by_partial_link_text
find_elements_by_tag_name
find_elements_by_class_name
find_elements_by_css_selector
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys   # enter,space gibi tuşları çalıştırmaya yarar
import time

driver = webdriver.Chrome()

url = "http://github.com"
driver.get(url)


searchInput = driver.find_element_by_xpath("/html/body/div[1]/header/div/div[2]/div[2]/div/div/div/form/label/input[1]")
time.sleep(1)
searchInput.send_keys("python")
time.sleep(1)
searchInput.send_keys(Keys.ENTER)
time.sleep(2)

result = driver.find_elements_by_xpath("//*[@id='js-pjax-container']/div/div[3]/div/ul/li[1]/div[2]/div[1]/a")

for element in result:
     print(element.text)

driver.close()

# driver.page_source  => sayfa kaynağını getirir
