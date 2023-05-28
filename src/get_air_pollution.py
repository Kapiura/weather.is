import datetime as dt
import requests,os
import matplotlib.pyplot as plt
from internet_connection_checker import internet


import standalone
standalone.run('PJS.settings')

import django
django.setup()
from cities.models import city

os.system('clear')
internet()

current_date = [dt.datetime.now().strftime('%Y'),dt.datetime.now().strftime('%m'),dt.datetime.now().strftime('%d')]
current_date = '-'.join(current_date)
ap_list = ['co','no','no2','o3','so2','pm2_5','pm10','nh3']
air_pol_titles = ['Carbon Monoxide','Nitric Oxide','Nitrogen Dioxide','Ozone','Sulfur Dioxide','Particulate Matter 2.5','Particulate Matter 10','Ammonia']
cities_ = ['Bialystok', 'Bydgoszcz', 'Gdansk', 'Gorzow Wielkopolski', 'Katowice', 'Kielce', 'Krakow', 'Lublin', 'Lodz', 'Olsztyn', 'Opole', 'Poznan', 'Rzeszow', 'Szczecin', 'Torun', 'Warsaw', 'Wroclaw', 'Zielona Gora']
API_KEY = '7b7fe4dd87c83d143654327eaa81fdd8'
air_num = {
    1:'Good',
    2:'Fair',
    3:'Moderate',
    4:'Poor',
    5:'Very Poor',
}

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
    
try:
    city.objects.all().delete()
    print("objects deleted")
    id_ = 1
    for c in cities_:
        air_pol_com = []
        print('adding info about {}'.format(c))
        weather = Weather(c)
        data = weather.get_coord()
        weather.lat = data['coord']['lat']
        weather.lon = data['coord']['lon']
        data = weather.get_info_from_coords()

        my_model = city()
        my_model.city_id = id_
        my_model.description_simple = data['weather'][0]['main']
        my_model.description = data['weather'][0]['description']
        my_model.pic = data['weather'][0]['icon']
        my_model.id_weather = data['weather'][0]['id']
        my_model.wind_speed = data['wind']['speed']
        my_model.clouds = data['clouds']['all']
        my_model.sunset = data['sys']['sunset']
        my_model.sunrise = data['sys']['sunrise']
        my_model.timezone = data['timezone']
        my_model.humidity = data['main']['humidity']
        my_model.temp = weather.get_temp()
        my_model.date = current_date

        air_pol = weather.get_air_pollution_info()
        my_model.air_pol = air_num[air_pol[0]]
        my_model.co = air_pol[1]
        my_model.no = air_pol[2]
        my_model.no2 = air_pol[3]
        my_model.o3 = air_pol[4]
        my_model.so2 = air_pol[5]
        my_model.pm25 = air_pol[6]
        my_model.pm10 = air_pol[7]
        my_model.nh3 = air_pol[8]
        air_pol_com = [my_model.co, my_model.no, my_model.no2, my_model.o3, my_model.so2, my_model.pm25, my_model.pm10, my_model.nh3]
        ap_list = ['co','no','no2','o3','so2','pm2_5','pm10','nh3']
        my_model.save()
        temp_c = c.replace(' ', '_')
        for i in range(len(air_pol_com)):
            temp = ap_list[i].replace('_','')
            with open(f'cities/static/graphs/{temp_c}/{temp}.txt', "a") as f:
                    f.write(f'{current_date} {air_pol_com[i]}\n')
            old_graph_path = f'{ap_list[i]}.png'
            if os.path.exists(old_graph_path):
                os.remove(old_graph_path)
            x = []
            y = []
            with open(f'cities/static/graphs/{temp_c}/{temp}.txt', 'r') as f:
                for line in f:
                    parts = line.split()
                    if len(parts) == 2:
                        x.append(parts[0])
                        y.append(float(parts[1]))
            plt.xticks([])
            plt.plot(x, y)
            plt.xlabel('Time')
            plt.ylabel(f'{air_pol_titles[i]} [μg/m$^3$]')
            plt.title(f'{air_pol_titles[i]} graph')
            plt.savefig(f'cities/static/graphs/{temp_c}/{temp}.png')
            plt.close()
            print(f'Graph of {temp} in {c}')
        print('Graphs have been done creating')
        print(f'Weather info about city {c} has been added\n\n')
        id_ +=1
    print('Info about weather of all these ciries have been added, enjoy :)')
except:
    print("no objects to delete - something went wrong")