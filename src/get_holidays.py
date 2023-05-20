from datetime import date
from workalendar.europe import Poland

import standalone
standalone.run('PJS.settings')

import django
django.setup()
from swieta.models import swieta

#deleting all obejcts from table 'swieta'
try:
    swieta.objects.all().delete()
    print("Objects have been deleted")
    #Get country holidays
    cal = Poland()
    #Get current year
    curretn_year = date.today().year
    #get dictionary of holidays
    holidays = cal.holidays(curretn_year)
    #adding holidays to database
    for holiday in holidays:
        my_model = swieta()               # Creating an object of 'swieta'       
        my_model.descritpion = holiday[1] # Give to description name of holiday
        my_model.date = holiday[0]        # Give to date, date of holiday
        my_model.save()                   # Save an object to database
except:
    print("Sometihing gone wrong while deleting objects")

