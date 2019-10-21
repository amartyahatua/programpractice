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


## Question##
## Ask a user to enter the deadline of a project and tell how many days remaining
## Answer them in weeks and days

todayDate = datetime.datetime.today()
deadLineFromUser = input("Enter the deadline (mm/dd/YYYY)")
deadline = datetime.datetime.strptime(deadLineFromUser,'%m/%d/%Y')

diff = deadline - todayDate

print("The dead line is", diff.days )

days = int(diff.days)

weeks = int(days/7)
daysremaining = days%7

print("Number of weeks",weeks)
print("Number of days", daysremaining)
