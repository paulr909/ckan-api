# encoding: utf-8
# !/usr/bin/env python3
import requests
import json
from decouple import config
from time import gmtime, strftime


def datastore_upsert():
    try:
        with open(
                "dataset/bitcoin-market-price.json", encoding="utf-8",
        ) as json_f:
            json_file = json.load(json_f)

        BaseURL = config("BaseURL")

        payload = {
            "method": "upsert",
            "resource_id": "249f32e0-504c-425f-aa78-73006004baf7",
            "force": True,
            "records": json_file,
        }

        data = json.dumps(payload)

        headers = {
            "Content-Type": "application/json",
            "Authorization": config("AUTHORIZATION"),
        }

        response = requests.post(
            f"{BaseURL}datastore_upsert",
            data=data,
            headers=headers,
        )

        print(
            f"Status code: {response.status_code}\nResponse headers: {response.headers}\nElapsed time: {response.elapsed}"
        )
    except ConnectionError as e:
        print(e)


if __name__ == "__main__":
    datastore_upsert()

print("Logged:", strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
