# Program to determine if a number is prime or not

# input
n = int(input("Enter a number: "))


# process/output

for i in range(2, n):
    if(n % i == 0):
        print("The number is not prime")
        break
else:
    print("The number is prime")


# The for loop/ while loop exits because of two reasons
# it has exhausted the range of values / condition became false -> natural exit
# it encountered a break statement

# if the loop exits naturally, else block will execute once
# if the loop exits because of a break statement, the else block does not execute