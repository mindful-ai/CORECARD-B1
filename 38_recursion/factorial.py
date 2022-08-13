def fact(n):
    numbers = [x for x in range(1, n+1)]
    res = 1
    for i in numbers:
        res = res * i
    return res

def factorial(n):
    if(n == 1):
        return 1
    else:
        return n * factorial(n - 1)

print(fact(5))
print(factorial(5))