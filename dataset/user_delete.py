# encoding: utf-8
#!/usr/bin/env python3
import requests
import json
from decouple import config
from time import gmtime, strftime

BaseURL = config("BaseURL")

payload = {
    "id": "test",
}

data = json.dumps(payload)

headers = {"Content-Type": "application/json", "Authorization": config("AUTHORIZATION")}

response = requests.post(
    f"{BaseURL}user_delete",
    data=data,
    headers=headers,
)

print("Logged:", strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
print(response.text)
