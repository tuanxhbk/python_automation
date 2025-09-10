from base.base_test import BaseTest
from pages.login_page import LoginPage

class TestOrangeHRM(BaseTest):

    def test_login(self):
        username = "Admin"
        password = "admin123"
        login_page = LoginPage(self.driver)
        login_page.login(username, password)