# @author       ：小青年
# @ProjectName  ：py_web_qianchengdai
# @Name         ：select_selenium
# @time         ：2020/3/19 16:52 

import time
from selenium import webdriver
from common.base_page import BasePage
class SelectSelenium(BasePage):
    def select_selenium_f(self):
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


        # 选择：微软 Word (.doc)
        # ①步骤一：定位select元素
        select_locator=driver.find_element_by_name("ft")
        # 选择的值：通过value方式定位
        locator='doc'
        self.select_selenium(select_locator,locator)
        time.sleep(2)
        driver.quit()
if __name__ == '__main__':
    driver = webdriver.Chrome()
    s=SelectSelenium(driver).select_selenium_f()