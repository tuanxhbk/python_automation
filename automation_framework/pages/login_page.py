from selenium.webdriver.common.by import By
from base.base_page import BasePage


class LoginPage(BasePage):
    USERNAME_INPUT = (By.XPATH, "//input[@name='username']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")

    def __init__(self, driver):
        super().__init__(driver)

    def enter_username(self, username):
        self.set_text(self.USERNAME_INPUT, username)

    def enter_password(self, password):
        self.set_text(self.PASSWORD_INPUT, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)
        

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
