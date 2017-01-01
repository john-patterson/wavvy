import requests


class OpenWeather:
    base_url = 'http://api.openweathermap.org/data/2.5/'

    def __init__(self, key):
        self.key = key

    def kelvin_by_zip(self, zipcode):
        payload = {
            'zip': zipcode,
            'APPID': self.key
        }
        return requests.get(self.base_url + '/weather', params=payload).json()['main']['temp']
