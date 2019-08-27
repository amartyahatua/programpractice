import numpy as np

def MinEditDist(arr, firstString, secondString):

    for i in range(1,len(secondString)+1):
        for j in range(1,len(firstString)+1):

            if(secondString[i-1] == firstString[j-1]):
                arr[i][j] = arr[i-1][j-1]
            else:
                arr[i][j] = min(arr[i][j-1], arr[i-1][j-1], arr[i-1][j]) + 1

    print(arr)

firstString = "abcdef"
secondString = "azced"

arr = np.zeros((len(secondString)+1, len(firstString)+1))

for i in range(len(firstString)+1):
    arr[0][i] = i

for i in range(len(secondString)+1):
    arr[i][0] = i

MinEditDist(arr, firstString, secondString)
