import datetime as dt
import requests,os,sys

import django
django.setup()
from cities.models import city

current_date = [dt.datetime.now().strftime('%Y'),dt.datetime.now().strftime('%m'),dt.datetime.now().strftime('%d')]
current_date = '-'.join(current_date)
ap_list = ['co','no','no2','o3','so2','pm2_5','pm10','nh3']
cities_ = ['Bialystok', 'Bydgoszcz', 'Gdansk', 'Gorzow Wielkopolski', 'Katowice', 'Kielce', 'Krakow', 'Lublin', 'Lodz', 'Olsztyn', 'Opole', 'Poznan', 'Rzeszow', 'Szczecin', 'Torun', 'Warsaw', 'Wroclaw', 'Zielona Gora']
API_KEY = '7b7fe4dd87c83d143654327eaa81fdd8'


class Weather:
    def __init__(self, city):
        self.city = city
    def get_coord(self):
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(self.city, API_KEY)
        response = requests.get(url)
        data = response.json()
        return data
    def get_air_pollution_info(self):
        url = 'http://api.openweathermap.org/data/2.5/air_pollution?lat={}&lon={}&appid={}'.format(self.lat,self.lon,API_KEY)
        response = requests.get(url)
        data = response.json()
        data_list = []
        data_list.append(data['list'][0]['main']['aqi'])
        for x in ap_list:
            data_list.append(data['list'][0]['components'][x])
        return data_list
    def get_temp(self):
        data['main']['temp'] = data['main']['temp'] - 273.15
        data['main']['temp'] = round(data['main']['temp'], 1)
        return data['main']['temp']
    def get_info_from_coords(self):
        url = 'https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}'.format(self.lat, self.lon, API_KEY)
        response = requests.get(url)
        data = response.json()
        return data
    



#deleting all objects
city.objects.all().delete()
print("objects deleted")




#adding
id_ = 1
for c in cities_:
    print('adding info about {}'.format(c))
    #creating an class object Weather
    weather = Weather(c)
    #get coord of city
    data = weather.get_coord()
    weather.lat = data['coord']['lat']
    weather.lon = data['coord']['lon']
    data = weather.get_info_from_coords()
    #create django database object
    my_model = city()
    #django object id
    my_model.city_id = id_
    #get simple and nomrlan info about weather
    my_model.description_simple = data['weather'][0]['main']
    my_model.description = data['weather'][0]['description']
    #get icon
    my_model.pic = data['weather'][0]['icon']
    #get weather id
    my_model.id_weather = data['weather'][0]['id']
    #get wind speed
    my_model.wind_speed = data['wind']['speed']
    #get clouds info
    my_model.clouds = data['clouds']['all']
    #get rain info
    #my_model.rain = data['rain'][0]['1h']
    #get sunrise and sunset time
    my_model.sunset = data['sys']['sunset']
    my_model.sunrise = data['sys']['sunrise']
    #timezone
    my_model.timezone = data['timezone']
    #air pollution info
    air_pol = weather.get_air_pollution_info()
    my_model.air_pol = air_pol[0]
    my_model.co = air_pol[1]
    my_model.no = air_pol[2]
    my_model.no2 = air_pol[3]
    my_model.o3 = air_pol[4]
    my_model.so2 = air_pol[5]
    my_model.pm25 = air_pol[6]
    my_model.pm10 = air_pol[7]
    my_model.nh3 = air_pol[8]
    #get temp
    my_model.temp = weather.get_temp()
    #get date
    my_model.date = current_date
    #iteration id
    id_ +=1
    #save object
    my_model.save()
    print('added')

print('enjoy')

#pressure
#rain naprwaic
#dodac ikonki dnia i nocy 