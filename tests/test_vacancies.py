import pytest
from base.base_test import BaseTest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.recruitment_page import RecruitmentPage
from datetime import datetime
from utils.config_reader import ConfigReader


class TestVacancies(BaseTest):

    #@pytest.mark.smoke
    def test_add_vacancy(self):
        # Set test data
        username = ConfigReader.get_username()
        password = ConfigReader.get_password()
        vacancy_name = "Test add vacancy " + str(datetime.now())
        job_title = "QA Engineer"
        description = "This is a test vacancy added by automation."
        number_of_positions = 3
        
        login_page = LoginPage(self.driver)
        login_page.login(username, password)
        dashboard_page = DashboardPage(self.driver)
        dashboard_page.navigate_to_recruitment()
        recruitment_page = RecruitmentPage(self.driver)
        recruitment_page.add_new_vacancy(vacancy_name, job_title, description, number_of_positions)
        assert recruitment_page.verify_on_edit_vacancy_page() == True, "Failed to add new vacancy"
        recruitment_page.click_cancel_button()
        assert recruitment_page.verify_on_vacancies_page() == True, "Failed to return to Vacancies page"
        recruitment_page.search_vacancy(job_title=job_title)
        assert recruitment_page.verify_vacancy_in_results(vacancy_name) == True, "Vacancy not found in search results"
