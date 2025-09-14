from base.base_test import BaseTest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.recruitment_page import RecruitmentPage
from time import sleep


class TestOrangeHRM(BaseTest):

    def test_login(self):
        username = "Admin"
        password = "admin123"
        login_page = LoginPage(self.driver)
        login_page.login(username, password)
        dashboard_page = DashboardPage(self.driver)
        assert dashboard_page.dashboard_header_is_displayed() == True

    def test_add_vacancy(self):
        username = "Admin"
        password = "admin123"
        login_page = LoginPage(self.driver)
        login_page.login(username, password)
        dashboard_page = DashboardPage(self.driver)
        dashboard_page.navigate_to_recruitment()
        recruitment_page = RecruitmentPage(self.driver)
        recruitment_page.add_new_vacancy(
            vacancy_name="Test add vacancy",
            job_title="QA Engineer",
            hiring_manager_hint="Test",
            hiring_manager="Orange  Test",
        )
        sleep(5)  # import time
