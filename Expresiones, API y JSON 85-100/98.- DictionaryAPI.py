import requests

url = "https://api.dictionaryapi.dev/api/v2/entries/en/example"
response = requests.get(url)
data = response.json()

palabra = data[0]["word"]
definicion = data[0]["meanings"][0]["definitions"][0]["definition"]

print("Palabra:", palabra)
print("Definición:", definicion)
