import time
from selenium import webdriver

from selenium.webdriver.common.by import By
driver =webdriver.Chrome()
driver.maximize_window()
driver.get('http://www.baidu.com')

driver.quit()

