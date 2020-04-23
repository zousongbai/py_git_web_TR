# @author       ：小青年
# @ProjectName  ：py_web_TR_boss
# @Name         ：user_page
# @time         ：2020/4/3 11:55 

from common.base_page import BasePage
from locator import user_locator
class UserPage(BasePage):
    def get_username_text(self):
        """获取用户名文本"""
        return self.driver.find_element(*user_locator.username_text)