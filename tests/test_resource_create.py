# encoding: utf-8
#!/usr/bin/env python3
import requests
from decouple import config

BaseURL = config("BaseURL")

data = {
    "package_id": "test-dataset",
    "name": "Test Package",
    "description": "A short description of my resource!",
    "owner_org": "company-name",
}

data_file = "/data/test-data.csv"
files = [("upload", open(data_file))]

headers = {"Authorization": config("Authorization")}


def test_resource_create_equals_200_json_success():
    response = requests.post(
        f"{BaseURL}resource_create",
        data=data,
        headers=headers,
        files=files,
    )

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json;charset=utf-8"

    response_body = response.json()

    assert response_body["success"] is True


def test_resource_create_status_code_equals_400():
    response = requests.post(
        f"{BaseURL}resource_create_bad_request",
        data=data,
        headers=headers,
        files=files,
    )

    assert response.status_code == 400
