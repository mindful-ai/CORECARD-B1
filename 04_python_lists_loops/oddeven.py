# Program to separate the odd number and even numbers

'''
INPUT: 12 34 45 56 67 78
OUTPUT:
ODD -> 45 67
EVEN -> 12 34 56 78
'''

# input
n = input("Enter the number separated by spaces: ")


# process
L = n.split()
odds = []
evens = []
for n in L:
    if(int(n) % 2 == 0):
        evens.append(n)
    else:
        odds.append(n)

# output

print('-'*50)
print("ODDS   -> ", odds)
print("EVENS  -> ", evens)
