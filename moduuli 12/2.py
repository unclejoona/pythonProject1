import requests

paikkakunta = input("Anna kaupunki:")
api = ""

pyynto = f"https://api.openweathermap.org/data/2.5/weather?q={paikkakunta}&appid={api}&units=metric"
haku = requests.get(pyynto).json()
saa = haku["weather"][0]["main"]
temp = haku["main"]["temp"]
print(saa)
print(temp)