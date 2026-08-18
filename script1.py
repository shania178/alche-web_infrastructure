#!/usr/bin/python3

"""
Find any free public API that interests you. Get one endpoint working in
Postman, then write a Python script that prints three useful fields from it. Bring
both next week."""

import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)
data = response.json()

print("id:", data["id"])
print("title:", data["title"])
print("body:", data["body"])
