import requests
import json


class APIHelper:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip('/')

    def _send_request(self, method: str, endpoint: str, headers: dict = None, params: dict = None, data: dict = None):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        method_map = {
            "GET": requests.get,
            "POST": requests.post,
            "PUT": requests.put,
            "DELETE": requests.delete
        }
        if method not in method_map:
            raise ValueError(f"Unsupported HTTP method: {method}")
        try:
            if method == "GET":
                response = method_map[method](url, headers=headers, params=params)
            else:
                response = method_map[method](url, headers=headers, params=params, data=data)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"API request failed: {e}")
            return None

    def get(self, endpoint: str, headers: dict = None, params: dict = None) -> requests.Response:
        return self._send_request("GET", endpoint, headers, params)

    def post(self, endpoint: str, headers: dict = None, params: dict = None, data: dict = None) -> requests.Response:
        return self._send_request("POST", endpoint, headers, params, data)

    def put(self, endpoint: str, headers: dict = None, params: dict = None, data: dict = None) -> requests.Response:
        return self._send_request("PUT", endpoint, headers, params, data)

    def delete(self, endpoint: str, headers: dict = None, params: dict = None, data: dict = None) -> requests.Response:
        return self._send_request("DELETE", endpoint, headers, params, data)

    def assert_status_code(self, response: requests.Response, expected_status_code: int):
        assert response is not None, "No response returned from API request."
        assert response.status_code == expected_status_code, (
            f"Expected status code {expected_status_code}, but got {response.status_code}"
        )

    def get_json_value(self, response: requests.Response, key: str):
        try:
            json_data = response.json()
            # Support nested keys like 'data.user.id'
            keys = key.split('.')
            for k in keys:
                if isinstance(json_data, dict):
                    json_data = json_data.get(k)
                else:
                    return None
            return json_data
        except (json.JSONDecodeError, ValueError):
            print("Response is not in JSON format")
            return None