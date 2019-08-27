import numpy as np


def CoinChange(arrycoins):

    for i in range(1,len(arrycoins)):
        coin = int(arrycoins[i][0])
        for j in range(1,13):

            if(coin == 1):
                arrycoins[i][j] = arrycoins[i-1][j]

            else:
                if(coin > arrycoins[0][j]):
                    arrycoins[i][j] = arrycoins[i-1][j]
                else:
                    arrycoins[i][j] = min(arrycoins[i-1][j], (1+arrycoins[i][j-coin]))


    print(arrycoins)




coins = [1,5,6,8]
total = 11

arrycoins = np.zeros((len(coins)+1, total+2))

for i in range(total+2):
    arrycoins[0][i] = i-1

for i in range(len(coins)):
    arrycoins[i+1][0] = coins[i]



CoinChange(arrycoins)

    
