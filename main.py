import requests

lat = 61.097301
lon = 7.484130

LAT_MY = 47.533340
LNG_MY = 21.625210
API_KEY = "7935e9ac6e636d5108f59309a7a91a51"
ONE_CALL_API = "https://api.openweathermap.org/data/2.5/onecall"
parameters = {
    "lat": lat,
    "lon": lon,
    "exclude": "current,minutely,daily,alerts",
    "appid": API_KEY,
    "units": "metric"
}

weather_response = requests.get(url=ONE_CALL_API, params=parameters)
weather_response.raise_for_status()
data = weather_response.json()

is_rain = False
for hour in range(12):
    id_code = data["hourly"][hour]["weather"][0]["id"]
    if id_code < 700:
        is_rain = True
if is_rain:
    print("Bring your umbrella.")
