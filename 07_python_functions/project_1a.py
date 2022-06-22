'''
Syntax for function definition ->
def <function name>(<inputs>):
    <logic>
    return <output>
'''

def checkprime(n):
    for i in range(2, n):
        if(n % i == 0):
            return False
    return True

def getprimes(start, end):
    primes = []
    for n in range(start, end + 1):
        if(checkprime(n) == True):
            primes.append((n))
    return tuple(primes)


def gethighestprime(n):
    pass

# ----------------------------------

print('Project 1A __name__ = ', __name__)
if __name__ == "__main__":
    # input
    x = int(input("[Project 1a]Enter a number: "))

    # process/output
    if(checkprime(x) == True):
        print("The number is prime")
    else:
        print("The number is not prime")