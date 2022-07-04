a = input("Enter a number: ")
b = input("Enter another number: ")

try:
    print('The result is ', int(a)/int(b))
except Exception as E:
    print('Incorrect inputs', E)
else:
    print('Operation completed')
finally:
    print('Thank you')


print("Next program block starts")

try:
    print('The result is ', int(a)/int(b))
    D = {'name':0}
    print(D['name'])
    open('xyz')
    print(a + 10)
except ZeroDivisionError:
    print('Incorrect inputs', E)
except KeyError:
    print("No key found")
except:
    print('Some other error')
else:
    print('Operation completed')
finally:
    print('Thank you')

# Refer https://www.tutorialspoint.com/python/standard_exceptions.htm for the list of exceptions
