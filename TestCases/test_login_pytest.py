# @author       ：小青年
# @ProjectName  ：py_web_TR_boss
# @Name         ：test_login_pytest
# @time         ：2020/4/22 10:04
import time

import pytest
from data.login_data import login_data_success
# test_data_success=login_data_success[0]
class TestLogin():
    @pytest.mark.parametrize('login_data_success_info',login_data_success)
    @pytest.mark.login_success
    def test_login_success(self,login_data_success_info,manage_driver):
        driver,login_page,user_page=manage_driver


        # 步骤一：执行登录操作：login_page.login()
        # login_page.login(login_data_success_info['username'], login_data_success_info['pwd'])
        login_page.login(login_data_success_info['username'], login_data_success_info['pwd'])
        time.sleep(3)

        # 步骤二：获取实际结果
        actual = user_page.get_username_text().text

        # 步骤三：获取预期结果
        expected=login_data_success_info['expected']

        # 步骤四：断言
        assert actual == expected
# if __name__ == '__main__':
#     # 如果使用pytest当中的参数化和fixture功能
#     pytest.main(['-m login_success', '-s'])