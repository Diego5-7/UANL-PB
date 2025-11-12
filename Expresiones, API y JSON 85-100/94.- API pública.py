import requests

response = requests.get("https://api.github.com")
print("Código de estado:", response.status_code)

if response.status_code == 200:
    print("Todo bien")
else:
    print("No esta bien :(")
