# Algorithm implementation
def search(iter, value):
    found = False
    for index in range(0, len(iter)):
        if(iter[index] == value):
            found = True
            break
    return found


# Test cases
import random
if __name__ == '__main__':

    L = [random.randint(1, 100) for n in range(20)]
    print(search(L, 19))
    print(search(L, 29))
    print(search(L, 39))

    
    print([search(L, x) for x in range(20, 25)])
