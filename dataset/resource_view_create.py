# encoding: utf-8
#!/usr/bin/env python3
import requests
import time
from datetime import timedelta
from decouple import config
from time import gmtime, strftime


def resource_view_create():
    BaseURL = config("BaseURL")

    data = {
        "resource_id": "249f32e0-504c-425f-aa78-73006004baf7",
        "title": "Grid",
        "view_type": "recline_grid_view",
    }

    headers = {"Authorization": config("AUTHORIZATION")}

    start = time.time()

    response = requests.post(
        f"{BaseURL}resource_view_create",
        data=data,
        headers=headers,
    )

    elapsed = time.time() - start
    print("Upload time:", str(timedelta(seconds=elapsed)))
    print(response.text)


if __name__ == "__main__":
    resource_view_create()

print("Logged:", strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
