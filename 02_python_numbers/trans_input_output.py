Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Inputs and output
>>> 
>>> a = 10
>>> b = 20
>>> print(a + b
)
30
>>> print("The sum of two numbers is", a+b )
The sum of two numbers is 30
>>> print("The sum of %d and %d is %d" % (a, b, a+b))
The sum of 10 and 20 is 30
>>> 
>>> 
>>> input()
45
'45'
>>> a = input()
45
>>> a
'45'
>>> a = input("Enter a number: ")
Enter a number: 45
>>> a
'45'
>>> print(a ** 2)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print(a ** 2)
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
>>> print(float(a) ** 2)
2025.0
>>> 
>>> 
>>> a = int(input("Enter a number: "))
Enter a number: 45
>>> a ** 2
2025
>>> 
