from base.base_test import BaseTest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.recruitment_page import RecruitmentPage

class TestOrangeHRM(BaseTest):

    def test_login(self):
        username = "Admin"
        password = "admin123"
        login_page = LoginPage(self.driver)
        login_page.login(username, password)
        dashboard_page = DashboardPage(self.driver)
        dashboard_page.verify_on_dashboard_page()
        
    def test_add_vacancies(self):
        username = "Admin"
        password = "admin123"
        login_page = LoginPage(self.driver)
        login_page.login(username, password)
        dashboard_page = DashboardPage(self.driver)
        dashboard_page.navigate_to_recruitment()
        recruitment_page = RecruitmentPage(self.driver)
        recruitment_page.add_new_vacancies()