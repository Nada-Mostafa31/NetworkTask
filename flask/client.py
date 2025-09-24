import requests


print(requests.get("http://127.0.0.1:5000/LocalTemp").json())

print(requests.post("http://127.0.0.1:5000/LocalTemp", json={"temperature": 20}).json())