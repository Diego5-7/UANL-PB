import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=19.43&longitude=-99.13&current_weather=true"
response = requests.get(url)
data = response.json()

temp = data["current_weather"]["temperature"]
viento = data["current_weather"]["windspeed"]

print("Temperatura actual:", temp, "°C")
print("Velocidad del viento:", viento, "km/h")
