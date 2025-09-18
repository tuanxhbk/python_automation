from base.base_api_test import BaseAPITest

class TestAPI(BaseAPITest):

    def test_get_user_info(self):
        endpoint = "users/2"
        expected_status_code = 200
        response = self.api_helper.get(endpoint=endpoint)
        self.api_helper.assert_status_code(response, expected_status_code=expected_status_code)
        data = self.api_helper.get_json_value(response, "data")
        assert data["id"] == 2

    def test_create_user(self):
        payload = {"name": "morpheus", "job": "leader"}
        endpoint = "users"
        expected_status_code = 201
        response = self.api_helper.post(endpoint=endpoint, headers=self.custom_headers, data=payload)
        self.api_helper.assert_status_code(response, expected_status_code=expected_status_code)
