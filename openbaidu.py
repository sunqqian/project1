import time
from selenium import webdriver
#导入By模块
from selenium.webdriver.common.by import By
#选择浏览器
driver =webdriver.Chrome()
#全屏
driver.maximize_window()
#进入百度网站
driver.get('http://www.baidu.com')

#通过find_element定位输入框
#driver.find_element(By.ID, 'kw').send_keys('pyhton')
#driver.find_element(By.XPATH,"//*[@id='kw']").send_keys("pyhton")

#点击
#driver.find_element(By.ID, 'su').click()
#driver.find_element(By.XPATH,"//*[@id='su']").click()
driver.quit()

