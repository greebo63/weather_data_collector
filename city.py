import json
import requests
import datetime
import os
import pandas


class city:
    name: str
    longitude: float
    latitude: float

    def __init__(self, name, longitude, latitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        if not os.path.exists(f'{str(os.path.abspath(__file__))[:-8]}/{self.name}'):
            os.makedirs(f'{self.name}')

    def see_info(self):
        print(f'Name of city = {self.name}\nLatitude = {self.latitude}\nLongitude = {self.longitude}\n')

    def weather_get(self, weather_variables):
        URL = f'https://api.open-meteo.com/v1/forecast?latitude={self.latitude}&longitude={self.longitude}&current={weather_variables}'
        r = requests.get(url=URL)
        result = r.json()
        with open(
                f'{str(os.path.abspath(__file__))[:-8]}/{self.name}/{str(datetime.datetime.now(datetime.UTC)).replace(':', '_')[:-13]}',
                'w') as file:
            json.dump(result, file, indent=4, sort_keys=True)

    def weather_get_csv(self, weather_variables):
        URL = f'https://api.open-meteo.com/v1/forecast?latitude={self.latitude}&longitude={self.longitude}&current={weather_variables}'
        r = requests.get(url=URL)
        result = r.json()
        df = pandas.DataFrame([{'time': f'{result.get('current').get('time')}',
                                'temperature_2m': f'{result.get('current').get('temperature_2m')}',
                                'wind_speed_10m': f'{result.get('current').get('wind_speed_10m')}',
                                'precipitation_probability': f'{result.get('current').get('precipitation_probability')}'}])
        print(df)
        df.to_csv(f'{str(os.path.abspath(__file__))[:-8]}/{self.name}/{str(datetime.datetime.now())[:-13]}.csv',
                  index=False)
