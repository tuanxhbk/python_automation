from selenium.webdriver.common.by import By
from time import sleep
from base.base_page import BasePage


class DashboardPage(BasePage):
    DASHBOARD_HEADER = (
        By.XPATH,
        "//header[contains(@class,'topbar')]//*[text()='Dashboard']"
    )
    RECRUITMENT_SPAN = (By.XPATH, "//span[text()='Recruitment']")

    # def __init__(self, driver):
    #     self.driver = driver

    def dashboard_header_is_displayed(self):
        dashboard_header = self.driver.find_element(*self.DASHBOARD_HEADER)
        return dashboard_header.is_displayed()

    def navigate_to_recruitment(self):
        recruitment_span = self.driver.find_element(*self.RECRUITMENT_SPAN)
        recruitment_span.click()
        sleep(2)
