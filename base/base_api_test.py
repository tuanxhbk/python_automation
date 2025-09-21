from helper.api_helper import APIHelper
import pytest


class BaseAPITest:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.api_helper = APIHelper(base_url="https://reqres.in/api")
        self.custom_headers = {"x-api-key": "reqres-free-v1"}
        yield
