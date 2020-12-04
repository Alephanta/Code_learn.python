#Превратите строку "01/01/25 12:10:03.234567" в объект datetime

from datetime import datetime
dt = '01/01/25 12:10:03.234567'
date_t = datetime.strptime(dt, '%m/%d/%y %H:%M:%S.%f')

print(date_t)