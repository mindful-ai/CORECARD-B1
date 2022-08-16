# input
uin = input("Enter a sequece of numbers: (10 20 30) : ")
n = [int(x) for x in uin.split()]

searchval = int(input("What do you want to search? "))

# process
found = False
for index in range(0, len(n)):
    if(n[index] == searchval):
        found = True
        break

# output
if(found == True):
    print("The search value was found")
else:
    print("The search value ws not found")