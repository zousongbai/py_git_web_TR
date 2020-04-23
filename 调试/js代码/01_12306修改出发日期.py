# @author       ：小青年
# @ProjectName  ：py_web_qianchengdai
# @Name         ：12306修改出发日期
# @time         ：2020/3/20 17:21 


# 系统和系统之间的交互，使用强制等待，如：Python和js的交互
from selenium import webdriver
import time

driver = webdriver.Chrome()
# 隐式等待
driver.implicitly_wait(30)
driver.maximize_window()
driver.get("https://www.12306.cn/index/")
# （1）查找到修改的元素
data_element = driver.find_element_by_id("train_date")
# （2）修改data_element的readOnly属性
js_code = "arguments[0].readOnly=false;"
# 备注：arguments[0]：表示data_element
# （3）发送js指令：将js代码发送给12306
driver.execute_script(js_code, data_element)
# 系统和系统之间的交互，使用强制等待，如：Python和js的交互
time.sleep(2)  # 添加等待的目的是让上一步修改的信息生效后，再进行下一步操作
# （4）第二步：修改value属性
# 继续发送：修改后的value值
js_code_date = "arguments[0].value='2020-01-29';"
driver.execute_script(js_code_date, data_element)
time.sleep(2)
driver.quit()