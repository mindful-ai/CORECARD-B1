# Ref -> 01_getindex.py

def getindeces(item, collection):
    if(type(collection) == list or type(collection) == tuple):
        indeces = []
        for i in range(len(collection)):
            if(collection[i] == item):
                indeces.append(i)
        return tuple(indeces)
    else:
        return False
     

def getfactors(n):
    pass

def getspan(mainstr, substr):
    temp = mainstr
    pointer = 0
    span = []
    while substr in temp:
        start = temp.find(substr) + pointer
        end = start + len(substr)
        span.append((start, end))
        temp = mainstr[start + 1 : ]
        pointer = start + 1
    return tuple(span)