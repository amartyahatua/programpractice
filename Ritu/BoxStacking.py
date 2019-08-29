import  numpy as np
class Box:
    def __init__(self, l, w, h):
        self.l = l
        self.w = w
        self.h = h


def createList(box):
    tempArrng = []
    arrange = []
    if(box.l > box.h):
        tempArrng.append(box.l)
        tempArrng.append(box.h)
        tempArrng.append(box.w)
    elif(box.l < box.h):
        tempArrng.append(box.h)
        tempArrng.append(box.l)
        tempArrng.append(box.w)
    arrange.append(tempArrng)
    tempArrng = []

    if (box.l > box.w):
        tempArrng.append(box.l)
        tempArrng.append(box.w)
        tempArrng.append(box.h)
    elif (box.l < box.w):
        tempArrng.append(box.w)
        tempArrng.append(box.l)
        tempArrng.append(box.h)
    arrange.append(tempArrng)
    tempArrng= []

    if (box.w > box.h):
        tempArrng.append(box.w)
        tempArrng.append(box.h)
        tempArrng.append(box.l)
    elif (box.w < box.h):
        tempArrng.append(box.h)
        tempArrng.append(box.w)
        tempArrng.append(box.l)
    arrange.append(tempArrng)
    #tempArrng=[]

    return arrange

def generateKey(arrangement):
    return (arrangement[0]*arrangement[1])


def maxStackHeight(arr):
    arrangement = []

    lenarr = np.zeros(6)
    posarr = np.zeros(6)

    for i in range(len(arr)):
        temparr = createList(arr[i])
        for j in range(len(temparr)):
            arrangement.append(temparr[j])


    print(arrangement)

    arrangement.sort(key=generateKey, reverse=True)
    print(len(arrangement))

    for i in range(len(arrangement)):
        lenarr[i] = arrangement[i][2]
        posarr[i] = i

    print(lenarr)
    print(posarr)

    tempH = 0
    store = 0
    for i in range(1,len(arrangement)):
        tempH = 0
        for j in range(i):
            if((arrangement[i][0] < arrangement[j][0]) and (arrangement[i][1] < arrangement[j][1])):
                if(tempH < lenarr[i] + lenarr[j]):
                    tempH = lenarr[i] + lenarr[j]
                    posarr[i] = j
        if(tempH > 0):
            lenarr[i] = tempH
    print("Height array")
    print(lenarr)
    print(posarr)

    return  max(lenarr)


arr = [Box(1, 2, 4), Box(3, 2, 5)]

print("Maximux height -->")
print(maxStackHeight(arr))