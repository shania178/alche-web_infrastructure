#!/usr/bin/python3

import requests

url = "https://api.restful-api.dev/objects"

response = requests.get(url)
data = response.json()

print("Status code:", response.status_code)
print(data)
