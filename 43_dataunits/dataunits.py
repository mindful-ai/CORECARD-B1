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

root = d1


# Algorithm to traverse a linked list
curr = root
while True:
    print(curr.getdata())
    if curr.getlink() == None:
        break
    else:
        curr = curr.getlink()

# Algorithm to search for a value in the linked list
curr = root
searchdata = 30
while True:
    if curr.getdata() == searchdata:
        print(searchdata, ' is found in ', curr)
    if curr.getlink() == None:
        break
    else:
        curr = curr.getlink()