import requests


def test_get_user_info():
    response = requests.get("https://reqres.in/api/users/2")
    assert response.status_code == 200
    data = response.json()


def test_create_user():
    login_payload = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
    login_response = requests.post("https://reqres.in/api/login", json=login_payload)
    token = None
    if login_response.status_code == 200:
        token = login_response.json()["token"]
    payload = {"name": "morpheus", "job": "leader"}
    response = requests.post("https://reqres.in/api/users", json=payload, auth=("", token))
    assert response.status_code == 201
    data = response.json()
