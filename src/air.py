import datetime as dt
import requests,os
import matplotlib.pyplot as plt


import standalone
standalone.run('PJS.settings')

import django
django.setup()
from cities.models import city

current_date = [dt.datetime.now().strftime('%Y'),dt.datetime.now().strftime('%m'),dt.datetime.now().strftime('%d')]
current_date = '-'.join(current_date)
ap_list = ['co','no','no2','o3','so2','pm2_5','pm10','nh3']
cities_ = ['Bialystok', 'Bydgoszcz', 'Gdansk', 'Gorzow Wielkopolski', 'Katowice', 'Kielce', 'Krakow', 'Lublin', 'Lodz', 'Olsztyn', 'Opole', 'Poznan', 'Rzeszow', 'Szczecin', 'Torun', 'Warsaw', 'Wroclaw', 'Zielona Gora']
API_KEY = '7b7fe4dd87c83d143654327eaa81fdd8'
Air_pol_com = ['co', 'nh3', 'no', 'no2', 'o3', 'pm10', 'pm25', 'so2']
Air_pol_com_desc = ['Carbon Monoxide', 'Ammonia', 'Nitric Oxide', 'Nitrogen Dioxide', 'Ozone', 'Particulate Matter 10', 'Particulate Matter 2.5', 'Sulfur Dioxide']



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
    
def gowno():
        my_model.co = air_pol[1]
        c_graph_title = c
        c = c.replace(" ","_")
        with open(f'cities/static/graphs/{c}/co.txt', "a") as f:
            f.write('{} {}\n'.format(current_date,air_pol[1]))
        old_graph_path = "co.png"

        # If the old PNG file exists, delete it
        if os.path.exists(old_graph_path):
            os.remove(old_graph_path)

        # Read x and y data from the file
        x = []
        y = []
        with open('cities/static/graphs/{}/co.txt'.format(c), 'r') as f:
            for line in f:
                parts = line.split()
                if len(parts) == 2:
                    x.append(parts[0])
                    y.append(float(parts[1]))
        # Generate a new graph using Matplotlib
        plt.xticks([])
        plt.plot(x, y)
        plt.xlabel('date')
        plt.ylabel('co')
        plt.title('{} co graph'.format(c_graph_title))
        plt.savefig("cities/static/graphs/{}/co.png".format(c))
        plt.close()


def generate_graph(city_name, parameter, title_graph):
    file_path = f'cities/static/graphs/{city_name}/{parameter}.txt'
    graph_path = f'cities/static/graphs/{city_name}/{parameter}.png'
    old_graph_path = f'{parameter}.png'

    if os.path.exists(old_graph_path):
        os.remove(old_graph_path)

    x = []
    y = []
    with open(file_path, 'r') as f:
        for line in f:
            parts = line.split()
            if len(parts) == 2:
                x.append(parts[0])
                y.append(float(parts[1]))

    plt.xticks([])
    plt.plot(x, y)
    plt.xlabel('date')
    plt.ylabel(parameter)
    plt.title(f'{title_graph} graph for {city_name.replace(" ","_")}')
    plt.savefig(graph_path)
    plt.close()


city.objects.all().delete()
print("objects deleted")
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
    #my_model.rain = data['rain']
    #get sunrise and sunset time
    my_model.sunset = data['sys']['sunset']
    my_model.sunrise = data['sys']['sunrise']
    #timezone
    my_model.timezone = data['timezone']
    #humidity
    my_model.humidity = data['main']['humidity']
    #air pollution info
    air_pol = weather.get_air_pollution_info()
    my_model.air_pol = air_pol[0]
    my_model.co = air_pol[1]
    c_graph_title = c.replace(" ","_")
    for i in range(8):
        generate_graph(c, Air_pol_com[i], Air_pol_com)
    #get temp
    my_model.temp = weather.get_temp()
    #get date
    my_model.date = current_date
    #iteration id
    id_ +=1
    #save object
    #my_model.save()
    #add this 
    print('added')
print('enjoy')



        