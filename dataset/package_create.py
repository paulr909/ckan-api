# encoding: utf-8
# !/usr/bin/env python3
import requests
import json
from decouple import config
from time import gmtime, strftime


def package_create():
    BaseURL = config("BaseURL")

    payload = {
        "title": "Bitcoin Market Price",
        "name": "bitcoin-market-price",
        "owner_org": "company-name",
        "license_id": "uk-ogl",
        "notes": "This dataset includes Bitcoin Market Price",
        "tags": [
            {"name": ""},
            {"name": ""},
            {"name": ""},
        ],
        "extras": [
            {
                "key": "",
                "value": ""
            },
            {
                "key": "",
                "value": "",
            },
            {
                "key": "",
                "value": "",
            },
        ],
    }

    data = json.dumps(payload)

    headers = {
        "Content-Type": "application/json",
        "Authorization": config("AUTHORIZATION"),
    }

    response = requests.post(
        f"{BaseURL}package_create",
        data=data,
        headers=headers,
    )

    print(response.text)


if __name__ == "__main__":
    package_create()

print("Logged:", strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
