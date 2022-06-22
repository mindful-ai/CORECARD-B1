# Accept a series of numbers from the user
# filter all the prime numbers


import project_1a

# input

n = input("[Project 2a]Enter the numbers: ")
n = n.split()
n = list(map(lambda s : int(s), n))
print(n)

# process

primes = []
for num in n:
    if(project_1a.checkprime(num) == True):
        primes.append(num)

# output
print(primes)