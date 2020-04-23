# @author       ：小青年
# @ProjectName  ：py_web_TR_boss
# @Name         ：test_login
# @time         ：2020/4/3 11:14
import time
import unittest
import ddt
import os
from page.login_page import LoginPage
from page.user_page import UserPage
from data.login_data import login_data_success
from selenium import webdriver
from common.contants import conf_dir
from common.read_conf import MyConf
url_conf_filename=os.path.join(conf_dir,'url_conf.ini')

@ddt.ddt
class TestLogin(unittest.TestCase):
    url=MyConf(url_conf_filename).get_str('url','url_login')
    def setUp(self):
        self.driver=webdriver.Chrome()
        # self.driver.get(self.url)
        self.driver.maximize_window()
        # 设置隐式等待
        self.driver.implicitly_wait(30)

        # # 初始化要用到的页面
        self.login_page = LoginPage(self.driver)
        self.user_page=UserPage(self.driver)
    def tearDown(self):
        # self.driver.quit()
        pass
    @ddt.data(*login_data_success)
    def test_login(self,test_data_success):

        # 步骤一：输入手机号和密码，登录
        self.login_page.login(test_data_success['username'],test_data_success['pwd'])
        # time.sleep(2)
        # 步骤二：获取实际结果
        actual=self.user_page.get_username_text().text

        # 步骤三：断言
        self.assertEqual(actual,test_data_success['expected'])
# if __name__ == '__main__':
