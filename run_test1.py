# @author       ：小青年
# @ProjectName  ：py_web_TR_boss
# @Name         ：run_test
# @time         ：2020/4/22 14:29

"""启动文件不要test，不然pytest会把这个文件当成用例文件，再执行一次"""

import pytest

# # 添加入口
# # ②第二种方式：xml，生成xml文件，主要在Jenkins中使用xml
# pytest.main(['-m login_success', '-s', '--junitxml=reports/report.xml'])
# # -m：运行指定的参数，执行标记
# # -s：打印print的信息
# # --junitxml：xml文本的测试报告，该路径没有则自动生成


import pytest
# 添加入口
# ③第三种方式：html。HTMLTestRunner。安装：pip install pytest-html
# pytest.main(['-m login_success','-s','--html=reports/report.html'])
# -m：运行指定的参数，执行标记
# -s：打印print的信息

pytest.main(['-m login_success','-s',r'--alluredir=alluredir/'])