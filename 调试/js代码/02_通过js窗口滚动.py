# @author       ：小青年
# @ProjectName  ：py_web_qianchengdai
# @Name         ：通过js滚动到指定位置
# @time         ：2020/3/20 17:46 

import time
from selenium import webdriver
from common.base_page import BasePage
class JsDesign(BasePage):
    def js_design(self):
        # 隐式等待
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("http://lemon.ke.qq.com/")
        time.sleep(2)

        # 移动到窗口绝对位置坐标
        self.js_move_to_absolute_coord(0,1200)
        time.sleep(2)

        # 移动到指定的坐标(相对当前的坐标移动)
        self.js_move_to_appoint(0,1600)
        time.sleep(2)

        # 找到元素
        ele=driver.find_element_by_xpath("//h4[text()='华华老师']")

        # 移动到元素element对象的“顶端”与当前窗口的“顶部”对齐
        self.js_move_to_element_top(ele)
        time.sleep(2)

        # 移动到元素element对象的“底端”与当前窗口的“底部”对齐
        self.js_move_to_element_bottom(ele)
        time.sleep(2)

        # 移动到页面最底部
        self.js_move_to_page_bottom()
        time.sleep(2)

if __name__ == '__main__':
    driver = webdriver.Chrome()
    js=JsDesign(driver).js_design()