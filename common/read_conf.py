# @author       ：小青年
# @ProjectName  ：py_api_qianchengdai
# @Name         ：read_conf
# @time         ：2020/3/11 16:52 

from configparser import ConfigParser
from common.contants import conf_dir
import os
class MyConf:
    def __init__(self,filename,encoding='utf-8'):
        """
        :param filename: 配置文件名
        :param encoding: 文件编码方法
        """
        self.filename=filename
        self.encoding=encoding
        # 创建文件解释器对象，设置为对应的conf属性
        self.conf=ConfigParser() # ConfigParser：专门解析配置文件的
        # 使用解释器对象，加载配置文件中的内容
        self.conf.read(filename,encoding)
    # 读取数据
    def get_str(self,section,option):
        """
        :param section: 配置块
        :param option: 配置项
        :return:
        """
        # 使用配置文件解释器，调用里面的get方法
        return self.conf.get(section,option)

    # 读取整型数据类型
    def get_int(self,section,option):
        return self.conf.getint(section,option)

    # 读取浮点数据类型
    def get_float(self,section,option):
        return self.conf.getfloat(section,option)

    # 读取布尔值类型
    def get_boolean(self,section,option):
        return self.conf.getboolean(section,option)

    # 写入数据
    def write_data(self,section,option,value):
        """
        :param section: 配置块
        :param option: 配置项
        :param value: 配置项对应的值
        :return:
        """
        # （1）写入：通过文件解释器对象，在通过set方法，然后传入块、配置项、写入的内容
        self.conf.set(section,option,value)
        # （2）保存到文件
        self.conf.write(open(self.filename,'w',encoding=self.encoding))
if __name__ == '__main__':
    mysql_filename=os.path.join(conf_dir,'mysql_conf.ini')
    conf=MyConf(mysql_filename).get_str('mysql','host')
    print(conf)
    test_data_filename=os.path.join(conf_dir,'test_data_conf.ini')
    test_data_conf=MyConf(test_data_filename).write_data('test_data','aa','123')

