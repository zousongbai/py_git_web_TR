# @author       ：小青年
# @ProjectName  ：py_web_qianchengdai
# @Name         ：base_page
# @time         ：2020/3/19 10:02 

"""
（1）自定义等待：自己封装。如：等待元素可见、等待元素出现、等待元素可被点、不需要显示等待
（2）截图
（3）窗口切换：Windows、iframe、alert
（4）鼠标操作：鼠标悬停、鼠标左击、鼠标拖拽
（5）选择下拉框(select)
（6）窗口的滚动
（7）文件上传：
①input标签使用send_keys
②非input标签pyautogui或
"""
import logging
import time
import pyautogui
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from common.contants import screenshot_dir
# from common import logger
from common.my_log import my_log


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_element_visible(self, locator, timeout, poll_frequency=0.5):
        """等待元素可见"""
        wait = WebDriverWait(self.driver, timeout, poll_frequency=poll_frequency)
        return wait.until(EC.visibility_of_element_located(locator))

    def wait_element_precence(self, locator, timeout, poll_frequency=0.5):
        """等待元素出现"""
        wait = WebDriverWait(self.driver, timeout, poll_frequency=poll_frequency)
        return wait.until(EC.presence_of_element_located(locator))

    def wait_element_clickable(self, locator, timeout, poll_frequency=0.5):
        """等待元素可被点击"""
        wait = WebDriverWait(self.driver, timeout, poll_frequency=poll_frequency)
        return wait.until(EC.element_to_be_clickable(locator))

    def get_element(self, locator,model_name="model"):
        """不需要显示等待"""
        try:

            return self.driver.find_element(*locator)
        except:
            # 截图保存
            self.Save_screenShot(model_name)
            # logging.exception("{}下查找元素失败".format(model_name))
            my_log.exception("{}下查找元素失败".format(model_name))
    def Save_screenShot(self, model_name="model"):
        """
        截图功能
        :param model_name: 功能模块货用例名称
        :return:
        """

        # 根据功能和时间点生成截图
        # 文件格式 ：功能名称_年月日-时分秒.png
        img_file_path = screenshot_dir + "/{0}_{1}.png".format(model_name,
                                                          time.strftime("%Y-%m-%d-%H-%M-%S",
                                                          time.localtime()))
        # logging.info("截图成功,路径为：{0}".format(img_file_path))
        my_log.info("截图成功,路径为：{0}".format(img_file_path))

        # 截图文件存放在 Screenshot目录下
        # driver方法：self.driver.Save_screenshot()
        self.driver.save_screenshot(img_file_path)
        return img_file_path

    def switch_window_new(self):
        """切换到新窗口"""
        handles = self.driver.window_handles
        print('获取所有的窗口句柄', handles)

        # 切换窗口
        self.driver.switch_to.window(handles[-1])

    def switch_iframe(self, iframe_element):
        """切换到iframe中
        通过switch_to.frame()进行切换
        iframe操作步骤：
            （1）先定位iframe元素
            （2）再driver.switch_to.frame进入iframe
            （3）定位iframe里面的元素，进行操作
            （4）切换定位完成后，记住要退出：driver.switch_to.default_content()
        """
        self.driver.switch_to.frame(iframe_element)

    def switch_alert(self):
        """切换到alert
        通过switch_to.alert进行切换
        alert操作步骤：
            （1）切换到alert弹框上面，switch_to不需要加括号
            （2）点击确认按钮或取消按钮：确定(accept)、取消(dismiss)
        """
        # switch_to.alert：得到的是一个Alert对象
        myalert = self.driver.switch_to.alert
        # 点击确认按钮
        myalert.accept()

    def mouse_hover(self, locator):
        """鼠标悬停
        操作步骤：
        （1）步骤一：初始化ActionChains
        （2）步骤二：定位要操作的元素
        （3）步骤三：执行对应的操作，右击，传入定位的元素
        （4）步骤四：执行完操作以后，加释放动作
        """
        # (1)步骤一：初始化ActionChains
        action_chaincs = ActionChains(self.driver)
        # (2)步骤二：定位要操作的元素
        element = self.driver.find_element_by_xpath(locator)
        # (3)步骤三：执行对应的操作，传入定位的元素
        action_chaincs.move_to_element(element)
        # (4)步骤四：执行完操作以后，加释放动作
        action_chaincs.perform()
        # 备注：如果不加这步，前面的操作都不会被执行,因为不悬停,高级搜索没有出现

    def mouse_left_click(self, locator):
        """鼠标左击"""
        # (1)步骤一：初始化ActionChains
        action_chaincs = ActionChains(self.driver)
        # (2)步骤二：定位要操作的元素
        element = self.driver.find_element_by_xpath(locator)
        # (3)步骤三：执行对应的操作，传入定位的元素
        action_chaincs.click(element)  # 因为action_chaincs是全局的,所以可以直接使用
        # (4)步骤四：执行完操作以后，加释放动作
        action_chaincs.perform()

    def drag(self, src, target):
        """鼠标拖拽
        拖拽操作：右键按住拖动某一个元素到另外一个区域，然后释放按键
        """
        # (1)步骤一：初始化ActionChains
        action_chaincs = ActionChains(self.driver)
        # (2)步骤二：执行对应的操作，传入定位的元素
        action_chaincs.drag_and_drop(src, target)
        # (3)步骤三：执行完操作以后，加释放动作
        action_chaincs.perform()

    def select_selenium(self, select_element, locator):
        """
        选择下拉框(select)selenium封装
        :param select_locator: 定位select元素
        :param locator: 选择的元素value值
        :return:
        """
        # （2）方式二：使用selenium封装
        # ①步骤一：初始化select类，将参数传入到类里面
        select = Select(select_element)
        # ②步骤二：选择，三种方式
        # 1）通过value方式定位
        select.select_by_value(locator)  # 使用select对象
        # # 2）通过text文本定位
        # select.select_by_visible_text('微软 Word (.doc)')
        # # 3）通过index索引定位
        # select.select_by_index(1) # 索引从0开始

    def js_code_send(self, js_code_date, js_element):
        """发送js代码"""
        self.driver.execute_script(js_code_date, js_element)

    """
    滚动方式：
    （1）移动到元素element对象的“顶端”与当前窗口的“顶部”对齐
            driver.execute_script("arguments[0].scrollIntoView();", element);
            或driver.execute_script("arguments[0].scrollIntoView(true);", element);
    （2）移动到元素element对象的“底端”与当前窗口的“底部”对齐
        driver.execute_script("arguments[0].scrollIntoView(false);", element);
    （3）移动到页面最底部
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)");
    （4）移动到指定的坐标(相对当前的坐标移动)
        driver.execute_script("window.scrollBy(0, 700)");
    （5）移动到窗口绝对位置坐标，如：下移动到纵坐标1600像素位置
        driver.execute_script("window.scrollTo(0, 1600)");
    """

    def js_move_to_absolute_coord(self, width, height):
        """移动到窗口绝对位置坐标"""
        js_code = "window.scrollTo({},{})".format(width, height)
        self.driver.execute_script(js_code)

    def js_move_to_appoint(self, width, height):
        """移动到指定的坐标(相对当前的坐标移动)"""
        js_code = "window.scrollBy({}, {})".format(width, height)
        self.driver.execute_script(js_code)

    def js_move_to_element_top(self, element):
        """移动到元素element对象的“顶端”与当前窗口的“顶部”对齐"""
        js_code = "arguments[0].scrollIntoView()"
        self.driver.execute_script(js_code, element)

    def js_move_to_element_bottom(self, element):
        """移动到元素element对象的“底端”与当前窗口的“底部”对齐"""
        js_code = "arguments[0].scrollIntoView(false);"
        self.driver.execute_script(js_code, element)

    def js_move_to_page_bottom(self):
        """移动到页面最底部"""
        js_code = "window.scrollTo(0, document.body.scrollHeight);"
        self.driver.execute_script(js_code)

    def input_upload_file(self, element, filename):
        """
        input标签上传文件，使用send_keys
        :param element: input上传文件元素
        :param filename: 文件路径
        :return:
        """
        element.send_keys(filename)

    def pyautogui_upload_file(self, filename):
        """
        非input标签上传文件，使用pyautogui方式
        :param element:
        :param filename:
        :return:
        """
        pyautogui.write(filename)
        time.sleep(2)
        # 步骤三：输入回车或点击“打开”按钮
        pyautogui.press("enter", presses=2)  # presses：按1次不会生效，要按2次才会生效
        time.sleep(2)
