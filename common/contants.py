# @author       ：小青年
# @ProjectName  ：py_api_qianchengdai
# @Name         ：contains
# @time         ：2020/3/11 16:53 

"""
该模块用来处理整个项目目录的路径
"""
import os

# 项目目录的路径
basedir=os.path.dirname(os.path.dirname(__file__))
# print('获取项目目录：',basedir)

# 配置文件夹的目录
conf_dir=os.path.join(basedir,'conf')
# print('配置文件夹的目录：',conf_dir)

# 用例数据的目录
data_dir=os.path.join(basedir,'data')
# print('用例数据的目录：',data_dir)

# 日志文件的目录
log_dir=os.path.join(basedir,'log')
# print('日志文件的目录：',log_dir)

# 测试报告的目录
reports_dir=os.path.join(basedir,'reports')
# print('日志文件的目录：',reports_dir)

# 测试用例模块所在的目录
case_dir=os.path.join(basedir,'TestCases')
# print('测试用例模块所在的目录：',case_dir)

# 截图目录
screenshot_dir=os.path.join(basedir,'ScreenShot')