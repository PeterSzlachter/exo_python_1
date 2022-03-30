import requests

# req = requests.get("https://api.kanye.rest/")

for i in range(10):
    req = requests.get("https://api.kanye.rest/")
    print(req.json().get('quote'))