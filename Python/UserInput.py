name = input("What is your name? \n")
country = input("What country do you live in? \n")
country = country.upper()

# message.find --> finds the position of the satrting charecter in the search string

message = "Hello world"
print(message.find("world"))

# message.count --> counts the number of that string or charecters in the original string

message = "Hello worlod"
print(message.count('o'))

# message.capitalize() --> Capitalizes the first letters of every word in the string

message = "hello world"
print(message.capitalize())

# message.upper() --> Capitalizes all the letters of every word in the string
message = "Hello world"
print(message.upper())

# message.replace('Hello', 'Hi') --> Replace the first argument by the second
message = "Hello world"
print(message.replace("Hello", "Hi"))


print(country)
print(name)

