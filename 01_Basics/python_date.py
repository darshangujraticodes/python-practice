
import datetime

# Displaying Date and time

time = datetime.datetime.now()

print('\nPython Date =',time)

print(f'Date = {time.day}/{time.month}/{time.year} ')



# creating date object to declare date and time 

date = datetime.datetime(2024,5,17)

print(date)


# format date into readable string using strftime()

time2 = datetime.datetime.now()

print(f'Python Date Readable Strings = {time2.strftime('%d')}/{time2.strftime('%m')}/{time2.strftime('%Y')} || Day: {time2.strftime('%A')}, Time: {time2.strftime('%X')} |, {time2.strftime('%c')} ')



# for more information refer this w3school doc : https://www.w3schools.com/python/python_datetime.asp







