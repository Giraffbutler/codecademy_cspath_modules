#Importing the 'datetime' module
from datetime import datetime

birthday = datetime(1998, 6, 7, 10, 21)
#print(birthday.year)
#print(birthday.weekday())

#Using datetime.now()
#print(datetime.now())

#Using timedelta
#print(datetime(2020, 6, 19, 8, 9) - datetime(2020, 3, 5, 18, 27))

#parsing string to time --> https://docs.python.org/3/library/datetime.html
parsed_date = datetime.strptime('Jan 15, 2018', '%b %d, %Y')
#print(parsed_date.month)
#print(parsed_date.year)
#print(parsed_date.day)

#creating string from time value
date_string = datetime.strftime(datetime.now(), '%b %d, %Y')
print(date_string)

#testing change to remote git repo w/ comment