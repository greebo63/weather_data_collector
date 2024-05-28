import datetime
import requests
from city import city

kazan_lat = 55.8304307
kazan_lon = 49.0660806
moscow_lat = 55.755826
moscow_lon = 37.486382
nb_lon = 54.167847
nb_lat = 56.126209
weather_variables = 'temperature_2m,wind_speed_10m,precipitation_probability'

kazan = city('Kazan', latitude=kazan_lat, longitude=kazan_lon)
kazan.weather_get(weather_variables)

moscow = city('Moscow', latitude=moscow_lat, longitude=moscow_lon)
moscow.weather_get(weather_variables)

nb = city('Nikolo-Beryozovka', latitude=nb_lat,longitude=nb_lon)
nb.weather_get(weather_variables)