# # ！/usr/bin/python3
# -*- coding: utf-8 -*-
# 当前项目名称：Selenium3自动化测试实战
# 文件名称： Test_web.py
# 登录用户名： yanshaoyou
# 作者： 闫少友
# 邮件： 2395969839@qq.com
# 电话：17855503800
# 创建时间： 2021/12/9  13:11
"""
封装测试方法：
    1、访问url
    2、定位页面元素
    3、输入搜索元素
    4、点击搜索
    5、关闭页面
    6、关闭退出
    7、等待操作：强制等待、隐式等待、显示等待
    8、鼠标操作：右击、双击、悬停、拖动
"""
import os

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as ec
from time import sleep
# from log.log import log_show


# log_export = log_show()
# 构造浏览器对象:Chrome（默认）、Firefox、Ie、Edge、Opera等浏览器
def open_browser(name):
    try:
        driver = getattr(webdriver, name)()
    except BaseException as e:
        print("{}\n'{}'浏览器输入错误，请输入正确的浏览器名，默认Chrome。".format(e, name))
        driver = webdriver.Chrome()
    return driver


class BasePage:
    """selenium封装
       1、id：唯一标识，不重复
       2、name：名称标识，可能重复
       3、class：class标识，重复，少用；可使用定位一组元素再通过列表循环等方式定位想要的元素
       4、tag：标签标识，重复，少用；可使用定位一组元素再通过列表循环等方式定位想要的元素
       5、link_text:超链接标识，超链接文本必须写全
       6、partial_link_text：超链接标识，超链接文本可以不写全
       7、xpath：路径标识，
            1、绝对路径；
            2、表达式，按照属性进行定位，格式：[@属性=‘属性值] /根节点，//所有节点，*所有元素，类似正则表达式。
            ps：//*[@id="kw"]
       8、css：调整页面样式标识
            1、属性定位：id、class、标签；id使用#表示，ps：#kw；class使用.,ps:.s_ipt;tag标签，直接使用标签名，ps：input；
            2、层级定位：通过后代元素 元素 后代元素的方式，ps：#head_wrapper .s_btn；
            3、标签与属性组合；ps：input[id='kw']
            注意：python中单引号和双引号的使用。
       9、frame切换/窗口切换：
            总的流程：找到iframe  切换到iframe 内部中  //*所有节点的元素 找到iframe的父类  定位到iframe
            1、找到iframe   ps：//*[@id='loginDiv']/iframe
            2、switch_to.frame，跳转到iframe内部
            3、定位元素即可
            4、switch_to.default_content,跳转到iframe外部
       10、窗口切换：
            1、driver.window_handles,获取打开的所有窗口句柄
            2、可以使用for循环显示窗口
            3、switch_to.window(i),切换到新窗口
            4、driver.title,可以通过窗口名称,判断是否是自己想要的窗口.
       11、单选框：可以使用css进行定位，标签[@属性='属性值']的方式,ps：input[value='peach']；或者其它定位方式
           复选框：
             1、先确定要复选的元素，不选的元素被选了，可再点击一次就不选了
             2、一般checked属性的元素是被选的，可以先把该属性的元素再点击下，就取消转态了，可以使用for循环
             3、再定位要复选的元素，如果不好定位，可以先定位父类再定位子类,父类与子类间用空格隔开，ps：#s_checkbox input[value='peach']
           下拉框：一般先定位父类，再进行元素定位
             1、索引的方式，先获取父类id，再使用select_by_index('i')进行索引定位；
                ps:find_element_by_id('aoe').select_by_index('1')
             2、value值的方式，先获取父类id，再使用select_by_value('peach')进行value定位；
             3、文本值的方式，先获取父类id，再使用select_by_visible_text('桃子')进行文本值定位。
    """
    # 打开浏览器对象
    def __init__(self, name):
        self.driver = open_browser(name)

    # 访问URl
    def open_url(self, name):
        self.driver.get(name)

    # 定位元素,传参写法一，推荐
    def loactor_element(self, name, value):
        # log_export.info('定位元素{} {}'.format(name, value))  # 日志记录
        if name[0] == 's':
            name = name[1:]
            # log_export.info('定位元素{} {}'.format(name, value))  # 日志记录
            return self.driver.find_elements(name, value)
        else:
            return self.driver.find_element(name, value)

    # 定位元素,传参写法二，推荐
    # def loactor_element(self, *args):
    #     """定位元素"""
    #     return self.driver.find_element(*args)

    # 定位元素,传参写法三
    # def loactor_element(self, args):
    #     """定位元素"""
    #     return self.driver.find_element(*args)

    # 常用方法，可以直接使用原装方法或封装方法：清除文本、按钮输入、点击、提交、尺寸、文本、属性值、是否可见、标题、URL、ID、位置、标签名
    # 清除文本
    def clear_element(self, name, value):
        self.loactor_element(name, value).clear()

    # 输入元素
    def input_element(self, name, value, txt):
        self.loactor_element(name, value).send_keys(txt)

    # 默认点击搜索，有第三个参数时，启用回车提交表单
    def click_element(self, name, value, *args):
        if args:
            click = self.loactor_element(name, value).submit()
        else:
            click = self.loactor_element(name, value).click()
        return click

    # 返回元素尺寸
    def size_element(self, name, value):
        return self.loactor_element(name, value).size

    # 获取元素文本
    def text_element(self, name, value):
        return self.loactor_element(name, value).text

    # 获取元素属性值
    def attribute_element(self, name, value):
        return self.loactor_element(name, value).get_attribute('type')

    # 设置该元素是否用户可见
    def display_element(self, name, value):
        return self.loactor_element(name, value).is_displayed()

    # 获取标题
    def title_page(self):
        return self.driver.title

    # 获取URL
    def current_url_page(self):
        return self.driver.current_url

    # 获取id
    def get_id(self, name, value):
        return self.loactor_element(name, value).id

    # 获取元素位置
    def get_location(self, name, value):
        return self.loactor_element(name, value).location

    # 获取元素标签名
    def get_tag_name(self, name, value):
        return self.loactor_element(name, value).tag_name

    # 关闭页面
    def close_browser(self):
        self.driver.close()

    # 关闭退出
    def quit_browser(self):
        self.driver.quit()

    # 封装命名规则，直译_原先方法名称；可以加强理解与原先方法名称的认识
    # 浏览器控制封装：窗口尺寸(默认全屏）、前进、后退、刷新
    # 窗口尺寸，默认全屏
    def window_size(self, *args):
        if args:
            self.driver.set_window_size(*args)
        else:
            self.driver.maximize_window()

    # 窗口前进
    def window_forward(self):
        self.driver.forward()

    # 窗口后退
    def window_back(self):
        self.driver.back()

    # 窗口刷新
    def window_refresh(self):
        self.driver.refresh()

    # 等待操作封装：强制等待、隐式等待、显示等待
    # 强制等待
    def sleep_time(self, txt):
        sleep(txt)

    # 隐式等待
    def implicit_implicitly_wait(self, txt):
        self.driver.implicitly_wait(txt)

    # 显示等待1，一般写法
    def display_wait1(self, name, value, txt, rate):
        locator = (name, value)
        WebDriverWait(self.driver, txt, rate).until(ec.presence_of_element_located(locator))

    # 显示等待2，写法不同，推荐
    def display_wait2(self, name, value, txt, rate):
        WebDriverWait(self.driver, txt, rate).until(lambda el: self.loactor_element(name, value))

    # 鼠标操作封装：单击（左击）、双击、右击、拖动、悬停。。。
    # 鼠标左击，单击
    def left_click(self, name, value):
        ActionChains(self.driver).click(self.loactor_element(name, value)).perform()

    # 鼠标左击，不松开
    def left_click_and_hold(self, name, value):
        ActionChains(self.driver).click_and_hold(self.loactor_element(name, value)).perform()

    # 鼠标左击，双击
    def left_double_click(self, name, value):
        ActionChains(self.driver).double_click(self.loactor_element(name, value)).perform()

    # 鼠标右击，单击
    def right_context_click(self, name, value):
        ActionChains(self.driver).context_click(self.loactor_element(name, value)).perform()

    # 鼠标拖动，拖拽到某个元素然后松开
    def mouse_drag_to_drop(self, name, value, name1, value1):
        ActionChains(self.driver).drag_and_drop(self.loactor_element(name, value), self.loactor_element(name1, value1)).perform()

    # 鼠标悬停,移动到某个元素
    def hover_move_to_element(self, name, value):
        ActionChains(self.driver).move_to_element(self.loactor_element(name, value)).perform()

    # 鼠标从当前位置移动到某个坐标
    def mouse_move_by_offset(self, coord1, coord2):
        ActionChains(self.driver).move_by_offset(coord1, coord2).perform()

    # 移动到距某个元素（左上角坐标）多少距离的位置
    def mouse_move_to_element_with_offset(self, name, value, coord1, coord2):
        ActionChains(self.driver).move_to_element_with_offset(self.loactor_element(name, value), coord1, coord2).perform()

    # 拖拽到某个坐标然后松开
    def mouse_drag_and_drop_by_offset(self, name, value, coord1, coord2):
        ActionChains(self.driver).move_to_element_with_offset(self.loactor_element(name, value), coord1, coord2).perform()

    # 按下某个键盘上的键
    def mouse_key_down(self, *args):
        ActionChains(self.driver).key_down(*args).perform()

    # 松开某个键
    def mouse_key_up(self, *args):
        ActionChains(self.driver).key_up(*args).perform()

    # 释放鼠标，在某个元素位置松开鼠标左键
    def mouse_release(self, *args):
        ActionChains(self.driver).release(*args)

    # 键盘操作封装：键盘操作可直接使用原装方法
    # 之后可思考更优化的方法
    # 发送某个键到当前焦点的元素
    def keyboard_handle(self, name, value, *args):
        self.loactor_element(name, value).send_keys(*args)

    # 多表单切换封装：跳转到iframe中、跳转到iframe外部
    # 表单切换一般步骤：1、找到iframe位置；2、跳转到内部；3、找到要定位的元素；4、跳转到iframe外部
    # 跳转到iframe中
    def switch_to_frame(self, name, value):
        self.driver.switch_to.frame(self.loactor_element(name, value))

    # 跳转到iframe外部
    def default_switch_to(self):
        self.driver.switch_to.default_content()

    # 多窗口切换封装：获取当前窗口句柄、返回所有窗口句柄到当前会话、切换到相应窗口
    # 获取当前窗口句柄,
    def get_current_window_handle(self):
        return self.driver.current_window_handle

    # 获取所有窗口句柄
    def get_window_handle(self):
        return self.driver.window_handles

    # 切换到相应窗口
    def switch_to_window(self, txt):
        self.driver.switch_to.window(txt)

    # 待验证，警告框处理封装：alert、confirm、prompt
    # 主要操作方法：text（获取文本信息）、accept（OK）、dismiss（取消）、send_keys(输入信息）
    # alert，显示消息、OK对话框
    def switch_to_alert(self, *args):
        if args == 'text':
            return self.driver.switch_to.alert.text
        elif args == 'accept':
            return self.driver.switch_to.alert.accept()
        elif args == 'dismiss':
            return self.driver.switch_to.alert.dismiss()
        else:
            return self.driver.switch_to.alert.send_keys()

    # 待验证，下拉框处理封装：select定位select标签，value、text、index
    # 根据value值定位
    def get_select_value(self, name, value, txt):
        return Select(self.loactor_element(name, value)).select_by_value(txt)

    # 根据text值定位
    def get_select_text(self, name, value, txt):
        return Select(self.loactor_element(name, value)).select_by_visible_text(txt)

    # 根据index值定位
    def get_select_index(self, name, value, txt):
        return Select(self.loactor_element(name, value)).select_by_index(txt)

    # 上传文件封装：普通上传（通过input、form、send_keys等标签上传）、插件上传（Flash/JavaScript/Ajax等技术实现）
    #


    # 待验证，下载文件封装：Firefox浏览器下载、Chrome浏览器下载
    # Firefox浏览器文件下载
    def firefox_download_file(self, name, value, txt):
        fp = webdriver.FirefoxProfile()
        fp.set_preference("browser.download.folderList", 2)  # 2，下载到指定目录；0，下载到默认路径
        fp.set_preference("browser.download.dir", os.getcwd())  # browser.download.dir
        fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "binary/octet-stream")
        self.driver = webdriver.Firefox(firefox_profile=fp)
        self.open_url(txt)
        return self.click_element(name, value)

    # Chrome浏览器文件下载
    def chrome_download_file(self, name, value, txt):
        options = webdriver.ChromeOptions()
        prefs = {'profile.default_content_settings.popups': 0,
                 'download.default_directory': os.getcwd()}  # 0,设置禁止弹出下载窗口
        options.add_experimental_option('prefs', prefs)
        self.driver = webdriver.Chrome(chrome_options=options)
        self.open_url(txt)
        return self.click_element(name, value)

    # 待验证，Cookie操作封装：Cookie（存储文本或其它信息,一般以字典存储）、获取所有cookie、获取特定cookie、添加cookie、删除特定cookie、删除所有cookie
    # 获取所有cookie
    def cookie_get_cookies(self):
        return self.driver.get_cookies()

    # 获取特定cookie
    def cookie_get_cookie(self, name):
        return self.driver.get_cookie(name)

    # 添加cookie
    def cookie_add_cookie(self, *args):
        self.driver.add_cookie(*args)

    # 删除特定cookie
    def cookie_delete_cookie(self, name):
        self.driver.delete_cookie(name)

    # 删除所有cookie
    def cookie_delete_cookies(self):
        self.driver.delete_all_cookies()

    # 调用JavaScript封装：浏览器滚动条拖动、输入页面中的textarea文本框内容
    # 浏览器滚动条拖动
    def execute_script_scrollbar(self, name, value):
        self.driver.execute_script("window.scrollTo({},{});".format(name, value))

    # 输入页面中的textarea文本框内容
    def execute_script_textarea(self, name, value, txt):
        self.driver.execute_script("document.getElementBy{}('{}').value='{}';".format(name, value, txt))

    # 出来HTML5视频播放封装：加载、播放、暂停
    # 返回文件播放地址
    def video_url(self, name, vaule):
        video = self.loactor_element(name, vaule)
        return self.driver.execute_script("return arguments[0].currentSrc;", video)

    # 视频加载
    def video_load(self, name, vaule):
        self.driver.execute_script("arguments[0].load()", self.loactor_element(name, vaule))

    # 视频播放
    def video_play(self, name, vaule):
        self.driver.execute_script("arguments[0].play()", self.loactor_element(name, vaule))

    # 视频暂停
    def video_pause(self, name, vaule):
        self.driver.execute_script("arguments[0].pause()", self.loactor_element(name, vaule))

    # 视频停止
    def video_stop(self, name, vaule):
        self.driver.execute_script("arguments[0].stop()", self.loactor_element(name, vaule))

    # 滑动解锁封装：水平滑动(左右滑动)、垂直滑动(上下滑动)，可以考虑通过上方的鼠标移动操作组合进行水平、垂直滑动
    # 滑动，TouchActions类方式
    def scroll_from_element(self, name, value, coord1, coord2):
        webdriver.TouchActions(self.driver).scroll_from_element(self.loactor_element(name, value), coord1, coord2).perform()

    # 窗口截图封装：save_screenshot
    # 截图保存
    def picture_save_screenshot(self, name):
        self.driver.save_screenshot(name)














