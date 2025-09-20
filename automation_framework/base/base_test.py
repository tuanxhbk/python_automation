import pytest
from selenium import webdriver
from utils.config_reader import ConfigReader

class BaseTest:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, request):
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless')
        # options.add_argument('--no-sandbox')
        # options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        
        base_url = ConfigReader.get_base_url()
        if base_url:
            driver.get(base_url)
            
        request.cls.driver = driver
        yield
        driver.quit()