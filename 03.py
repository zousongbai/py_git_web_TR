# @author       ：小青年
# @ProjectName  ：py_web_TR_boss
# @Name         ：03
# @time         ：2020/4/16 17:28 

import logging
from logging.handlers import RotatingFileHandler,TimedRotatingFileHandler
# def create_logger():
# (1)步骤一：创建一个名为：py24的日志收集器
my_log = logging.getLogger("py24")

# (2)步骤二：设置等级
my_log.setLevel("DEBUG")

# (3)步骤三：添加输出渠道(输出到控制台)
# ①创建一个输出到控制台的输出渠道
sh = logging.StreamHandler()
# ②设置输出等级：设置输出到控制台的等级
sh.setLevel("INFO")
# ③将输出渠道绑定到日志收集器上
my_log.addHandler(sh)

# (4)步骤四：添加输出渠道(输出到文件)
# ①创建一个输出到文件的输出渠道                    )
# 3)按时间进行轮转
fh=TimedRotatingFileHandler(filename="test.log",
                            encoding="utf-8",
                            when="S",#设置间隔单位(默认H)。S：Seconds(秒)，M：Minutes(分钟),H：Hours(小时)，D：Day()天
                            interval=1,#设置间隔单位
                            backupCount=7#轮转的文件数量
                            )
# ②设置输出等级：设置输出到控制台的等级
fh.setLevel("DEBUG")
# ③将输出渠道绑定到日志收集器上
my_log.addHandler(fh)

# (5)步骤五：设置日志输出的格式
# ①创建一个日志输出格式
formatter = logging.Formatter('%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s')
# asctime：当前系统的时间
# filename：当前文件名
# lineno：当前输出是哪一行
# levelname：当前输出日志的等级
# message：输出的日志信息
# ②将输出格式和输出渠道进行绑定
sh.setFormatter(formatter)  # 输出到控制台的绑定
fh.setFormatter(formatter)  # 输出到文件的绑定


my_log.debug("这个是自己记录了的debug等级的日志")
my_log.info("这个是自己记录了的info等级的日志")
my_log.warning("这个是自己记录了的warning等级的日志")
my_log.error("这个是自己记录了的error等级的日志")
my_log.critical("这个是自己记录了的critical等级的日志")