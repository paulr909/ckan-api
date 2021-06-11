# encoding: utf-8
#!/usr/bin/env python3
import requests
import time
from datetime import timedelta
from decouple import config
from time import gmtime, strftime


def resource_create():
    BaseURL = config("BaseURL")

    data = {
        "package_id": "bitcoin-market-price",
        "name": "Bitcoin Market Price",
        "owner_org": "company-name",
        "format": "CSV",
    }

    file_path = "dataset/bitcoin-market-price.csv"
    files = [("upload", open(file_path))]

    headers = {"Authorization": config("AUTHORIZATION")}

    start = time.time()

    response = requests.post(
        f"{BaseURL}resource_create",
        data=data,
        headers=headers,
        files=files,
    )

    elapsed = time.time() - start
    print("Upload time:", str(timedelta(seconds=elapsed)))
    print(response.text)


if __name__ == "__main__":
    resource_create()

print("Logged:", strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
