import requests

url = "https://pokeapi.co/api/v2/pokemon/25"
response = requests.get(url)
data = response.json()

nombre = data["name"]
tipos = [t["type"]["name"] for t in data["types"]]

print("Nombre:", nombre)
print("Tipos:", ", ".join(tipos))
