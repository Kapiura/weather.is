from django.shortcuts import render
import abalin_nameday
import json
import datetime
from cities.models import city
from holidays.models import Shopping_sundays
from datetime import date
from swieta.models import swieta
from horoscope.models import horoscope



def home_view(request, *args, **kwargs):
    myClient = abalin_nameday.namedayRequestor('pl', 'Europe/Warsaw')
    data = json.dumps(json.loads(myClient.GetData()), indent=2, sort_keys=True)
    data = json.loads(data)
    pl_names = data['namedays']['nameday']['pl']
    today = date.today()
    today = today.strftime("%Y-%m-%d")
    #get str like monday, tuesday etc
    day_name = date.today().strftime("%A")
    year = date.today().strftime("%Y")
    #monht but name like may
    month = date.today().strftime("%B")
    week = date.today().strftime("%W")
    city_ = city.objects.get(city_id=1)
    timezone = int(city_.timezone) // 3600
    timezone = f"UTC {('+' if timezone >= 0 else '')}{timezone}"

    today = date.today()
    sunday = today + datetime.timedelta(days=(6 - today.weekday() + 7) % 7)
    sunday = sunday.strftime("%Y-%m-%d")
    try:
        Shopping_sundays.objects.get(date=sunday)
        sunday = True
    except Shopping_sundays.DoesNotExist:
        sunday = False

    horoscope_ = horoscope.objects.all()

    holi = swieta.objects.all()
   
    now  = datetime.datetime.now()
    now = str(now.strftime("%Y-%m-%d"))

    for h in holi:
        if h.date == now:
            status_sw = True
            hdate = h.date
            hdesc = h.descritpion
            break
        else:
            status_sw = False
            hdate = now
            hdesc = "No holiday today"
    
    # Get the current date
    current_date = datetime.date.today()

    # Calculate the differences between current date and holiday dates
    differences = [(holiday - current_date).days for holiday in holiday_dates]

    # Find the minimum non-negative difference
    nearest_holiday = min(d for d in differences if d >= 0)

    print("Days until the nearest holiday:", nearest_holiday)


    context = {
        'today': day_name,
        'imieniny': pl_names,
        'year': year,
        'month': month,
        'week': week,
        'timezone': timezone,
        'sunday': sunday,
        'horoscope': horoscope_,
        'hdate': hdate,
        'hdesc': hdesc,
        'status_sw': status_sw,
    }
    return render(request, "home.html", context)

def weather_view(request, *args, **kwargs):
    context = {

    }
    return render(request, "weather.html", context)

def about_me_view(request, *args, **kwargs):
    img = ''
    context = {

    }
    return render(request, "about_me.html", context)

def contact_view(request, *args, **kwargs):
    context = {

    }
    return render(request, "contact.html", context)

def graphs_view(request, *args, **kwargs):
    context = {

    }
    return render(request, "graphs.html", context)
