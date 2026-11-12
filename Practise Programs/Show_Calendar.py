# To show calendar.

import calendar

year = int(input('The year:'))
month = int(input('The month:'))

cal = calendar.month(year,month)

print(cal)
