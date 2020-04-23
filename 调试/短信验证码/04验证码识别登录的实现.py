# @author       ：小青年
# @ProjectName  ：py_web_qianchengdai
# @Name         ：04验证码识别登录的实现
# @time         ：2020/3/19 16:52

"""
第一步：输入账号

第二步：输入密码

第三步：输入验证码
    1、识别验证码的内容
        1）、获取验证码图片
           保存整个页面截图
           定位页面中的验证码
           获取验证码图片的坐标位置
        2）、识别
    2、输入

第四步：点击登录
"""
import os
from selenium import webdriver
from PIL import Image
from 调试.短信验证码.chaojiying import Chaojiying
from common.base_page import BasePage
from common.contants import screenshot_dir
# 第一步：打开浏览器，访问登录页面
class aa(BasePage):
    def bb(self):

        # 访问登录页面
        driver.get("http://www.chaojiying.com/user/login/")

        # 第二步：输入账号和密码
        # 定位到账号输入框
        user_input = driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div[1]/form/p[1]/input")
        # 输入账号
        user_input.send_keys("qq121292679")

        # 定位到密码输入框
        pwd_input = driver.find_element_by_xpath("//input[@placeholder='密码']")
        # 输入密码
        pwd_input.send_keys("a546245426")

        # 第三步：验证码识别
        # 1、获取到验证码的图片
        # 保存整个页面截图
        # driver.save_screenshot("page.png")
        img_name=self.Save_screenShot()
        print(img_name)
        # 定位页面中的验证码
        v_code = driver.find_element_by_xpath("//form[@name='fm2']//div//img")
        # 获取验证码图片的坐标位置
        size = v_code.size # 获取验证码图片高度和宽度
        loc = v_code.location # 获取验证码图片x和y位置
        # rect=v_code.rect # 获取验证码图片高度和宽度、x和y位置
        # 获取左边界位置
        left = loc["x"]*1.25
        # 获取右边界位置
        right = (loc['x'] + size["width"])*1.25
        # 获取上边界位置
        top = loc['y']*1.25
        # 获取下边界位置
        bot = (loc['y'] + size["height"])*1.25
        # 备注：1.25获得途径：通过桌面右击->显示设置->缩放与布局->更改文本、应用等项目的大小->125%
        # 坐标位置的顺序：左  上   右   下
        location = (left, top, right, bot)
        # 打开页面图片
        # page = Image.open("page.png")
        page = Image.open(img_name)
        # 根据坐标位置进行截图
        v_pic = page.crop(location)
        # 保存截取下来的图片（验证码）
        v_pic.save("v.png")

        # 2、识别验证码
        yz = Chaojiying(username='zousongbai', password='880320aa', soft_id='903275')
        pic = open('v.png', 'rb').read()
        # 通过对象调用post_pic方法，进行图片识别，返回的结果是一个地点类型数据，其中的pic_str就是识别的结果
        result = yz.post_pic(pic, codetype='1004')
        v_str = result.get('pic_str')
        print('识别的结果:', v_str)

        # 第四步：验证码输入
        # 定位验证码输入框
        v_input = driver.find_element_by_xpath("//input[@placeholder='输入验证码']")

        # 输入验证码
        v_input.send_keys(v_str)

        # 点击登录
        # 定位登录按钮
        btn = driver.find_element_by_xpath("//input[@class='login_form_input_submit']")
        # 点击登录
        btn.click()
        driver.quit()

if __name__ == '__main__':
    driver = webdriver.Chrome()
    s=aa(driver).bb()
