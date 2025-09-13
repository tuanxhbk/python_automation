import pytest
from selenium import webdriver

class BaseTest:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, request):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        request.cls.driver = driver
        yield
        driver.quit()