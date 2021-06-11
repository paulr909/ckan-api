# encoding: utf-8
#!/usr/bin/env python3
import requests
import json
from decouple import config

BaseURL = config("BaseURL")

data = {
    "title": "Test title",
    "name": "test-dataset_api",
    "notes": "Test Package Create",
    "owner_org": "company-name",
    "tags": [{"name": "test"}, {"name": "api"}, {"name": "pytest"}],
    "resources": [
        {
            "package_id": "test-dataset",
            "name": "S3 URL test",
            "url": "https://s3-test-bucket/test.json",
            "description": "Short description",
        }
    ],
}

payload = json.dumps(data)

headers = {"Content-Type": "application/json", "Authorization": config("Authorization")}


def test_package_create_equals_200_json_success():
    response = requests.post(
        f"{BaseURL}package_create",
        data=payload,
        headers=headers,
    )

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json;charset=utf-8"

    response_body = response.json()

    assert response_body["success"] is True


def test_package_create_status_code_equals_400():
    response = requests.post(
        f"{BaseURL}package_create_bad_request",
        data=payload,
        headers=headers,
    )

    assert response.status_code == 400
