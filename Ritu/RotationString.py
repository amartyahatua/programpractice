def isRotation(first, second):
    newString=first+first
    if (second in newString):
        return True
    else:
        return False

first = "IndiaUSAEngland"
second = "USAEnglandIndia"
print(isRotation(first, second))

first = "IndiaUSAEngland"
second = "IndiaEnglandUSA"
print(isRotation(first, second))