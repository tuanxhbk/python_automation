from base.base_test import BaseTest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.recruitment_page import RecruitmentPage
from time import sleep
from datetime import datetime


class TestVacancies(BaseTest):

    def test_add_vacancy(self):
        username = "Admin"
        password = "admin123"
        vacancy_name = "Test add vacancy " + str(datetime.now())
        job_title = "QA Engineer"
        description = "This is a test vacancy added by automation."
        number_of_positions = 3
        login_page = LoginPage(self.driver)
        login_page.login(username, password)
        dashboard_page = DashboardPage(self.driver)
        dashboard_page.navigate_to_recruitment()
        recruitment_page = RecruitmentPage(self.driver)
        recruitment_page.add_new_vacancy(vacancy_name, job_title, description, number_of_positions )

        sleep(5)  # import time
