class dataunit(object):

    def __init__(self, data):
        self.data = data
        self.link = None

    def setdata(self, data):
        self.data = data
    
    def getdata(self):
        return self.data

    def setlink(self, link):
        self.link = link

    def getlink(self):
        return self.link

# --------------------------------------------------------------


d1 = dataunit(10)
d2 = dataunit(20)
d3 = dataunit(30)
d4 = dataunit(40)
d5 = dataunit(50)

# Creation of linked list

d1.setlink(d2)
d2.setlink(d3)
d3.setlink(d4)
d4.setlink(d5)

root = d1  # root should always be a global variable, updated regularly, it is the entry point into the data structure

# Algorithm to traverse a linked list
def traverse(start):
    print("--------------------------------------")
    curr = start
    while True:
        print(curr.getdata())
        if curr.getlink() == None:
            break
        else:
            curr = curr.getlink()


# function to insert a dataunit in to the linked list
def listinsert(start, pos, dataunit):  # 0, -1, 1, 2, 3, ... 10 ....
    temp = dataunit
    curr = start
    count = 0
    global root
    if pos == 0:
        temp.setlink(start)
        root = temp
    elif pos == -1:
        while curr.link != None:
            curr = curr.link
        curr.link = temp
    else:
        while count < pos - 1:
            curr = curr.link
            if(curr.link == None):
                break
            count += 1
        temp.setlink(curr.link)
        curr.setlink(temp)
        


# swap two values

def swap(a, b):
    global root
    if(a == 0):
        temp = root
        root = root.getlink()
        temp.setlink(root.getlink())
        root.setlink(temp)
    else:
        # Move to one step before the swap position
        x = root
        c = 0
        while c < a - 1:
            x = x.getlink()
            c += 1

        # create the variables prev and curr
        prev = x
        curr = x.getlink()
        print(curr.getdata(), curr.getlink().getdata())

        temp = curr
        prev.setlink(curr.getlink())
        temp.setlink(temp.getlink().getlink())
        prev.getlink().setlink(temp)
        


def bubble(root):
    pass

        

# reverse the list
from copy import deepcopy
def reverse():
    global root
    prev = deepcopy(root)
    prev.setlink(None)
    curr = deepcopy(root.getlink())
    pointer = deepcopy(root.getlink())
    while True:
        print(prev.getdata(), curr.getdata())
        curr.setlink(prev)
        prev = deepcopy(curr)
        curr = deepcopy(pointer.getlink())
        pointer = pointer.getlink()
        if(pointer.getlink() == None):
            curr.setlink(prev)
            break
    print(curr.getdata())
    root = deepcopy(curr)

    



# update a specific node's data
    

#listinsert(root, 0, dataunit(60))
#listinsert(root, -1, dataunit(70))
#listinsert(root, 2, dataunit(100))
traverse(root)
print("--------------------------------------")
reverse()
traverse(root)

prev = root
print(prev.getdata(), root.getdata())
prev.setdata(90)
print(prev.getdata(), root.getdata())

print('---------------')

prev = deepcopy(root)
print(prev.getdata(), root.getdata())
prev.setdata(1000)
print(prev.getdata(), root.getdata())


