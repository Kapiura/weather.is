import requests
from datetime import date

import standalone
standalone.run('PJS.settings')

import django
django.setup()
from horoscope.models import horoscope

#deleting all horoscopes 
try:
    horoscope.objects.all().delete()
    print("Objects have been deleted")  
except:
    print("Something gone wrong while deleting objects from 'horoscope'")

# Get today's date
current = date.today()
# Transofrm it to format = YY-mm-dd
current = current.strftime("%Y-%m-%d")
# List of horoscope signs
horoscope_signs = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Pisces', 'Aquarius']
for sign in horoscope_signs:
    # Creating an horoscope object
    my_model = horoscope()
    url = f"https://horoscope-app-api.vercel.app/api/v1/get-horoscope/daily?sign={sign}&day={current}"
    response = requests.get(url)
    response = response.json()
    my_model.sign = sign
    try:
        horoskopik = response['data']['horoscope_data']
        print(horoskopik)
        my_model.description = horoskopik
    except:
        pass
        my_model.description = 'Something went wrong getting horoscope for today from api :('
        print("Something went wrong getting horoscope for today from api :(")
    my_model.save()