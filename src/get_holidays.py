from datetime import date
from workalendar.europe import Poland
from internet_connection_checker import internet

import standalone
standalone.run('PJS.settings')

import django
django.setup()
from holidays.models import Holidays

internet()

#deleting all obejcts from table 'swieta'
try:
    Holidays.objects.all().delete()
    print("Objects have been deleted")
    #Get country holidays
    cal = Poland()
    #Get current year
    curretn_year = date.today().year
    #get dictionary of holidays
    holidays = cal.holidays(curretn_year)
    #adding holidays to database
    for holiday in holidays:
        my_model = Holidays()               # Creating an object of 'swieta'       
        my_model.descritpion = holiday[1] # Give to description name of holiday
        my_model.date = holiday[0]        # Give to date, date of holiday
        my_model.save()
        print(holiday[0],holiday[1])                   # Save an object to database
except:
    print("Sometihing gone wrong while deleting objects")

