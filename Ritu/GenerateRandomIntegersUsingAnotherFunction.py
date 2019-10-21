import numpy as np

def generateRandomFive():
    number = np.random.randint(low=1, high=5, size=1)
    return  number


def my_random_7():
    i = 5*generateRandomFive() + generateRandomFive() - 5
    if(i<22):
        return ((i%7)+1)
    else:
        my_random_7()

for i in range(10):
    print(my_random_7())
