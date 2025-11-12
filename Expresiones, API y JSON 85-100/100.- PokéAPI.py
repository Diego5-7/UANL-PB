import requests

url = "https://pokeapi.co/api/v2/pokemon?limit=5"
response = requests.get(url)
data = response.json()

print("Primeros 5 Pokémon:")
for poke in data["results"]:
    print("-", poke["name"])
