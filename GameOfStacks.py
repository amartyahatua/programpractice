#!/bin/python3

import os
import sys

#
# Complete the twoStacks function below.
#
def twoStacks(x, a, b):
    #
    # Write your code here.
    #
    count = 0
    sumT = 0
    while(sumT <= x):
        #count += 1
        if(len(a) > 0 and len(b)>0):
             sumT = sumT+a[0]+b[0]
        elif(len(a) > 0 and len(b) == 0):
            sumT = sumT + a[0]
        elif(len(b) > 0 and len(a) == 0):
            sumT = sumT + b[0]

        if(sumT <= x):
            count = count + 2
            a.pop(0)
            b.pop(0)
        elif((sumT - a[0]) <= x):
            count = count+1
            sumT = sumT - a[0]
            if(len(b)>0):
                b.pop(0)
        elif((sumT - b[0]) <= x):
            count = count + 1
            sumT = sumT - b[0]
            if(len(a)>0):
                a.pop(0)

    return count





def largestRectangle(h):
    presentareaF = 0
    presentareaB = 0
    tH = []
    while(len(h) > 0):
        minStack = min(h)
        temparea = minStack*len(h)
        if(temparea > presentareaB):
            presentareaB = temparea
        tH.append(h.pop(0))

    while(len(tH) > 0):
        minStack = min(tH)
        temparea = minStack*len(tH)
        if(temparea > presentareaF):
            presentareaF = temparea
        tH.pop()

    if(presentareaF > presentareaB):
        return presentareaF
    else:
        return presentareaB









# if __name__ == '__main__':
#     # fptr = open(os.environ['OUTPUT_PATH'], 'w')
#     #
#     # g = int(input())
#
#     for g_itr in range(1):
#         # nmx = input().split()
#         #
#         # n = int(nmx[0])
#         #
#         # m = int(nmx[1])
#         #
#         # x = int(nmx[2])
#         #
#         # a = list(map(int, input().rstrip().split()))
#         #
#         # b = list(map(int, input().rstrip().split()))
#         a = [4, 2, 4, 6, 1]
#         b = [2, 1, 8, 5]
#         x = 10
#
#         result = twoStacks(x, a, b)
#         print(result)
#
#         #fptr.write(str(result) + '\n')
#
#     #fptr.close()



a = [4, 2, 4, 6, 1]
b = [2, 1, 8, 5]
x = 10

# result = twoStacks(x, a, b)
# print(result)

h = [8979, 4570, 6436, 5083, 7780, 3269, 5400, 7579, 2324, 2116]
h = [1,2,3,4,5]
print(largestRectangle(h))
