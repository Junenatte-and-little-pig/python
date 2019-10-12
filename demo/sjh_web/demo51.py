# -*- encoding: utf-8 -*-
from selenium import webdriver
import time

# driver=webdriver.Firefox(executable_path=r"D:\Program Files (x86)\Mozilla Firefox\geckodriver.exe")
driver = webdriver.Firefox()  # geckodriver.exe放至python安装目录下
driver.get("http://www.baidu.com")
# print(driver.page_source)
print(driver.name)
print(driver.current_url)
print(driver.title)
print(driver.get_cookies())
print(
    driver.find_element_by_id('kw'))  # same as driver.find_element(By.ID, 'kw')
driver.find_element_by_id('kw').send_keys('selenium')
driver.find_element_by_id('su').click()
time.sleep(2)
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.close()
