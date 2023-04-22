from django.shortcuts import render
from .models import cities, city


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

# def index(request):
#     cities_ = cities.objects.all()
#     return render(request, 'weather/index.html', {'cities': cities_})
#
# def city(request, city_id):
#     city_ = city.objects.get(id=city_id)
#     return render(request, 'weather/city.html', {'city': city_})