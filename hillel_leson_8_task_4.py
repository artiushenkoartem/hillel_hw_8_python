"""Task 4. 30 points познакомиться с модулем datetime и написать программу с помощью lambda для
возвращение текущего года, месяца , дня

например результат должен быть таким
import datetime
now = datetime.datetime.now()
.....ваш код))
print(year(now))
print(month(now))
print(day(now))"""
# import the module to be able to work with it
import datetime
# create a variable that contains the current date and time
now = datetime.datetime.now()
# create variables using a lazy function in which we will substitute the value of the previous variable
year = lambda i: i.year
month = lambda i: i.month
day = lambda i: i.day
# output all the results of our lazy call functions
print(year(now))
print(month(now))
print(day(now))
