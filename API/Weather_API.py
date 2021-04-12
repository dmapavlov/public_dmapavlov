import requests

city = input("City???: ")
api_url = 'http://api.openweathermap.org/data/2.5/weather'
params = {
    'q': city,
    'appid': 'API key',  # API key must be here from https://openweathermap.org
    'units': 'metric',
    'lang': 'ru'
}

res = requests.get(api_url, params=params)
# print(res.status_code)
# print(res.headers["Content-Type"])
# print(res.json())
data = res.json()
temp = int(data["main"]["temp"])
print(f"Current temperature in {city} is {temp} C\N{DEGREE SIGN}")
