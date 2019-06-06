import unittest

from Common.basePage import BasePage
from PageObject.homePage import HomePage
from PageObject.loginPage import LoginPage
from Common.log import log1


class TestLogin(unittest.TestCase):
    """测试登录"""

    @classmethod
    def setUpClass(cls):
        browser = BasePage(cls)
        cls.driver = browser.open_browser()
        home = HomePage(cls.driver)
        home.click_sign_in()

    @classmethod
    def tearDownClass(cls):
        login = LoginPage(cls.driver)
        login.dr_quit()

    def test_login1(self):
        """用户名为空"""
        case_name = '用户为空'
        log1.info("执行测试用例：%s" % case_name)
        login = LoginPage(self.driver)
        login.login(' ', '12324')
        error_text = login.get_login_error()
        try:
            self.assertEqual(error_text, 'Incorrect username or password.')
            log1.info("测试用例执行成功:%s" % case_name + '\n')
        except AssertionError:
            log1.error("测试用例执行失败:%s" % case_name + '\n')
            raise

    def test_login2(self):
        """密码为空"""
        case_name = '密码为空'
        log1.info("执行测试用例：%s" % case_name)
        login = LoginPage(self.driver)
        login.login('xuhaixiang1993', '')
        error_text = login.get_login_error()
        try:
            self.assertEqual(error_text, 'Incorrect username or password.')
            log1.info("测试用例执行成功:%s" % case_name + '\n')
        except AssertionError:
            log1.error("测试用例执行失败:%s" % case_name + '\n')
            raise

    def test_login3(self):
        """密码不正确"""
        case_name = '密码不正确'
        log1.info("执行测试用例：%s" % case_name)
        login = LoginPage(self.driver)
        login.login('xuhaixiang1993', ' 12314')
        error_text = login.get_login_error()
        try:
            self.assertEqual(error_text, 'Incorrect username or password.')
            log1.info("测试用例执行成功:%s" % case_name + '\n')
        except AssertionError:
            log1.error("测试用例执行失败:%s" % case_name + '\n')
            raise

    def test_login4(self):
        """登录成功"""
        # 想要执行成功，需使用GitHub账号和密码
        case_name = '登录成功'
        log1.info("执行测试用例：%s" % case_name)
        login = LoginPage(self.driver)
        login.login('username', 'password')
        login_title = login.get_title()
        try:
            self.assertEqual(login_title, 'GitHub')
            log1.info("测试用例执行成功:%s" % case_name+'\n')
        except AssertionError:
            log1.error("测试用例执行失败:%s" % case_name+'\n')
            raise
