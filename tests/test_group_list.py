# encoding: utf-8
#!/usr/bin/env python3
import requests
from decouple import config

BaseURL = config("BaseURL")


def test_group_list_status_code_equals_200():
    response = requests.get(f"{BaseURL}group_list")

    assert response.status_code == 200


def test_group_list_content_type_equals_json():
    response = requests.get(f"{BaseURL}group_list")

    assert response.headers["Content-Type"] == "application/json;charset=utf-8"


def test_group_list_result_equals_test_data():
    response = requests.get(f"{BaseURL}group_list")
    response_body = response.json()

    assert response_body["result"] == [
        "cm-group",
        "cfd-actuals-group",
        "cfd-forecasts-group",
        "levy-group",
    ]


def test_group_list_status_code_equals_400():
    response = requests.get(f"{BaseURL}group_list_bad_request")

    assert response.status_code == 400
