# -*- encoding: utf-8 -*-
from selenium import webdriver
import time

# driver=webdriver.Chrome(executable_path=r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
driver = webdriver.Chrome()  # chromedriver.exe放至python安装目录下
driver.get("http://www.baidu.com")
print(driver.title)
time.sleep(5)
driver.close()
