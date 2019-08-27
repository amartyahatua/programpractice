import numpy as np

def Tiling(n):
    arry = np.zeros((n))

    for i in range(n):
        if( i == 0 or i == 1):
            arry[i] = i
        else:
            arry[i] = arry[i-1] + arry[i-2]


    print(arry)


n = 8

Tiling(n)
