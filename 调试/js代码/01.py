# @author       ：小青年
# @ProjectName  ：py_web_qianchengdai
# @Name         ：01
# @time         ：2020/3/22 18:11 

import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get("https://www.baidu.com/")
ele=driver.find_element_by_id("kw")
ele.send_keys('hhhhh')
ele1=driver.find_element_by_id("su")
ele1.click()