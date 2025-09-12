from selenium.webdriver.common.by import By
from time import sleep
from automation_framework.base.base_page import BasePage


class LoginPage(BasePage):
    USERNAME_INPUT = (By.XPATH, "//input[@name='username']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")

    # def __init__(self, driver):
    #     self.driver = driver

    def enter_username(self, username):
        username_input = self.driver.find_element(*self.USERNAME_INPUT)
        username_input.send_keys(username)

    def enter_password(self, password):
        password_input = self.driver.find_element(*self.PASSWORD_INPUT)
        password_input.send_keys(password)

    def click_login(self):
        login_button = self.driver.find_element(*self.LOGIN_BUTTON)
        login_button.click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        sleep(5)
