# @author       ：小青年
# @ProjectName  ：py_web_qianchengdai
# @Name         ：switch_alert
# @time         ：2020/3/19 14:52 

import time
from selenium import webdriver
from common.base_page import BasePage
class SwitchAlert(BasePage):

    def switch_alert_f(self):

        # 隐式等待
        driver.implicitly_wait(30)
        driver.get(r'E:\test\py_web_qianchengdai\data\switch_iframe.html')
        # 定位hello world，并点击
        driver.find_element_by_id('hello').click()
        time.sleep(2)
        self.switch_alert()
        driver.quit()
if __name__ == '__main__':
    driver = webdriver.Chrome()
    s=SwitchAlert(driver).switch_alert_f()