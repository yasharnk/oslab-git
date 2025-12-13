import requests

response = requests.get("http://backend:5000/api")
print(response.text)
