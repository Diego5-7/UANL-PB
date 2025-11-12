import requests

n = input("Escribe un número: ")
url = f"https://numbersapi.com/{n}?json"
response = requests.get(url)
data = response.json()

print("Trivia:", data["text"])
