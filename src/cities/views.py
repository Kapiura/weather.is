from django.shortcuts import render
from .models import cities, city
from django.http import Http404
from datetime import datetime

def weather_view(request, *args, **kwargs):
    cities_ = cities.objects.all()
    city_ = city.objects.all()
    ci_date = city.objects.get(city_id=1)
    context = {
        'cities': cities_,
        'city': city_,
        'c_date':ci_date,
    }
    return render(request, "weather.html", context)

def weather_view_detail(request,pk):
    city_ = city.objects.get(city_id=pk)
    city_name = cities.objects.get(id=pk)
    city_name_n = city_name.name.replace(" ","_")
    #path = ''.join('graphs/',city_name.name,'/co.png')
    timezone = city_.timezone
    sunset = city_.sunset
    sunrise = city_.sunrise
    sunrise = datetime.utcfromtimestamp(sunrise).strftime('%H:%M')
    sunset = datetime.utcfromtimestamp(sunset).strftime('%H:%M')
    context = {
        'city': city_,
        'name_space': city_name.name,
        'name' : city_name_n,
        'timezone': timezone,
        'sunrise': sunrise,
        'sunset': sunset,
    }
    if city_ is not None:
        return render(request, 'detail.html', context)
    else:
        raise Http404('Something gone wrong')

# def index(request):
#     cities_ = cities.objects.all()
#     return render(request, 'weather/index.html', {'cities': cities_})
#
# def city(request, city_id):
#     city_ = city.objects.get(id=city_id)
#     return render(request, 'weather/city.html', {'city': city_})