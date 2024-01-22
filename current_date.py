# import the datetime method
import datetime

# import the current date
now=datetime.datetime.now()
# print the current date
print("the current date is\n",now)
months=now.month
years=now.year
hours=now.hour
min=now.minute
print("the month is: ", months)
print("the year is: ",years)
print("the minutes are: ",min)
print("the hour is: ",hours)