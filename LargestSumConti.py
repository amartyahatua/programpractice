import numpy as np

def LargestSum(arr):

    arr[1][0] = arr[0][0]
    sumV = arr[1][0]

    for i in range(1,len(arr[0])):
        if((arr[0][i]+arr[1][i-1]) >= arr[0][i]):
            arr[1][i] = arr[0][i] + arr[1][i-1]
        else:
            arr[1][i] = arr[0][i]

    print(arr)


nums = [-2, -3, 4, -1, -2, 1, 5, -3]
arry = np.zeros((2,8))
arry[0,:] = nums

LargestSum(arry)
