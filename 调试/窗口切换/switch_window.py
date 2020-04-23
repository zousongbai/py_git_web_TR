# @author       ：小青年
# @ProjectName  ：py_web_qianchengdai
# @Name         ：switch_window
# @time         ：2020/3/19 11:46 

from selenium import webdriver
from common.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait # 导入计时器
from selenium.webdriver.support import expected_conditions as EC
class SwitchWindow(BasePage):

    def switch_window(self):

        driver.implicitly_wait(30)
        driver.get('http://www.baidu.com')
        input_elem=driver.find_element_by_id('kw')
        # 输入：柠檬班
        input_elem.send_keys('柠檬班')
        # 百度提交
        driver.find_element_by_id('su').click()

        # 点击腾讯课堂
        ketang=driver.find_element_by_xpath("//a[contains(text(),'lemon.ke.qq.com/')]")
        ketang.click()

        # handles = driver.window_handles
        # print('获取所有的窗口句柄',handles)
        #
        # # 切换窗口
        # r=driver.switch_to.window(handles[-1])
        # print("切换之后的当前窗口句柄",driver.current_window_handle)
        # return r
        print("切换之前的当前窗口句柄", driver.current_window_handle)
        self.switch_window_new()
        print("切换之后的当前窗口句柄", driver.current_window_handle)
        driver.quit()
if __name__ == '__main__':
    driver = webdriver.Chrome()
    s=SwitchWindow(driver).switch_window()
