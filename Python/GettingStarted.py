#Source https://www.youtube.com/watch?v=3cZsjOclmoM
#This is a comment
#And I can add lots if comments

print("Hello world")


## We can use single or double quotes
print('The capybera is the world largest rodent')
print("The capybera likes live in groups")
print("The capybera can swim")


## The problem may occur when there is a single quote inside the sentence like "It's a beautiful day". In this case, if we use
## sigle quote then the program may understand the single quote is ending after "It". In such cases we need to use double quotes.
## On the other hand if there is a double quotes inside my string, we can use a single string to quote the entire string

print("It's a beautiful day")
print('He said "have a look"')

## use \n forcefully introducing a new line
## \t for a tab

print("Hellow how are you? \nIt is raining today.")


## Triple quotes
## It allows you to get the output the way you have written in the print statement. It also allows the new lines.
print("""Hello 
how are you? 
I am in Mississippi""")
print("In python we can print \ in a line")

## I am inserting a  \\ so the \ appears correctly

print("But what if I want \news")
print("But what if I want \\news")

## Write a program that will display the following poem
# There once was a movie star icon
# who performed to sleep with the light on
# They learned how to code
# a device that sure glowed
# and lit up the night using Python!

#Sol 1:
print("===========SOLUTION 1=================")
print("There once was a movie star icon")
print("who performed to sleep with the light on")
print("They learned how to code")
print("a device that sure glowed")
print("and lit up the night using Python!")


#Sol 2:
print("===========SOLUTION 2=================")
print("There once was a movie star icon \nwho performed to sleep with the light on \nThey learned how to code \na device that sure glowed \nand lit up the night using Python!")


#Sol 3:
print("===========SOLUTION 3=================")
print("""There once was a movie star icon
who performed to sleep with the light on
They learned how to code
a device that sure glowed
and lit up the night using Python!""")