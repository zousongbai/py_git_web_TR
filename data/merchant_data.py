# @author       ：小青年
# @ProjectName  ：py_web_TR_boss
# @Name         ：merchant_data
# @time         ：2020/4/6 11:26 

from common.random_data import TestDataNumber
from common.id_card import getRandomIdCard
NumToChinese=TestDataNumber().num_to_chinese()
number=TestDataNumber().random_num()
Idcard=getRandomIdCard()

merchant_data_success=[
    {"merchant_name":"测试商户名称"+NumToChinese,"organ_code":"91430111MA4L16J"+str(number),"lega_lName":"法人代表姓名"+NumToChinese,"legal_Idcard":Idcard,"merchant_type":"2",'expected':"添加成功"}
]

# '测试商户名称01','91430111MA4L16JQ9B','法人代表姓名01','110101199003076077','2'
# print(merchant_data_success[0]['organ_code'])


merchant_data_error=[
{"merchant_name":"快牛","organ_code":"91430111MA4L16J"+str(number),"lega_lName":"法人代表姓名"+NumToChinese,"legal_Idcard":Idcard,"merchant_type":"2",'expected':"该商户已存在！"}
]

