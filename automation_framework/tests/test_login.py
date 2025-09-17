from base.base_test import BaseTest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


class TestLoginOrangeHRM(BaseTest):

    def test_login(self):
        username = "Admin"
        password = "admin123"

        login_page = LoginPage(self.driver)
        login_page.login(username, password)
        dashboard_page = DashboardPage(self.driver)
        assert dashboard_page.dashboard_header_is_displayed() == True
