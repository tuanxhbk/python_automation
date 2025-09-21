import pytest
from base.base_test import BaseTest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils.config_reader import ConfigReader


class TestLoginOrangeHRM(BaseTest):

    @pytest.mark.smoke
    def test_login(self):
        username = ConfigReader.get_username()
        password = ConfigReader.get_password()

        login_page = LoginPage(self.driver)
        login_page.login(username, password)
        dashboard_page = DashboardPage(self.driver)
        assert dashboard_page.dashboard_header_is_displayed() == True
