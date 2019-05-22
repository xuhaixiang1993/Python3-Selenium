import os
import time
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver

import getcwd
from Logs.log import log1
from Config.config import Config

path = getcwd.get_cwd()
config = Config()


class BasePage:
    """测试基类"""
    def __init__(self, driver):
        self.driver = driver

    def get_img(self):
        """截图"""
        jt_path = os.path.join(getcwd.get_cwd(), 'img/')
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        img_name = jt_path+rq+'.png'
        # noinspection PyBroadException
        try:
            self.driver.get_screenshot_as_file(img_name)
            log1.info('截图保存成功')
        except BaseException:
            log1.error('截图失败', exc_info=1)

    def open_browser(self):
        """打开浏览器，访问url"""
        browser = config.config_read('environment', 'browser')
        log1.info('读取浏览器配置,值为%s' % browser)
        url = config.config_read('environment', 'url')
        log1.info('读取url,值为%s' % url)
        # noinspection PyBroadException
        try:
            if browser == 'chrome':
                option = webdriver.ChromeOptions()
                option.add_argument('disable-infobars')
                self.driver = webdriver.Chrome(chrome_options=option)
                log1.info('打开chrome浏览器')
            elif browser == 'firefox':
                self.driver = webdriver.Firefox()
                log1.info('打开firefox浏览器')
            else:
                log1.error('浏览器配置有误，应为chrome或firefox')
            self.driver.get(url)
            log1.info('访问url')
            self.driver.maximize_window()
            log1.info('浏览器最大化')
            self.driver.implicitly_wait(10)
            log1.info('设置静态等待时间10秒')
            return self.driver
        except BaseException:
            log1.error('浏览器打开报错', exc_info=1)

    def get_element(self, selector):
        """定位元素"""
        by = selector[0]
        value = selector[1]
        bys = ['id', 'name', 'class', 'tag', 'link', 'plink', 'css', 'xpath']
        element = None
        if by in bys:
            try:
                if by == 'id':
                    element = self.driver.find_element_by_id(value)
                elif by == 'name':
                    element = self.driver.find_element_by_name(value)
                elif by == 'class':
                    element = self.driver.find_element_by_class_name(value)
                elif by == 'tag':
                    element = self.driver.find_element_by_tag_name(value)
                elif by == 'link':
                    element = self.driver.find_element_by_link_text(value)
                elif by == 'plink':
                    element = self.driver.find_element_by_partial_link_text(value)
                elif by == 'css':
                    element = self.driver.find_element_by_css_selector(value)
                elif by == 'xpath':
                    element = self.driver.find_element_by_xpath(value)
                log1.info('元素定位成功。定位方式：%s，使用的值：%s' % (by, value))
                return element
            except NoSuchElementException:
                log1.error('没有定位到元素,定位方式：%s，使用的值：%s' % (by, value), exc_info=1)
        else:
            log1.error('元素定位方式错误，请使用id，name，class，tag，link，plink，css，xpath为定位方式参数')

    @staticmethod
    def isdisplayed(element):
        """元素是否存在"""
        value = element.is_displayed()
        return value

    def type(self, selector, value):
        """往输入框输入内容"""
        element = self.get_element(selector)
        element.clear()
        # noinspection PyBroadException
        try:
            element.send_keys(value)
            log1.info('输入的内容：%s' % value)
        except BaseException:
            log1.error('内容输入报错', exc_info=1)
            self.get_img()

    def click(self, selector):
        """点击元素"""
        element = self.get_element(selector)
        # noinspection PyBroadException
        try:
            element.click()
            log1.info('点击元素成功')
        except BaseException:
            isdisplay = self.isdisplayed(element)
            if isdisplay is True:
                self.my_sleep(3)
                element.click()
                log1.info('点击元素成功')
            else:
                log1.error('点击元素报错', exc_info=1)

    @staticmethod
    def my_sleep(secondes):
        """强制等待"""
        time.sleep(secondes)
        log1.info('强制等待%d秒' % secondes)

    def get_title(self):
        """获取title"""
        title = self.driver.title
        log1.info('当前打开的title是：%s' % title)
        return title

    def get_text(self, selector):
        """获取text"""
        element = self.get_element(selector)
        text = element.text
        log1.info("获取的text：%s" % text)
        return text

    def use_js(self, js):
        """调用js"""
        # noinspection PyBroadException
        try:
            self.driver.execute_script(js)
            log1.info('js执行成功，js内容为：%s' % js)
        except BaseException:
            log1.error('js执行报错', exc_info=1)

    def switch_menue(self, parentelement, secelement, targetelement):
        """三级菜单切换"""
        self.my_sleep(3)
        # noinspection PyBroadException
        try:
            self.driver.switch_to_default_content()
            self.click(parentelement)
            log1.info('成功点击一级菜单：%s' % parentelement)
            self.click(secelement)
            log1.info('成功点击二级菜单：%s' % secelement)
            self.click(targetelement)
            log1.info('成功点击三级菜单：%s' % targetelement)
        except BaseException:
            log1.error('切换菜单报错', exc_info=1)

    def switch_ifarme(self, selector):
        """切换farm"""
        element = self.get_element(selector)
        # noinspection PyBroadException
        try:
            self.driver.switch_to.frame(element)
            log1.info('切换frame成功')
        except BaseException:
            log1.error('切换frame报错', exc_info=1)

    def get_handle(self):
        """获得当前handle"""
        handle = self.driver.current_window_handle
        return handle

    def chage_handle(self, handle):
        """切换窗口"""
        handles = self.driver.window_handles
        for i in handles:
            if i != handle:
                self.driver.switch_to_window(i)

    def dr_quit(self):
        self.driver.quit()