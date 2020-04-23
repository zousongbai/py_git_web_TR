# @author       ：小青年
# @ProjectName  ：py_web_TR_boss
# @Name         ：01
# @time         ：2020/4/3 16:39 

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait # 导入计时器
from selenium.webdriver.support import expected_conditions as EC
from page.merchant_page import MerchantPage
from locator import merchant_manage_locator

driver=webdriver.Chrome()
driver.implicitly_wait(30)
driver.get("http://boss.test.tongrong365.net/")
driver.maximize_window()
# 请输入登录账号
login_username_elem=WebDriverWait(driver,30).until(EC.visibility_of_element_located((By.ID,"userName")))
# input_login_elem=driver.find_element_by_id("loginname")
login_username_elem.send_keys("admin")

# 请输入登录密码
login_passwd_elem=driver.find_element_by_id("userPassword")
login_passwd_elem.send_keys("a123456")

# submit方式提交
# login_passwd_elem.submit()
# 定位：登陆按钮
button_elem=driver.find_element_by_xpath("//button[contains(@class,'btn-primary')]")
# 点击登陆
button_elem.click()

# 定位：导航栏商户管理
nav_elem=driver.find_element_by_xpath("//div[@id='navbar']//li[9]//a[1]")
nav_elem.click()
time.sleep(2)

# 定位：菜单栏商户管理
menu_elem=driver.find_element_by_xpath("//span[text()='商户管理']")
menu_elem.click()
time.sleep(6)

# # 定位：新增按钮
# add_button_elem=driver.find_element_by_xpath("//a[text()='新增']")
# add_button_elem.click()
#
# # 输入商户名称
# merchant_name_elem=driver.find_element_by_id('form-field-merchantName')
# merchant_name_elem.send_keys("快牛")

# # 选择下拉框
# # 步骤一：定位select元素
# select_elem=driver.find_element_by_xpath("//select[@id='form-field-merchantType']")
# # 步骤二：初始化select类，将参数传入到类里面
# select=Select(select_elem)
# # 步骤三：选择，三种方式
# # 1'通过value方式定位：select.select_by_value('doc') # 使用select对象
# # 2'通过text文本定位：select.select_by_visible_text('微软 Word (.doc)')
# # 3'通过index索引定位：select.select_by_index(1) # 索引从0开始
# select.select_by_value('2') # 选择债权转让方

# # 点击确定
# confirm_button_elem=driver.find_element_by_id("createMerchant")
# confirm_button_elem.click()
# time.sleep(2)
# error_msg_elem=driver.find_element_by_xpath("//div[@class='jBox-text-left']")
# ac=error_msg_elem.text
# print(ac)

# # 点击下一页
# next_page_elem=driver.find_element_by_xpath("//li[@id='table_next']//a")
# next_page_elem.click()
# time.sleep(6)

# 查找页码的最后一页
el=driver.find_element_by_xpath("//ul[@class='pagination']/li[last()-1]/a")
print(type(el))
print(el)

# # 查找有多少页
# page_num_elem=driver.find_elements_by_xpath("//ul[@class='pagination']/li")
# print(page_num_elem)
#
# # 最后一页
# last_page_num_elem=page_num_elem[-2]
# print(type(last_page_num_elem))
# print(last_page_num_elem)

# 点击最后一页
el.click()
time.sleep(6)

# 点击新增的商户对应的修改按钮
# e2=driver.find_element_by_xpath(merchant_manage_locator.revise_locator)
e2=driver.find_element_by_xpath(merchant_manage_locator.revise_locator)
e2.click()
time.sleep(6)