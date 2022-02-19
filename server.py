import requests
req = requests.get("http://api.open-notify.org/astros.json")
print (req.status_code)
print (req.json())