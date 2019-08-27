import numpy as np

def SubsetCount(arrCount):

    for i in range(len(arrCount)):
        coin = int(arrCount[i][0])
        for j in range(2,len(arrCount[0])):
            if(coin == j-1):
                arrCount[i][j] = 1
            elif(coin < j and i > 1):
                arrCount[i][j] = max(arrCount[i-1][j], arrCount[i-1][j-coin])
            elif(coin > j-1 and i >= 2):
                arrCount[i][j] = arrCount[i-1][j]


    print(arrCount)


count = 9

array = [2, 3, 4, 5, 12, 34]

arrCount = np.zeros((len(array)+1, count+2))

for i in range(1,len(arrCount)):
    arrCount[i][0] = array[i-1]
    arrCount[i][1] = 1

for i in range(1,len(arrCount[0])):
    arrCount[0][i] = i-1

#print(arrCount)
SubsetCount(arrCount)
