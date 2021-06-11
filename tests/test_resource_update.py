# encoding: utf-8
#!/usr/bin/env python3
import requests
from decouple import config

BaseURL = config("BaseURL")

data = {
    "package_id": "test-dataset",
    "name": "Test test-data",
    "description": "An updated resource tested!",
    "owner_org": "company-name",
    "id": "021966d4-e007-476b-9b16-82ad67e08d67",
}

data_file = "/data/test-data.csv"
files = [("upload", open(data_file))]

headers = {"Authorization": config("Authorization")}


def test_resource_update_equals_200_json_success():
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


def test_resource_update_status_code_equals_400():
    response = requests.post(
        f"{BaseURL}resource_update_bad_request",
        data=data,
        headers=headers,
        files=files,
    )

    assert response.status_code == 400
