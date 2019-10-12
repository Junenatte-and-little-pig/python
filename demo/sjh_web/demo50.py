# -*- encoding: utf-8 -*-
from selenium import webdriver
import time

# driver=webdriver.Firefox(executable_path=r"D:\Program Files (x86)\Mozilla Firefox\geckodriver.exe")
driver = webdriver.Firefox()  # geckodriver.exe放至python安装目录下
driver.get("http://www.baidu.com")
print(driver.title)
time.sleep(5)
driver.close()