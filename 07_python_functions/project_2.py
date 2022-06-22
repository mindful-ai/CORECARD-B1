# Accept a series of numbers from the user
# filter all the prime numbers

# input

n = input("Enter the numbers: ")
n = n.split()
n = list(map(lambda s : int(s), n))
print(n)

# process

primes = []
for num in n:
    prime = True
    for i in range(2, num):
        if(num % i == 0):
            prime = False
            break
    if(prime == True):
        primes.append(num)

# output
print(primes)
