from datetime import date
from workalendar.europe import Poland
import requests

cal = Poland()
curretn_year = date.today().year


holidays = cal.holidays(curretn_year)

for holiday in holidays:
    print(holiday[0], holiday[1])

