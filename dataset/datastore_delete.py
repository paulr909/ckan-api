# encoding: utf-8
#!/usr/bin/env python3
import requests
import json
from decouple import config
from time import gmtime, strftime


def datastore_delete():
    BaseURL = config("BaseURL")

    payload = {
        "resource_id": "2d1636d9-8e15-478d-9b54-ffe4eb0ce1bd",
        "force": True,
    }

    data = json.dumps(payload)

    headers = {
        "Content-Type": "application/json",
        "Authorization": config("AUTHORIZATION"),
    }

    response = requests.post(
        f"{BaseURL}datastore_delete",
        data=data,
        headers=headers,
    )

    print(response.text)


if __name__ == "__main__":
    datastore_delete()

print("Logged:", strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
