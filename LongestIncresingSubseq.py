import numpy as np

numArry = [10, 22, 9, 33, 21, 50, 41, 60, 80, 1, 120]

countArry = np.zeros(len(numArry))
countArry[0] = 1
count = 1

for i in range(len(numArry)):
    for j in range(i+1):
        if(numArry[i] > numArry[j]):
            tempCount = countArry[j] + 1
            if(tempCount > count):
                count = tempCount
        countArry[i] = count
    count = 1

print(countArry)



