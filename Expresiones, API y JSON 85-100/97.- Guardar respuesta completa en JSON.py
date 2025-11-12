import requests, json

url = "https://api.github.com"
response = requests.get(url)
data = response.json()

with open("respuesta.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print("Datos guardados en respuesta.json")
