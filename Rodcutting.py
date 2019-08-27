import numpy as np

def GetCutting(arr):

    for i in range(1, len(arr)):
        rodCost = int(arr[i][0])

        for j in range(2, len(arr[0])):

            if(i == 1):
                arr[i][j] = (j-1)*rodCost

            elif(i > 1 and i >= j):
                arr[i][j] = arr[i-1][j]

            else:
                arr[i][j] = max(arr[i-1][j], rodCost+arr[i][j-i])



    print(arr)


l = 5

cost = [2, 5, 7, 8]

cutArry = np.zeros((len(cost)+1, l+2))


for i in range(1,len(cost)+1):
    cutArry[i][0] = cost[i-1]

for i in range(1,l+2):
    cutArry[0][i] = i-1

GetCutting(cutArry)
