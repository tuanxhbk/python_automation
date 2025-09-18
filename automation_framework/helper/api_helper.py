import requests
import json

class APIHelper:
    def __init__(self, base_url):
        self.base_url = base_url

    def _send_request(self, method, endpoint, headers=None, params=None, data=None):
        url = f"{self.base_url}/{endpoint}"
        try:
            if method == "GET":
                response = requests.get(url, headers=headers, params=params, data=data)
            elif method == "POST":
                response = requests.post(url, headers=headers, params=params, data=data)
            elif method == "PUT":
                response = requests.put(url, headers=headers, params=params, data=data)
            elif method == "DELETE":
                response = requests.delete(url, headers=headers, params=params, data=data)
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")
            return response
        except requests.exceptions.RequestException as e:
            print(f"API request failed: {e}")
            return None
        
    def get(self, endpoint, headers=None, params=None, data=None):
        return self._send_request("GET", endpoint, headers, params, data)
    
    def post(self, endpoint, headers=None, params=None, data=None):
        return self._send_request("POST", endpoint, headers, params, data)
    
    def put(self, endpoint, headers=None, params=None, data=None):
        return self._send_request("PUT", endpoint, headers, params, data)
    
    def delete(self, endpoint, headers=None, params=None, data=None):
        return self._send_request("DELETE", endpoint, headers, params, data)
    
    def assert_status_code(self, response, expected_status_code):
        assert response.status_code == expected_status_code, \
            f"Expected status code {expected_status_code}, but got {response.status_code}"
        
    def get_json_value(self, response, key):
        try:
            json_data = response.json()
            return json_data.get(key)
        except json.JSONDecodeError:
            print("Response is not in JSON format")
            return None