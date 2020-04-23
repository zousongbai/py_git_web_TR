# @author       ：小青年
# @ProjectName  ：py_web_TR_boss
# @Name         ：random_data
# @time         ：2020/4/8 20:59 

import random
class TestDataNumber:
    def random_num(self):
        """产生三位数的随机数"""
        number = random.randint(100, 999)
        return number

    def num_to_chinese(self):
        """数字转中文"""
        number=self.random_num()
        num_dict={"0":u"零","1":u"一","2":u"二","3":u"三","4":u"四","5":u"五","6":u"六","7":u"七","8":u"八","9":u"九"}
        listnum=list(str(number))
        shu=[]
        for i in listnum:
            # print(num_dict[i])
            shu.append(num_dict[i])
        NumToChinese="".join(shu)
        return NumToChinese
if __name__ == '__main__':
    NumToChinese=TestDataNumber().num_to_chinese()
    print(NumToChinese)