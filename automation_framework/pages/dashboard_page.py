from selenium.webdriver.common.by import By
from base.base_page import BasePage


class DashboardPage(BasePage):
    DASHBOARD_HEADER = (
        By.XPATH,
        "//header[contains(@class,'topbar')]//*[text()='Dashboard']"
    )
    RECRUITMENT_SPAN = (By.XPATH, "//span[text()='Recruitment']")

    def __init__(self, driver):
        super().__init__(driver)

    def dashboard_header_is_displayed(self):
        dashboard_header = self.find_element(self.DASHBOARD_HEADER)
        return dashboard_header.is_displayed()

    def navigate_to_recruitment(self):
        self.click(self.RECRUITMENT_SPAN)
