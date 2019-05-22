from Common.basePage import BasePage


class LoginPage(BasePage):
    """login页面"""

    Username = ['id', 'login_field']  # 用户名输入框
    Password = ['id', 'password']  # 密码输入框
    Sign_button = ['name', 'commit']  # 登录按钮
    Forgot_password = ['link', 'Forgot password?']  # 忘记密码按钮
    login_error = ['id', 'js-flash-container']  # 错误提示

    def type_username(self, value):
        """输入用户名"""
        self.type(self.Username, value)

    def type_password(self, value):
        """输入密码"""
        self.type(self.Password, value)

    def click_sign(self):
        """点击登录按钮"""
        self.click(self.Sign_button)

    def get_login_error(self):
        """错误提示信息"""
        error_text = self.get_text(self.login_error)
        return error_text

    def click_forgot_password(self):
        """点击忘记密码按钮"""
        self.click(self.Forgot_password)
