# How many days do I have util my birthday?
# When is my poject due?
# I want to book an appointment in two weeks, what will the date be?
import  datetime
currentdate = datetime.date.today()
print(currentdate)

print(currentdate.day)
print(currentdate.month)
print(currentdate.year)

# Year with four digits
print(currentdate.strftime('%d %b,%Y'))

# Year with two digits
print(currentdate.strftime('%d %b,%y'))

print(currentdate.strftime('Please attend our event %A %B %d in the year %Y'))


userInput = input('Please enter your birthday (mm/dd/yyyy)')
birthday = datetime.datetime.strptime(userInput,'%m/%d/%Y')
print(birthday)

currentdate = datetime.datetime.today()
difference =  currentdate - birthday
print(difference.days)

currentdate = datetime.datetime.now()
print(currentdate.minute)