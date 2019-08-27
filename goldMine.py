import numpy as np

def goldMine(init_arr):
    print(init_arr[0])
    col = len(init_arr)
    row = len(init_arr[0])
    print(row)
    print(col)

    temp_arr = np.zeros((row,col))
    max_val = 0
    for i in range(col):
        for j in range(row):
            if (i==0):
                temp_arr[j][i] = init_arr[j][i]

            elif(i<col-1):
                if(j==0):
                    temp_arr[j][i] = max(temp_arr[j][i],temp_arr[j][i-1]+ init_arr[j][i],temp_arr[j+1][i-1]+ init_arr[j][i])

                elif(j==row-1):
                    temp_arr[j][i] = max(temp_arr[j][i],temp_arr[j-1][i-1]+ init_arr[j][i],temp_arr[j][i-1]+ init_arr[j][i])
                else:
                    temp_arr[j][i] = max(temp_arr[j][i],temp_arr[j-1][i-1]+ init_arr[j][i],temp_arr[j][i-1]+ init_arr[j][i],temp_arr[j+1][i-1]+ init_arr[j][i])

            elif(i == col-1):
                if(j==0):
                    temp_arr[j][i] = max(temp_arr[j][i],temp_arr[j][i-1]+ init_arr[j][i],temp_arr[j+1][i-1]+ init_arr[j][i])
                elif(j==row-1):
                    temp_arr[j][i] = max(temp_arr[j][i],temp_arr[j-1][i-1]+ init_arr[j][i],temp_arr[j][i-1]+ init_arr[j][i])
                else:
                    temp_arr[j][i] = max(temp_arr[j][i],temp_arr[j-1][i-1]+ init_arr[j][i],temp_arr[j][i-1]+ init_arr[j][i],temp_arr[j+1][i-1]+ init_arr[j][i])

            if(max_val < temp_arr[i][j]):
                max_val = temp_arr[i][j]
                print(max_val)



    #print(max_val)
    #retrun max_val
    max_val = 0
    print(temp_arr)
    #print(max(temp_arr))
    for i in range(row):
        for j in range(col):
            if(max_val < temp_arr[i][j]):
                max_val = temp_arr[i][j]
    print(max_val)


init_arr = [[10,33,13,15],[22,21,4,1],[5,0,2,3],[0,6,14,2]]
goldMine(init_arr)

