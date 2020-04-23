# @author       ：小青年
# @ProjectName  ：py_web_TR_boss
# @Name         ：merchant_page
# @time         ：2020/4/3 15:11
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from common.base_page import BasePage
from locator import navigation_locator
from locator import merchant_manage_locator
from data.merchant_data import merchant_data_success


class MerchantPage(BasePage):
    def get_navigation_merchant(self):
        """获取商户管理导航元素"""
        model_name = "导航栏-获取商户管理导航元素"
        return self.get_element(navigation_locator.navigation_merchant_locator,model_name)

    def get_men_merchant(self):
        """获取菜单商户管理元素"""
        model_name = "菜单栏-获取商户管理菜单元素"
        return self.get_element(merchant_manage_locator.men__merchant_locator,model_name)

    def get_add_merchant_button(self):
        """获取新增商户按钮元素"""
        model_name = "商户页面-获取商户新增按钮元素"
        return self.get_element(merchant_manage_locator.add_button_locator,model_name)

    def get_merchant_name(self):
        """商户名称输入框"""
        model_name = "商户页面-获取商户名称输入框元素"
        return self.get_element(merchant_manage_locator.merchant_name_locator,model_name)

    def get_merchant_type(self):
        """获取商户类型下拉框"""
        model_name = "商户页面-获取商户类型下拉框元素"
        return self.get_element(merchant_manage_locator.merchant_type_select_locator,model_name)

    def get_organ_code(self):
        """获取组织机构代码号"""
        model_name = "商户页面-获取组织机构代码号元素"
        return self.get_element(merchant_manage_locator.organ_code_locator,model_name)

    def get_lega_lName(self):
        """获取法定代表姓名"""
        model_name = "商户页面-获取法定代表姓名元素"
        return self.get_element(merchant_manage_locator.lega_lName_locator,model_name)

    def get_legal_Idcard(self):
        """获取法定代表身份证号"""
        model_name = "商户页面-获取法定代表身份证号元素"
        return self.get_element(merchant_manage_locator.legal_Idcard_locator,model_name)

    def get_confirm_button(self):
        """获取新增的确定按钮"""
        model_name = "商户页面-获取新增的确定按钮元素"
        return self.get_element(merchant_manage_locator.confirm_button_locator,model_name)

    def get_cancel_button(self):
        """取消按钮"""
        model_name = "商户页面-获取取消按钮元素"
        return self.get_element(merchant_manage_locator.cancel_button_locator,model_name)

    def get_tis_msg(self):
        """获取提示信息"""
        model_name = "商户页面-提示信息元素"
        return self.get_element(merchant_manage_locator.tis_msg_locator,model_name).text

    def click_next_page_button(self):
        """获取下一页按钮"""
        model_name = "商户页面-下一页按钮元素"
        self.get_element(merchant_manage_locator.next_page_button_locator,model_name).click()

    def click_last_page_button(self):
        """点击最后一页"""
        model_name = "商户页面-最后一页元素"
        self.get_element(merchant_manage_locator.last_page_button_locator,model_name).click()

    def get_new_merchant_name(self):
        """获取新增的时候名称"""
        model_name = "商户页面-新增的时候名称元素"
        return self.get_element(merchant_manage_locator.new_merchant_name_locator,model_name).text

    def get_revise_button(self):
        """根据新增商户名称获取对应的修改按钮"""
        model_name="商户页面-获取修改按钮"
        return self.get_element(merchant_manage_locator.revise_locator,model_name).click()

    def add_merchant(self, merchantName, organCode, legaIName, legalIdcard, merchantType):
        """新增商户"""

        # 点击导航栏，商户管理
        self.get_navigation_merchant().click()
        # 点击菜单栏，商户管理
        self.get_men_merchant().click()
        # 点击新增商户按钮
        self.get_add_merchant_button().click()

        # 输入：商户名称
        self.get_merchant_name().send_keys(merchantName)

        # 选择：商户类型
        # self.get_merchant_type().send_keys(merchantType)
        # self.select_selenium(self.get_merchant_type,merchantType)
        select_elem = self.get_merchant_type()
        # 步骤二：初始化select类，将参数传入到类里面
        # select = Select(select_elem)
        # # 步骤三：选择，三种方式
        # # 1'通过value方式定位：select.select_by_value('doc') # 使用select对象
        # # 2'通过text文本定位：select.select_by_visible_text('微软 Word (.doc)')
        # # 3'通过index索引定位：select.select_by_index(1) # 索引从0开始
        self.select_selenium(select_elem, merchantType)

        # 输入：组织机构代码号
        self.get_organ_code().send_keys(organCode)
        # 输入：获取法定代表姓名
        self.get_lega_lName().send_keys(legaIName)
        # 输入：法定代表身份证号
        self.get_legal_Idcard().send_keys(legalIdcard)

        # 点击确定
        self.get_confirm_button().click()
