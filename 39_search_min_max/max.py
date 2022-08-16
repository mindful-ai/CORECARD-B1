# Algorithm implementation
def getmax(iter):
    maximum = iter[0]
    for index in range(1, len(iter)):
        if(iter[index] > maximum):
            maximum = iter[index]

    return maximum

# Test case
import random
if __name__ == '__main__':

    L = [random.randint(1, 100) for n in range(20)]
    print(getmax(L))

    L = [random.randint(1, 100) for n in range(20)]
    print(getmax(L))

    L = [random.randint(1, 100) for n in range(20)]
    print(getmax(L))


    L = [34, 56, 67, 33]
    currmax = 67