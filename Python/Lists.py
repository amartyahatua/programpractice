guests = ['chris', 'susan', 'bill', 'satya']

# adding a value at the end
guests.append("steve")
print(guests)

# display the last value of the list
print(guests[-1])

# remove a member. If there are multiple 'chris' the first one will be removed
guests.remove('chris')
print(guests)

# find the index
print(guests.index('steve'))