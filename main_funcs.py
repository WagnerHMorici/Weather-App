# API - https://openweathermap.org/
# https://api.openweathermap.org/data/2.5/weather?q={}&appid={}

import requests

class GetData:

    def __init__(self, key, cidade):
        self.key = key
        self.cidade = cidade
        r = self.requisition()
        self.data = self.return_data(r)

    def requisition(self):

        url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(self.cidade, self.key)
        r = requests.get(url)
        return r

    def return_data(self, r):
        data = r.json()
        temp = data['main']['temp']
        weather = data['weather'][0]['description']
        return f"Temperature: {temp - 273.15:.2f}ºC\nDescription: {weather.title()}."

    def __str__(self):
        return self.data







