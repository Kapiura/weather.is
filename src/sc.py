import os,sys, requests
import datetime as dt

API_KEY = '7b7fe4dd87c83d143654327eaa81fdd8'

current_date = [dt.datetime.now().strftime('%Y'),dt.datetime.now().strftime('%m'),dt.datetime.now().strftime('%d')]
current_date = '-'.join(current_date)

cities_ = [ 'Bialystok', 'Bydgoszcz', 'Gdansk', 'Gorzow Wielkopolski', 'Katowice', 'Kielce', 'Cracow', 'Lublin', 'Lodz', 'Olsztyn', 'Opole', 'Poznan', 'Rzeszow', 'Szczecin', 'Torun', 'Warsaw', 'Wroclaw', 'Zielona Gora']



class Weather:
    def __init__(self, city):
        self.city = city
    def get_weather(self):
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(self.city, API_KEY)
        response = requests.get(url)
        data = response.json()
        return data
    def get_air_pollution(self):
        url = 'http://api.openweathermap.org/data/2.5/air_pollution?lat={}&lon={}&appid={}'.format(self.lat, self.lon, API_KEY)
        response = requests.get(url)
        data = response.json()
        return data['list'][0]['main']['aqi']
    def __str__(self):
        return 'City: {}, description: {}'.format(self.city, self.description)
    

for c in cities_:
    weather = Weather(c)
    data = weather.get_weather()
    weather.lat = data['coord']['lat']
    weather.lon = data['coord']['lon']
    weather.description = data['weather'][0]['description']
    print(current_date)
    print('City: {}'.format(c))
    print('Air pollution: {}'.format(weather.get_air_pollution()))
    print('---------------------')