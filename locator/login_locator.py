# @author       ：小青年
# @ProjectName  ：py_web_TR_boss
# @Name         ：login_locator
# @time         ：2020/4/3 10:46
from selenium.webdriver.common.by import By

# 登录用户名元素
login_username_locator=(By.ID,"userName") # 利用元祖的方式，解决了只能使用xpath方式的弊端

# 登录密码元素
login_pwd_locator=(By.ID,"userPassword")

# 登录按钮元素
login_button_locator=(By.XPATH,"//button[contains(@class,'width-35')]")
