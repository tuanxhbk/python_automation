from selenium.webdriver.common.by import By
from time import sleep
from base.base_page import BasePage

class RecruitmentPage(BasePage):
    VACANCIES_LINK = (By.XPATH, "//a[text()='Vacancies']")
    ADD_VACANCIES_BUTTON = (By.XPATH, "//button[contains(.,'Add')]")

    # def __init__(self, driver):
    #     self.driver = driver

    def click_vacancies_link(self):
        vacancies_link = self.driver.find_element(*self.VACANCIES_LINK)
        vacancies_link.click()
        sleep(2)
    
    def click_add_vacancies_button(self):
        add_vacancies_button = self.driver.find_element(*self.ADD_VACANCIES_BUTTON)
        add_vacancies_button.click()
        sleep(2)

    def add_new_vacancies(self):
        self.click_vacancies_link()
        self.click_add_vacancies_button()