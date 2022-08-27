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

print(d1.getdata())
print(d2.getdata())

print(d1)
print(d2)


# Creation of linked list

d1.setlink(d2)
d2.setlink(d3)
d3.setlink(d4)
d4.setlink(d5)

root = d1  # root should always be a global variable, updated regularly, it is the entry point into the data structure


# Algorithm to traverse a linked list
def traverse(start):
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
        
# deleting a node from the linked list

# swap two values

# update a specific node's data
    

listinsert(root, 0, dataunit(60))
listinsert(root, -1, dataunit(70))
listinsert(root, 2, dataunit(100))
traverse(root)



