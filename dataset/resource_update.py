# encoding: utf-8
#!/usr/bin/env python3
import requests
import time
from datetime import timedelta
from decouple import config
from time import gmtime, strftime


def resource_update():
    BaseURL = config("BaseURL")

    data = {
        "package_id": "bitcoin-market-price",
        "owner_org": "company-name",
        "id": "ab7ea978-2f03-4ee4-99ef-f9cdf398b849",
    }

    file_path = "bitcoin-market-price.csv"
    files = [("upload", open(file_path))]

    headers = {"Authorization": config("AUTHORIZATION")}

    start = time.time()

    response = requests.post(
        f"{BaseURL}resource_update",
        data=data,
        headers=headers,
        files=files,
    )

    elapsed = time.time() - start
    print("Upload time:", str(timedelta(seconds=elapsed)))
    print(response.text)


if __name__ == "__main__":
    resource_update()

print("Logged:", strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
