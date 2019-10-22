## Source https://www.youtube.com/watch?v=eHxoh9Rrtdk

## If with strings

answer = input("Would you like express shipping \n")

## Converting all the answers in lower case so that we can accept any input
answer = answer.lower()
if (answer == "yes"):
    print("That will be an extra $10")

print("Have a nice day")

favouriTeam = input("What is your favourite team \n ")
favouriTeam = favouriTeam.lower()

if(favouriTeam == "senators"):
    print("Yeah go Sens go!!")
    print("But we miss our captain")

print("Its ok if you prefer Football/Soccer")


## If with numbers

deposite = input("How much do you want to deposite? \n")
deposite = int(deposite)

if (deposite > 100):
    print("Enjoy your free toaster!!!")

print("Have a nice day")



if(deposite > 100):
    print("Enjoy your free toaster")
else:
    print("Enjoy your free mug!!")

print("Enjoy your day!!!!")



## Boolean variables
freeToaster = False
if(deposite > 100):
    freeToaster = True

if(freeToaster):
    print("Enjoy free toaster")