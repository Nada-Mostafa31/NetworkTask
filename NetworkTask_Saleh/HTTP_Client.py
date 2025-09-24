import requests
print(requests.get("http://127.0.0.1:5000/temperature").json())
print(requests.post("http://127.0.0.1:5000/temperature", json={"temperature": 20}).json())