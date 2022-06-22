# Write a program to extract all the primes
# between a user given range


import project_1a
print('Project 3 __name__ = ', __name__)

# input
s = int(input("Enter the starting range: "))
e = int(input("Enter the ending range: "))

# process
p = project_1a.getprimes(s, e)

# output
print(p)

# Importance of __name__
'''
>python project_1a.py
Project 1A __name__ =  __main__
[Project 1a]Enter a number: 12
The number is not prime

>python project_3.py  
Project 1A __name__ =  project_1a
Project 3 __name__ =  __main__
Enter the starting range: 11
Enter the ending range: 33
(11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33)


'''
