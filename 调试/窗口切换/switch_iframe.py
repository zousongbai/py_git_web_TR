# @author       ：小青年
# @ProjectName  ：py_web_qianchengdai
# @Name         ：switch_iframe
# @time         ：2020/3/19 14:33 

from selenium import webdriver
from common.base_page import BasePage
class SwitchIframe(BasePage):

    def switch_iframe_f(self):

        # 隐式等待
        driver.implicitly_wait(30)
        driver.get(r'E:\test\py_web_qianchengdai\data\switch_iframe.html')
        # 定位hello world
        driver.find_element_by_id('hello')

        # 切换iframe

        # （2）方式三：通过iframe元素的 webelement对象切换
        iframe_elem = driver.find_element_by_xpath('//iframe[@name="baidu"]')
        # driver.switch_to.frame(iframe_elem)
        self.switch_iframe(iframe_elem)
        driver.quit()
if __name__ == '__main__':
    driver = webdriver.Chrome()
    s=SwitchIframe(driver).switch_iframe_f()