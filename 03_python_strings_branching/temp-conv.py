'''
Enter temperature: 100C
OUTPUT: 212.0F
Enter temperature: 212F
OUTPUT: 100C
'''

# input
t = input("Enter the temperature to convert: ")

# process
n = t[:-1]
cf = t[-1]

if(cf == 'C' or cf == 'c'):
    o = str(float(n) * 1.8 + 32) + 'F'
elif(cf == 'F' or cf == 'f'):
    o = str((float(n) - 32) / 1.8) + 'C'
else:
    o = 'Invalid input'

# output

print("---------------------------------------------")
print(o)
    
