from selenium.webdriver.common.by import By
from base.base_page import BasePage
from selenium.webdriver.support.ui import Select


class RecruitmentPage(BasePage):
    VACANCIES_LINK = (By.XPATH, "//a[text()='Vacancies']")
    ADD_VACANCIES_BUTTON = (By.XPATH, "//button[contains(.,'Add')]")
    VACANCY_NAME_INPUT = (
        By.XPATH,
        "//label[contains(.,'Vacancy Name')]/parent::div/following-sibling::div/input"
    )
    JOB_TITLE_ARROW_DOWN = (
        By.XPATH,
        "//label[contains(.,'Job Title')]/parent::div/following-sibling::div//i[contains(@class,'oxd-select-text--arrow')]"
    )
    DESCRIPTION_TEXTAREA = (
        By.XPATH,
        "//textarea[@placeholder='Type description here']"
    )
    NUMBER_OF_POSITIONS_INPUT = (
        By.XPATH,
        "//label[contains(.,'Number of Positions')]/parent::div/following-sibling::div/input"
    )
    HIRING_MANAGER_INPUT = (
        By.XPATH,
        "//label[contains(.,'Hiring Manager')]/parent::div/following-sibling::div//input[contains(@placeholder,'Type for hints')]"
    )
    CANCEL_BUTTON = (By.XPATH, "//button[contains(.,'Cancel')]")
    SAVE_BUTTON = (By.XPATH, "//button[contains(.,'Save')]")
    USERNAME_DROPDOWN = (By.XPATH, "//p[@class='oxd-userdropdown-name']")

    def __init__(self, driver):
        super().__init__(driver)

    def click_vacancies_link(self):
        self.click(self.VACANCIES_LINK)

    def click_add_vacancy_button(self):
        self.click(self.ADD_VACANCIES_BUTTON)

    def set_vacancy_name(self, vacancy_name: str):
        self.send_keys(self.VACANCY_NAME_INPUT, vacancy_name)

    def click_job_title_arrow_down(self):
        self.click(self.JOB_TITLE_ARROW_DOWN)

    def select_job_title(self, job_title: str):
        job_title_xpath_value = (
            "//div[@class='oxd-select-wrapper']//div[@role='listbox']//div[@role='option']//span[.='"
            + job_title
            + "']"
        )
        self.click((By.XPATH, job_title_xpath_value))

    def set_description(self, description: str):
        self.send_keys(self.DESCRIPTION_TEXTAREA, description)

    def set_number_of_positions(self, number_of_positions: int):
        self.send_keys(self.NUMBER_OF_POSITIONS_INPUT, str(number_of_positions))

    def select_hiring_manager(self):
        current_username = self.find_element(self.USERNAME_DROPDOWN).text
        self.send_keys(self.HIRING_MANAGER_INPUT, current_username)
        hiring_manager_listbox_span_xpath_value = "//div[@role='listbox']/div/span"
        self.click((By.XPATH, hiring_manager_listbox_span_xpath_value))

    def click_save_button(self):
        self.click(self.SAVE_BUTTON)

    def add_new_vacancy(self, vacancy_name: str, job_title: str, description: str = "", number_of_positions: int = 1):
        self.click_vacancies_link()
        self.click_add_vacancy_button()
        self.set_vacancy_name(vacancy_name)
        self.click_job_title_arrow_down()
        self.select_job_title(job_title)
        self.set_description(description)
        self.set_number_of_positions(number_of_positions)
        self.select_hiring_manager()
        self.click_save_button()
