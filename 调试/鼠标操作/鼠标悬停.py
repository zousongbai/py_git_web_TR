# @author       ：小青年
# @ProjectName  ：py_web_qianchengdai
# @Name         ：鼠标悬停
# @time         ：2020/3/19 15:50 

import time
from selenium import webdriver
from common.base_page import BasePage
class MouseHover(BasePage):
    def mouse_hover_f(self):
        # 隐式等待
        driver.implicitly_wait(30)
        driver.get('http://www.baidu.com')
        driver.maximize_window()

        # 鼠标悬停到百度首页-设置
        setting_locator="//a[@href='http://www.baidu.com/gaoji/preferences.html']"
        self.mouse_hover(setting_locator)
        time.sleep(2)

        # 左击-高级搜索
        gaoji_locator="//a[text()='高级搜索']"
        self.mouse_left_click(gaoji_locator)
        time.sleep(2)
        driver.quit()
if __name__ == '__main__':
    driver = webdriver.Chrome()
    s=MouseHover(driver).mouse_hover_f()