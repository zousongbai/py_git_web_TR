# @author       ：小青年
# @ProjectName  ：py_web_TR_boss
# @Name         ：merchant_manage_locator
# @time         ：2020/4/3 16:52 

from selenium.webdriver.common.by import By
from data.merchant_data import merchant_data_success

# 菜单栏商户管理
men__merchant_locator=(By.XPATH,'//li[2]//a[1]//span[1]')

# 新增按钮
add_button_locator=(By.XPATH,"//a[contains(@class,'btn-purple')]")

# 商户名称
merchant_name_locator=(By.ID,'form-field-merchantName')

# 商户类型下拉框，定位select元素
merchant_type_select_locator=(By.ID,'form-field-merchantType')

# 组织机构代码号
organ_code_locator=(By.ID,'form-field-organCode')

# 法定代表姓名
lega_lName_locator=(By.ID,'form-field-legalName')

# 法定代表身份证号
legal_Idcard_locator=(By.ID,'form-field-legalIdNo')

# 确定按钮
confirm_button_locator=(By.ID,'createMerchant')

# 取消按钮
cancel_button_locator=(By.ID,"//div[@id='createModal']//button[@class='btn btn-sm']")

# 错误信息提示
tis_msg_locator=(By.XPATH,"//div[@class='jBox-text-left']")

# 下一页按钮
next_page_button_locator=(By.XPATH,"//li[@id='table_next']//a")

# 最后一页
last_page_button_locator=(By.XPATH,"//ul[@class='pagination']/li[last()-1]/a")

# 新增成功后的商户名称
for li in merchant_data_success:
    new_merchant_name_locator=(By.XPATH,"//td[text()='{}']".format(li['merchant_name']))
    print(new_merchant_name_locator)

# # 定位商户ID为
# revise="//a[@data-merchantid='000001']"

# 根据商户名称去查找对应的修改功能
for li in merchant_data_success:
    revise_locator=(By.XPATH,"//a[@data-merchantname='{}']".format(li['merchant_name']))
    print(revise_locator)



