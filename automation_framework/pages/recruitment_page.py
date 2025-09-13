from selenium.webdriver.common.by import By
from base.base_page import BasePage
from selenium.webdriver.support.ui import Select

class RecruitmentPage(BasePage):
    VACANCIES_LINK = (By.XPATH, "//a[text()='Vacancies']")
    ADD_VACANCIES_BUTTON = (By.XPATH, "//button[contains(.,'Add')]")
    VACANCY_NAME_INPUT = (By.XPATH, "//label[contains(.,'Vacancy Name')]/parent::div/following-sibling::div/input")
    JOB_TITLE_ARROW_DOWN = (By.XPATH, "//label[contains(.,'Job Title')]/parent::div/following-sibling::div//i[contains(@class,'oxd-select-text--arrow')]")
    JOB_TITLE_SELECT = (By.XPATH, "//div[@role='listbox']")

    def __init__(self, driver):
        super().__init__(driver)

    def click_vacancies_link(self):
        self.click(self.VACANCIES_LINK)
    
    def click_add_vacancies_button(self):
        self.click(self.ADD_VACANCIES_BUTTON)
    
    def set_vacancy_name(self, text):
        self.set_text(self.VACANCY_NAME_INPUT, text)
    
    def click_job_title_arrow_down(self):
        self.click(self.JOB_TITLE_ARROW_DOWN)
        
    def select_job_title(self, job_title):
        self.click_job_title_arrow_down()
        job_title_select = Select(self.get_element(self.JOB_TITLE_SELECT))
        job_title_select.select_by_visible_text(job_title)
        # job_title_xpath_value = 

    def add_new_vacancies(self, vacancy_name, job_title):
        self.click_vacancies_link()
        self.click_add_vacancies_button()
        self.set_vacancy_name(vacancy_name)
        self.select_job_title(job_title)