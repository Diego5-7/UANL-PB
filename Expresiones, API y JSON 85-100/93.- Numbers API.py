import requests

url = "https://numbersapi.com/42?json"
response = requests.get(url)
data = response.json()

print("Trivia:", data["text"])
