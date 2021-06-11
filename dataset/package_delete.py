# encoding: utf-8
#!/usr/bin/env python3
import requests
import json
from decouple import config
from time import gmtime, strftime

BaseURL = config("BaseURL")

payload = {
    "title": "Bitcoin Market Price",
    "name": "bitcoin-market-price",
    "owner_org": "company-name",
    "id": "5d19cf32-13df-45a7-bdf7-7e3ad3478702",
}

data = json.dumps(payload)

headers = {"Content-Type": "application/json", "Authorization": config("AUTHORIZATION")}

response = requests.post(
    f"{BaseURL}package_delete",
    data=data,
    headers=headers,
)

print("Logged:", strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
print(response.text)
