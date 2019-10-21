# No quotes so it is a number

area = 0
width = 4
height = 5


area = width * height/2

# Calculating the area of a triangle
print(area)

# Print area with 2 decimal points
print("area of the triangle %.2f" %area)
print("area of the triangle %.6f" %area)

# Number with leading zeros

print("My favourite number is %06d !" % area)

## The input is a string

salary = input("Please enter your salary \n")
bonus = input("please enter your bonus \n")

paycheckamaout = salary + bonus

print(paycheckamaout)

## To get numeric values we need to convert it to numbers or integers

salary = int(salary)
bonus = int(bonus)
paycheckamaout = salary + bonus
print(paycheckamaout)


## Loan claculator

monthly_payment = 0
loan_amount = 5000
interst = 0.05
number_of_payment = 60

monthly_payment = loan_amount*(interst*(1+interst)*number_of_payment) / ((1+interst)*number_of_payment - 1)

print(monthly_payment)
