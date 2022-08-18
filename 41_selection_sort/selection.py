# Implementation
def selection(iter, asc=True):
    temp = iter
    for startindex in range(0, len(iter)-1):
        for index in range(startindex, len(iter)):
            if(temp[startindex] > temp[index]):
                t = temp[startindex]
                temp[startindex] = temp[index]
                temp[index] = t
        print('Pass ', startindex + 1, ' ---> ', temp)
    return temp

# Test the algorithm
if __name__ == '__main__':

    print(selection([9, 1, 3, 5, 7, 8, 2, 4, 6, 6, 6]))  # 1, 2, 3, 4
    print(selection([4, 1, 3, 2])) # 4, 3, 2, 1