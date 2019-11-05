d = dict()

d['xyz'] = 1
d['abc'] = 2
d['lmn'] = 3

print("Keys-->",d.keys())
print("Values -->",d.values())


#delete a key-value pair
del d['xyz']

print("Keys-->",d.keys())
print("Values -->",d.values())

# Declaration of dictionary
d1 = {'xyz':1, 'abc':2, 'lmn':3}
print(d1.keys())
print(d1.values())

## Check the key is present or not

print('xyz' in d1)

if(d1.get('xyz')):
    print("yes")

##Copy of the dictinary

b = d1.copy()
print(b)


## Update
print(b.update)

## Get function
print(b.get('xyz'))

## Keys
print(b.keys())

##pop
x = b.pop('xyz')
print(x)
print(b)

##popitem
x = b.popitem()
print(b)






## clear
d1.clear()
print(d1)




