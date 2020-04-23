# @author       ：小青年
# @ProjectName  ：py_web_TR_boss
# @Name         ：test_merchant_manage
# @time         ：2020/4/3 15:37
import time
import unittest
import os
import ddt
from selenium import webdriver
from common.contants import conf_dir
from common.read_conf import MyConf
from page.login_page import LoginPage
from page.user_page import UserPage
from data.login_data import login_data_success
from page.merchant_page import MerchantPage
from data.merchant_data import merchant_data_success,merchant_data_error


test_data_success=login_data_success[0]
url_conf_filename=os.path.join(conf_dir,'url_conf.ini')
@ddt.ddt
class TestMerchantManage(unittest.TestCase):
    url = MyConf(url_conf_filename).get_str('url', 'url_login')
    def setUp(self):
        """登录"""
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        self.driver.maximize_window()
        # 设置隐式等待
        self.driver.implicitly_wait(30)

        # # 初始化要用到的页面
        self.login_page = LoginPage(self.driver)
        self.user_page = UserPage(self.driver)
        self.merchant_manage_page = MerchantPage(self.driver)


        # 登录
        # 步骤一：输入手机号和密码，登录
        self.login_page.login(test_data_success['username'], test_data_success['pwd'])
        time.sleep(2)
        # 步骤二：获取实际结果
        actual = self.user_page.get_username_text().text

        # 步骤三：断言
        self.assertEqual(actual, test_data_success['expected'])
    def tearDown(self):
        self.driver.quit()

    @ddt.data(*merchant_data_success)
    def test_add_merchant_success(self,test_data_success):
        """新增商户成功"""
        self.merchant_manage_page.add_merchant(test_data_success['merchant_name'],
                                               test_data_success['organ_code'],
                                               test_data_success['lega_lName'],
                                               test_data_success['legal_Idcard'],
                                               test_data_success['merchant_type'])

        time.sleep(2)
        res_msg = self.merchant_manage_page.get_tis_msg()
        print(res_msg)
        self.assertEqual(test_data_success['expected'],res_msg)

        time.sleep(2)
        # 点击最后一页
        self.merchant_manage_page.click_last_page_button()
        time.sleep(2)


        res_merchant_name=self.merchant_manage_page.get_new_merchant_name()
        print(res_merchant_name)
        self.assertEqual(res_merchant_name,test_data_success['merchant_name'])
        time.sleep(2)

        # 点击修改按钮
        self.merchant_manage_page.get_revise_button()
        # for li in merchant_data_success:
        #     e2 = self.driver.find_element_by_xpath("//a[@data-merchantname='{}']".format(li['merchant_name']))
        #     e2.click()
        #     time.sleep(6)
        time.sleep(6)

    # @ddt.data(*merchant_data_error)
    # def test_add_merchant_error(self,test_data_error):
    #     """新增商户失败"""
    #     time.sleep(2)
    #     self.merchant_manage_page.add_merchant(test_data_error['merchant_name'],
    #                                            test_data_error['organ_code'],
    #                                            test_data_error['lega_lName'],
    #                                            test_data_error['legal_Idcard'],
    #                                            test_data_error['merchant_type'])
    #     time.sleep(2)
    #     ac=self.merchant_manage_page.get_tis_msg()
    #     print(ac)
    #     self.assertEqual(test_data_error['expected'],ac)

