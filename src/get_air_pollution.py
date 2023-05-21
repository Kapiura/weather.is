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
        c_graph_title = c
        c = c.replace(" ","_")
        with open('cities/static/graphs/{}/co.txt'.format(c), "a") as f:
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

        my_model.no = air_pol[2]
        with open('cities/static/graphs/{}/no.txt'.format(c), "a") as f:
            f.write('{} {}\n'.format(current_date,air_pol[2]))
        old_graph_path = "no.png"

        # If the old PNG file exists, delete it
        if os.path.exists(old_graph_path):
            os.remove(old_graph_path)

        # Read x and y data from the file
        x = []
        y = []
        with open('cities/static/graphs/{}/no.txt'.format(c), 'r') as f:
            for line in f:
                parts = line.split()
                if len(parts) == 2:
                    x.append(parts[0])
                    y.append(float(parts[1]))
        # Generate a new graph using Matplotlib
        plt.xticks([])
        plt.plot(x, y)
        plt.xlabel('date')
        plt.ylabel('no')
        plt.title('{} no graph'.format(c_graph_title))
        plt.savefig("cities/static/graphs/{}/no.png".format(c))
        plt.close()

        my_model.no2 = air_pol[3]
        with open('cities/static/graphs/{}/no2.txt'.format(c), "a") as f:
            f.write('{} {}\n'.format(current_date,air_pol[3]))
        old_graph_path = "no2.png"

        # If the old PNG file exists, delete it
        if os.path.exists(old_graph_path):
            os.remove(old_graph_path)

        # Read x and y data from the file
        x = []
        y = []
        with open('cities/static/graphs/{}/no2.txt'.format(c), 'r') as f:
            for line in f:
                parts = line.split()
                if len(parts) == 2:
                    x.append(parts[0])
                    y.append(float(parts[1]))
        # Generate a new graph using Matplotlib
        plt.xticks([])
        plt.plot(x, y)
        plt.xlabel('date')
        plt.ylabel('no2')
        plt.title('{} no2 graph'.format(c_graph_title))
        plt.savefig("cities/static/graphs/{}/no2.png".format(c))
        plt.close()
        my_model.o3 = air_pol[4]
        with open('cities/static/graphs/{}/o3.txt'.format(c), "a") as f:
            f.write('{} {}\n'.format(current_date,air_pol[4]))
        old_graph_path = "o3.png"

        # If the old PNG file exists, delete it
        if os.path.exists(old_graph_path):
            os.remove(old_graph_path)

        # Read x and y data from the file
        x = []
        y = []
        with open('cities/static/graphs/{}/o3.txt'.format(c), 'r') as f:
            for line in f:
                parts = line.split()
                if len(parts) == 2:
                    x.append(parts[0])
                    y.append(float(parts[1]))
        # Generate a new graph using Matplotlib
        plt.xticks([])
        plt.plot(x, y)
        plt.xlabel('date')
        plt.ylabel('o3')
        plt.title('{} o3 graph'.format(c_graph_title))
        plt.savefig("cities/static/graphs/{}/o3.png".format(c))
        plt.close()
        my_model.so2 = air_pol[5]
        with open('cities/static/graphs/{}/so2.txt'.format(c), "a") as f:
            f.write('{} {}\n'.format(current_date,air_pol[5]))
        old_graph_path = "so2.png"

        # If the old PNG file exists, delete it
        if os.path.exists(old_graph_path):
            os.remove(old_graph_path)

        # Read x and y data from the file
        x = []
        y = []
        with open('cities/static/graphs/{}/so2.txt'.format(c), 'r') as f:
            for line in f:
                parts = line.split()
                if len(parts) == 2:
                    x.append(parts[0])
                    y.append(float(parts[1]))
        # Generate a new graph using Matplotlib
        plt.xticks([])
        plt.plot(x, y)
        plt.xlabel('date')
        plt.ylabel('so2')
        plt.title('{} so2 graph'.format(c_graph_title))
        plt.savefig("cities/static/graphs/{}/so2.png".format(c))
        plt.close()
        my_model.pm25 = air_pol[6]
        with open('cities/static/graphs/{}/pm25.txt'.format(c), "a") as f:
            f.write('{} {}\n'.format(current_date,air_pol[6]))
        old_graph_path = "pm25.png"

        # If the old PNG file exists, delete it
        if os.path.exists(old_graph_path):
            os.remove(old_graph_path)

        # Read x and y data from the file
        x = []
        y = []
        with open('cities/static/graphs/{}/pm25.txt'.format(c), 'r') as f:
            for line in f:
                parts = line.split()
                if len(parts) == 2:
                    x.append(parts[0])
                    y.append(float(parts[1]))
        # Generate a new graph using Matplotlib
        plt.xticks([])
        plt.plot(x, y)
        plt.xlabel('date')
        plt.ylabel('pm25')
        plt.title('{} pm2_5 graph'.format(c_graph_title))
        plt.savefig("cities/static/graphs/{}/pm25.png".format(c))
        plt.close()
        my_model.pm10 = air_pol[7]
        with open('cities/static/graphs/{}/pm10.txt'.format(c), "a") as f:
            f.write('{} {}\n'.format(current_date,air_pol[7]))
        old_graph_path = "pm10.png"

        # If the old PNG file exists, delete it
        if os.path.exists(old_graph_path):
            os.remove(old_graph_path)

        # Read x and y data from the file
        x = []
        y = []
        with open('cities/static/graphs/{}/pm10.txt'.format(c), 'r') as f:
            for line in f:
                parts = line.split()
                if len(parts) == 2:
                    x.append(parts[0])
                    y.append(float(parts[1]))
        # Generate a new graph using Matplotlib
        plt.xticks([])
        plt.plot(x, y)
        plt.xlabel('date')
        plt.ylabel('pm10')
        plt.title('{} pm10 graph'.format(c_graph_title))
        plt.savefig("cities/static/graphs/{}/pm10.png".format(c))
        plt.close()
        my_model.nh3 = air_pol[8]
        with open('cities/static/graphs/{}/nh3.txt'.format(c), "a") as f:
            f.write('{} {}\n'.format(current_date,air_pol[8]))
        old_graph_path = "nh3.png"

        # If the old PNG file exists, delete it
        if os.path.exists(old_graph_path):
            os.remove(old_graph_path)

        # Read x and y data from the file
        x = []
        y = []
        with open('cities/static/graphs/{}/nh3.txt'.format(c), 'r') as f:
            for line in f:
                parts = line.split()
                if len(parts) == 2:
                    x.append(parts[0])
                    y.append(float(parts[1]))
        # Generate a new graph using Matplotlib
        plt.xticks([])
        plt.plot(x, y)
        plt.xlabel('date')
        plt.ylabel('nh3')
        plt.title('{} nh3 graph'.format(c))
        plt.savefig("cities/static/graphs/{}/nh3.png".format(c))
        plt.close()
        #get temp
        my_model.temp = weather.get_temp()
        #get date
        my_model.date = current_date
        #iteration id
        id_ +=1
        #save object
        my_model.save()
        #add this 
        print('added')

    print('enjoy')
  
except:
    print("no objects to delete - something went wrong")