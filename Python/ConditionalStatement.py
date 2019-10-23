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


# #########Question###############
#
shoppingCost = input("How is the total cost? \n")
shoppingCost = int(shoppingCost)

totalcost = 0

if(shoppingCost < 50):
    totalcost = shoppingCost + 10
else:
    totalcost = shoppingCost

print("Total cost is $%d"%totalcost)


############### IF-ELSE-ELIF######################

team = input("Enter your favourite team \n").lower()

if team == 'flyers':
    print('Best team ever')
elif team == 'senators':
    print('Go sens go')
elif team == 'rangers':
    print('Go rangers')
else:
    print("I don\'t have anything clear fav")




####################LOGICAL AND OR###############

team = input("Enter your favourite team \n").lower()
sport = input("Enter your favourite sports \n").lower()

if team == 'rangers' and sport == 'hockey':
    print('I miss captain')
elif(team == 'senator' or team == 'leaf'):
    print("Good luck")
else:
    print("I don't know the team!!!!")


############## PRECEDENCE --> AND first then OR #####################


########## WRONG  EXAMPLE ###############
team = input("Enter your favourite team \n").lower()
sport = input("Enter your favourite sports \n").lower()

if sport == 'hockey' and team == 'senators' or team == 'leafs':
    print("Good luck for the cup")


########## CORRECT  EXAMPLE ###############
team = input("Enter your favourite team \n").lower()
sport = input("Enter your favourite sports \n").lower()

if sport == 'hockey' and (team == 'senators' or team == 'leafs'):
    print("Good luck for the cup")


print(team)
print(sport)

sportsIsHockey = False
if sport == "hockey":
    sportsIsHockey = True

teamIsCorrect = False
if team == 'leafs' or team == 'senators':
    teamIsCorrect = True

print(sportsIsHockey)
print(teamIsCorrect)

if sportsIsHockey and teamIsCorrect:
    print("Good luck for the cup")