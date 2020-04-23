# @author       ：小青年
# @ProjectName  ：py_web_qianchengdai
# @Name         ：01_input元素上传文件
# @time         ：2020/3/22 16:14 

import time
from selenium import webdriver
from common.base_page import BasePage
class InputUploadFile(BasePage):
    def input_upload_file_f(self):
        # 隐式等待
        driver.implicitly_wait(30)
        driver.get(r"E:\test\py_web_qianchengdai\调试\文件上传\上传文件.html")
        time.sleep(2)
        file_elem = driver.find_element_by_name("myfile")  # 定位元素
        file_name=r"E:\test\py_web_qianchengdai\调试\js代码\02_通过js窗口滚动.py"
        self.input_upload_file(file_elem,file_name)  # 上传文件
if __name__ == '__main__':
    driver = webdriver.Chrome()
    js=InputUploadFile(driver).input_upload_file_f()