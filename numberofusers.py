
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
#driver.get("http://www.python.org")
driver.get("http://admin:Chennaisuperkings7@routerlogin.net/")

#a = driver.find_element_by_id("AttachedDevices-condition")

driver.switch_to.frame("page")

b = driver.page_source

result = b.find('<span id="AttachedDevices-condition" class="Condition-normal">')

driver.implicitly_wait(15)

driver.quit()
#Result gives the postion of the span id
