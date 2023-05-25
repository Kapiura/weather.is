from django.shortcuts import render
import abalin_nameday
import json
import datetime
from cities.models import city
from holidays.models import Shopping_sundays, Holidays
from datetime import date
from horoscope.models import horoscope



def home_view(request, *args, **kwargs):
    today = date.today()
    city_ = city.objects.get(city_id=1)

    myClient = abalin_nameday.namedayRequestor('pl', 'Europe/Warsaw')
    data = json.loads(json.dumps(json.loads(myClient.GetData()), indent=2, sort_keys=True))
    pl_names = data['namedays']['nameday']['pl']

    timezone = int(city_.timezone) // 3600
    timezone = f"UTC {('+' if timezone >= 0 else '')}{timezone}"

    sunday = (today + datetime.timedelta(days=(6 - today.weekday() + 7) % 7)).strftime("%Y-%m-%d")
    try:
        Shopping_sundays.objects.get(date=sunday)
        sunday = True
    except Shopping_sundays.DoesNotExist:
        sunday = False

    horoscope_ = horoscope.objects.all()
    holidays_ = Holidays.objects.all()

    for h in holidays_:
        if h.date == str(today.strftime("%Y-%m-%d")):
            holidayStatus = True
            hdate = h.date
            hdesc = h.descritpion
            break
        else:
            holidayStatus = False
            hdate = str(today.strftime("%Y-%m-%d"))
            hdesc = "No holiday today"
    
    ## Get the current date
    #current_date = datetime.date.today()
    ## Calculate the differences between current date and holiday dates
    #differences = [(holiday - current_date).days for holiday in holiday_dates]
    ## Find the minimum non-negative difference
    #nearest_holiday = min(d for d in differences if d >= 0)
    #print("Days until the nearest holiday:", nearest_holiday)


    context = {
        'today': today.strftime("%d - %A"),
        'imieniny': pl_names,
        'year': today.strftime("%Y"),
        'month': today.strftime("%B"),
        'week': today.strftime("%W"),
        'timezone': timezone,
        'sunday': sunday,
        'horoscope': horoscope_,
        'hdate': hdate,
        'hdesc': hdesc,
        'holidayStatus': holidayStatus,
    }
    return render(request, "home.html", context)

def about_me_view(request, *args, **kwargs):
    context = {
    }
    return render(request, "about_me.html", context)

def contact_view(request, *args, **kwargs):
    context = {

    }
    return render(request, "contact.html", context)