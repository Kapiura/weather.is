import requests
from datetime import date
from internet_connection_checker import internet

import standalone
standalone.run('PJS.settings')

import django
django.setup()
from horoscope.models import horoscope

internet()

#deleting all horoscopes to make space for new 
try:
    horoscope.objects.all().delete()
    print("Objects have been deleted")  
except:
    print("Something gone wrong while deleting objects from 'horoscope'")

current = date.today().strftime("%Y-%m-%d")
horoscope_signs = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Pisces', 'Aquarius']
for sign in horoscope_signs:
    my_model = horoscope()
    url = f"https://horoscope-app-api.vercel.app/api/v1/get-horoscope/daily?sign={sign}&day={current}"
    response = requests.get(url).json()
    my_model.sign = sign
    try:
        my_model.description = response['data']['horoscope_data']
        print(f'Horoscope for {sign}: {my_model.description}')
    except:
        pass
        my_model.description = 'Something went wrong getting horoscope for today from api :('
        print("Something went wrong getting horoscope for today from api :(")
    my_model.save()