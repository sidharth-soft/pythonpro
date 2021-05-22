from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Edge(executable_path="D:\msedgedriver.exe")
driver.get('http://thetestingworld.com/testings')
ob = Select(driver.find_element_by_name('sex'))
time .sleep(10)
driver.maximize_window()
# ob.select_by_index(1)
ob.select_by_value('1')
B = Select(driver.find_element_by_id('countryId'))
B.select_by_value('101')
driver.close()

