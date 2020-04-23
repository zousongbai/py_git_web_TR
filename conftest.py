# @author       ：小青年
# @ProjectName  ：py_web_TR_boss
# @Name         ：conftest
# @time         ：2020/4/22 10:06
import os

import pytest
from selenium import webdriver

from page.login_page import LoginPage
from page.user_page import UserPage

@pytest.fixture()
def manage_driver():
    """管理浏览器"""
    # 步骤一：初始化浏览器
    driver = webdriver.Chrome()
    # 浏览器最大化
    driver.maximize_window()

    # 步骤二：初始化页面：
    # 申明login_page相关的信息
    login_page = LoginPage(driver)
    user_page=UserPage(driver)

    # 步骤三：通过yield保存manage_browser返回过来的参数
    yield driver, login_page,user_page

    # 步骤四：关闭浏览器
    driver.quit()
