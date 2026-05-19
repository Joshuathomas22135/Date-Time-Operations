# Create a program to display today's date, time, hour, mins, second, and calendar year in 3 columns.

import datetime
import calendar

currentTime = datetime.datetime.now()

print("Time now at greenwich meridian is: ")
print(currentTime)

print("\n", calendar.calendar(2026))