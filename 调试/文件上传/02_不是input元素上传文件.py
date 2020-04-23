# @author       ：小青年
# @ProjectName  ：py_web_qianchengdai
# @Name         ：02_不是input元素上传文件
# @time         ：2020/3/22 16:52 

import time
from selenium import webdriver

from common.base_page import BasePage


class InputUploadFile(BasePage):
    def pyautogui_upload_file_f(self):
        # 隐式等待
        driver.implicitly_wait(30)
        driver.get(r"E:\test\py_web_qianchengdai\调试\文件上传\上传文件.html")
        time.sleep(2)
        file_elem = driver.find_element_by_name("myfile")  # 定位元素
        file_elem.click()
        # 系统之间要用强制等待
        time.sleep(3)
        # 步骤二：往组件里面写入文件
        file_name = r"E:\test\py_web_qianchengdai\调试\js代码\02_通过js窗口滚动.py"
        self.pyautogui_upload_file(file_name)

        # self.input_upload_file(file_elem,file_name)  # 上传文件
if __name__ == '__main__':
    driver = webdriver.Chrome()
    f=InputUploadFile(driver).pyautogui_upload_file_f()