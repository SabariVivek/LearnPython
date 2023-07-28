# DataAndTime.py
import datetime

# Declaration 1...
date_with_argument = datetime.datetime(year=1999, month=8, day=21, hour=11, minute=34, second=22)

# Declaration 2...
date = datetime.datetime(1999, 8, 21, 11, 34, 22, 345)

# Printing the data in the date...
print(date)
print(date.year)
print(date.month)
print(date.day)
print(date.minute)
print(date.hour)
print(date.second)
print(date.microsecond)

# Printing the date in custom format...
print(date.strftime("%b %d, %Y"))  # Aug 21, 1999

# Printing current date...
print(datetime.datetime.now())
