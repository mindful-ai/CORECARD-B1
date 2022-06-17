# Program to subtract two numbers
# Print if the result is positive, negative or zero

# input
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# process

res = a - b

# output

print("--------------------------------------------")
print("DIFFERENCE: ", abs( a- b))
if(res > 0):
    print("The result is positive")
elif(res < 0):
    print("The result is negative")
else:
    print("The result is zero")

    
