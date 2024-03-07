'''
#ex1.Write a Python program to subtract five days from current date.
import datetime

x=datetime.datetime.now()-datetime.timedelta(days=5)
print(f"Current date: {datetime.datetime.now()}")
print(f"Data 5 days ago: {x}")

#ex2.Write a Python program to print yesterday, today, tomorrow.
import datetime

today=datetime.datetime.now()
yesterday=datetime.datetime.now()-datetime.timedelta(days=1)
tomorrow=datetime.datetime.now()+datetime.timedelta(days=1)
print(f"Yesterday: {yesterday}")
print(f"Today: {today}")
print(f"Tomorrow: {tomorrow}")

#ex3.Write a Python program to drop microseconds from datetime.
import datetime

today=datetime.datetime.now().strftime("%X")

print(f"Today: {today}")

#ex4.Write a Python program to calculate two date difference in seconds.
import datetime
import random

date1 = datetime.datetime.now()


ran_hour = random.randint(1, 23)
ran_minutes = random.randint(1, 60)
ran_seconds = random.randint(1, 60)

time_difference = datetime.timedelta(hours=ran_hour, minutes=ran_minutes, seconds=ran_seconds)

date2 = date1 - time_difference


difference_seconds = abs((date1 - date2).total_seconds())

print(f"Date 1: {date1}")
print(f"Date 2: {date2}")
print(f"Difference in seconds: {difference_seconds}")
'''
