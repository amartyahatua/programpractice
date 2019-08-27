import numpy as np

def FriendPair(n):

    arry = np.zeros(n)

    for i in range(n):
        if(i <= 2):
            arry[i] = i
        else:
            arry[i] = (arry[i-1] + (i-1)*arry[i-2])

    print(arry)

n = 5

FriendPair(n)
