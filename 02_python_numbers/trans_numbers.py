Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Experiments with numbers
>>> 
>>> a= 10
>>> b = 5
>>> type(a)
<class 'int'>
>>> f = 10.56
>>> type(f)
<class 'float'>
>>> e = -56
>>> f =-0.56764
>>> 
>>> # ----------------------- Operators
>>> 
>>> # Arithmetic operators, relational operators, logical operators
>>> 
>>> # Arithmetic operators
>>> 
>>> a
10
>>> print(a)
10
>>> a + b
15
>>> a - b
5
>>> c = a + b
>>> c
15
>>> print(c)
15
>>> a * b
50
>>> a / b
2.0
>>> a % b
0
>>> 5 % 3
2
>>> 5 // 3
1
>>> 5 ** 2
25
>>> (a + b) ** a//2
288325195312
>>> r = 1000
>>> dc = 78
>>> d = r / dc
>>> print(d)
12.820512820512821
>>> 
>>> 
>>> 7/3
2.3333333333333335
>>> 7//3
2
>>> 7%3
1
>>> # Relational operators
>>> 
>>> a > b # Is a greater than b?
True
>>> a < b
False
>>> a == b * 2
True
>>> a != b**2
True
>>> a == b**2
False
>>> a >= b
True
>>> a <= b
False
>>> 
>>> # Logical operators
>>> 
>>> a > b and a < 10
False
>>> a > b or a < 10
True
>>> a > b and not a < 10
True
>>> 
>>> 
>>> # ----------------------- in-built functions
>>> 
>>> a = 100
>>> print(a)
100
>>> type(a)
<class 'int'>
>>> 
>>> float(a)
100.0
>>> bin(a)
'0b1100100'
>>> hex(a)
'0x64'
>>> oct(a)
'0o144'
>>> 
>>> s = '1234'
>>> s + 10
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    s + 10
TypeError: can only concatenate str (not "int") to str
>>> int(s) + 10
1244
>>> float(s) + 10
1244.0
>>> 
>>> 
>>> s = '1011101'
>>> 
>>> int(s)
1011101
>>> int(s)/ 2
505550.5
>>> int(s, 2)
93
>>> bin(93)
'0b1011101'
>>> int(s, 2)/2
46.5
>>> 
>>> 
>>> a = 10
>>> b = 4
>>> a - b
6
>>> b - a
-6
>>> abs(b - a)
6
>>> 
>>> 
>>> # Using the python built-in modules
>>> 
>>> gcd(65, 105)
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    gcd(65, 105)
NameError: name 'gcd' is not defined
>>> import math
>>> gcd(65, 105)
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    gcd(65, 105)
NameError: name 'gcd' is not defined
>>> math.gcd(65, 105)
5
>>> math.lcm(65, 105)
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    math.lcm(65, 105)
AttributeError: module 'math' has no attribute 'lcm'
>>> # lcm() is new in python 3.9 and above
>>> 
>>> math.sqrt(144)
12.0
>>> 
>>> 
>>> a = 90
>>> math.sin(a)
0.8939966636005579
>>> math.sin(a * 3.14/180)
0.9999996829318346
>>> 22/7
3.142857142857143
>>> math.sin(a * 3.142857142857143/180)
0.9999998001333682
>>> math.sin(a * math.pi/180)
1.0
>>> math.sin(math.radians(a))
1.0
>>> 

>>> import random
>>> random.randint(1, 100)
13
>>> random.randint(1, 100)
40
>>> random.randint(1, 100)
38
>>> random.randint(1, 100)
7
>>> random.randint(1, 100)
64
>>> random.randint(1, 100)
75
>>> random.randint(1, 100)
52
>>> 
