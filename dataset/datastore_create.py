# encoding: utf-8
#!/usr/bin/env python3
import requests
import json
from decouple import config
from time import gmtime, strftime


def datastore_create():
    with open(
            "bitcoin-market-price.json", encoding="utf-8",
    ) as json_f:
        json_file = json.load(json_f)

    BaseURL = config("BaseURL")

    payload = {
        "resource": {
            "package_id": "bitcoin-market-price",
            "name": "Bitcoin Market Price",
            "format": "JSON",
        },
        "primary_key": ", , ,",
        "fields": [
            {"id": "", "type": "text"},
            {"id": "", "type": "text"},
            {"id": "", "type": "text"},
            {"id": "", "type": "text"},
            {"id": "", "type": "text"},
            {"id": "", "type": "text"},
        ],
        "records": json_file,
        "calculate_record_count": True,
    }

    data = json.dumps(payload)

    headers = {
        "Content-Type": "application/json",
        "Authorization": config("AUTHORIZATION"),
    }

    response = requests.post(
        f"{BaseURL}datastore_create",
        data=data,
        headers=headers,
    )

    print(response.text)


if __name__ == "__main__":
    datastore_create()

print("Logged:", strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
