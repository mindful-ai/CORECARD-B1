
# Algorithm implementation
def bubble(iter, asc=True):
    temp = iter
    swap = -1
    while swap != 0:
        i = 0
        j = 1
        swap = 0
        while True:
            if(asc == True):
                if(temp[i] > temp[j]):
                    t = temp[i]
                    temp[i] = temp[j]
                    temp[j] = t
                    swap += 1
            else:
                if(temp[i] < temp[j]):
                    t = temp[i]
                    temp[i] = temp[j]
                    temp[j] = t
                    swap += 1                
            if(j == len(iter) - 1):
                break
            #print(i, j)
            i += 1
            j += 1
    return temp

# Test the algorithm
if __name__ == '__main__':

    print(bubble([4, 1, 3, 2], True))  # 1, 2, 3, 4
    print(bubble([4, 1, 3, 2], False)) # 4, 3, 2, 1