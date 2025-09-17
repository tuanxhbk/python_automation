from selenium.webdriver.common.by import By
from base.base_test import BaseTest
from time import sleep


class TestOrangeHRM(BaseTest):
    USERNAME_INPUT = (By.XPATH, "//input[@name='username']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")

    def test_login(self):
        username = self.driver.find_element(*self.USERNAME_INPUT)
        username.send_keys("Admin")
        password = self.driver.find_element(*self.PASSWORD_INPUT)
        password.send_keys("admin123")
        login_button = self.driver.find_element(*self.LOGIN_BUTTON)
        login_button.click()
        sleep(5)
