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