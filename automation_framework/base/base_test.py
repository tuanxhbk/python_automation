import pytest
from selenium import webdriver

class BaseTest:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, request):
        options = webdriver.ChromeOptions()
        #options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        request.cls.driver = driver
        yield
        driver.quit()