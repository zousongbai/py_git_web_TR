# @author       ：小青年
# @ProjectName  ：py_web_TR_boss
# @Name         ：login_page
# @time         ：2020/4/3 10:42
import os
import time

from common.base_page import BasePage
from common.contants import conf_dir
from common.read_conf import MyConf
from locator import login_locator
url_conf_filename=os.path.join(conf_dir,'url_conf.ini')
url=MyConf(url_conf_filename).get_str('url','url_login')
class LoginPage(BasePage):
    def get_input_username(self):
        """获取输入登录用户名"""
        model_name="登陆页面-获取用户名输入框"
        return self.get_element(login_locator.login_username_locator,model_name)

    def get_input_pwd(self):
        """获取输入登录密码"""
        model_name = "登陆页面-获取密码输入框"
        return self.get_element(login_locator.login_pwd_locator,model_name)

    def get_login_button(self):
        """获取登录按钮"""
        model_name = "登陆页面-获取登录按钮"
        return self.get_element(login_locator.login_button_locator,model_name)

    def login(self,username,pwd):
        """登录功能"""

        self.driver.get(url)
        # 步骤一：查找登录的用户名和密码元素
        # 查找输入的用户名
        username_element=self.get_input_username()
        # 查找输入的密码
        pwd_element=self.get_input_pwd()
        # 查找登录按钮
        button_element=self.get_login_button()

        # 步骤二：输入用户名和密码
        username_element.send_keys(username)
        pwd_element.send_keys(pwd)

        # 步骤三：登录
        # pwd_element.submit()
        button_element.click()
        time.sleep(2)