import requests

response = requests.get("https://api.github.com")
print("Status:", response.status_code)
print("Content-Type:", response.headers["Content-Type"])
