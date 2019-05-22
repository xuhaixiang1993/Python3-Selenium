from Common.basePage import BasePage
from selenium.webdriver.common.keys import Keys


class HomePage(BasePage):
    """GitHub主页面"""

    signin_button = ['link', 'Sign in']  # Sign in 按钮
    search = ['name', 'q']  # 搜索框
    tes1 = ['id', 'jump-to-suggestion-search-global']

    def click_sign_in(self):
        """点击Sign in 按钮，跳转登录页面"""
        self.click(self.signin_button)

    def search_for(self, value):
        """输入selenium，并回车"""
        self.type(self.search, value)
        self.click(self.tes1)
