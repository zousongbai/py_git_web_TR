# @author       ：小青年
# @ProjectName  ：py_web_TR_boss
# @Name         ：logger
# @time         ：2020/4/16 10:01 

# 日志文件
import logging
from logging.handlers import RotatingFileHandler
import time
from common import contants

# 设置日志的格式
fmt = " %(asctime)s  %(levelname)s %(filename)s %(funcName)s [ line:%(lineno)d ] %(message)s"
# 时间的格式
datefmt = '%a, %d %b %Y %H:%M:%S'
# 输出到控制台同时输出到文件中
handler_1 = logging.StreamHandler()
# 输出文件的名称
curTime = time.strftime("%Y-%m-%d %H %M", time.localtime())
# 将日志输出到Logs文件夹中
handler_2 = RotatingFileHandler(contants.log_dir + "/Web_Autotest_{0}.log".format(curTime), backupCount=20,
                                encoding='utf-8')

# 设置rootlogger 的输出内容形式，输出渠道
# 备注：调用python3中logging模块的basicConfig基本设置
logging.basicConfig(format=fmt, datefmt=datefmt, level=logging.INFO, handlers=[handler_1, handler_2])

logging.info("hehehe")
