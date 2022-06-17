Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # STRINGS

>>> s = "computer"
>>> type(s)
<class 'str'>
>>> 
>>> 
>>> # ----------------------- immutable aspect of strings
>>> 
>>> s[0]
'c'
>>> s[1]
'o'
>>> s[0] = 'x'
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    s[0] = 'x'
TypeError: 'str' object does not support item assignment
>>> 
>>> # ------------------------- subscripting
>>> 
>>> s
'computer'
>>> s[0]
'c'
>>> s[1]
'o'
>>> s[2]
'm'
>>> s[-1]
'r'
>>> s[-2]
'e'
>>> s[-3]
't'
>>> s[3:5]
'pu'
>>> s[3:6]
'put'
>>> s[0:3]
'com'
>>> s[:3]
'com'
>>> s[5:8]
'ter'
>>> s[5:]
'ter'
>>> s[:]
'computer'
>>> s[1:-1]
'ompute'
>>> s[1:7]
'ompute'
>>> s[1:7:2]
'opt'
>>> s[:]
'computer'
>>> s[::2]
'cmue'
>>> s[1::2]
'optr'
>>> s[::-1
  ]
'retupmoc'
>>> # ------------------------ operators
>>> 
>>> 'abcd' + 'efgh'
'abcdefgh'
>>> 'abcd' * 3
'abcdabcdabcd'
>>> len(s)
8
>>> type(s) == str
True
>>> isinstance(s, str)
True
>>> del s
>>> s
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    s
NameError: name 's' is not defined
>>> 
>>> # ----------------------- functions
>>> 
>>> # ------- case of the strings
>>> 
>>> s = "python"
>>> s.upper()
'PYTHON'
>>> s.lower()
'python'
>>> s.capitalize()
'Python'
>>> s
'python'
>>> 
>>> # ----------- string checking
>>> 
>>> '1234'.isdigit()
True
>>> '123s'.isdigit()
False
>>> '1234s'.isalnum()
True
>>> 'asd'.isalpha()
True
>>> '  '.isspace()
True
>>> s
'python'
>>> s.isupper()
False
>>> s.islower()
True
>>> s.istitle()
False
>>> t = "This Is A Title"
>>> t.istitle()
True
>>> 
>>> 
>>> site = "www.google.com"
>>> site.startswith("www")
True
>>> site.endswith("org")
False
>>> 
>>> # -------------------------- searching/finding
>>> 
>>> s
'python'
>>> 'th' in s
True
>>> 'app' in s
False
>>> s.find('a')
-1
>>> s.find('t')
2
>>> s = 'mississippi'
>>> s.count('s')
4
>>> s.count('ss')
2
>>> 
>>> # ----------------------------- modifying string content
>>> 
>>> ip = "127-45-56-8"
>>> newip = ip.replace('-', '.')
>>> newip
'127.45.56.8'
>>> 
>>> 
>>> text = " 123435    "
>>> text.strip()
'123435'
>>> text.lstrip()
'123435    '
>>> text.rstrip()
' 123435'
>>> 
>>> 
>>> ip
'127-45-56-8'
>>> text
' 123435    '
>>> 
>>> 
>>> text = "hello"
>>> text.ljust(20)
'hello               '
>>> text.rjust(20, '>')
'>>>>>>>>>>>>>>>hello'
>>> 
>>> 
>>> text = "mary had a little lamb"
>>> text.split()
['mary', 'had', 'a', 'little', 'lamb']
>>> text.split('a')
['m', 'ry h', 'd ', ' little l', 'mb']
>>> 
>>> 
>>> L = ['mary', 'had', 'a', 'little', 'lamb']
>>> '-'.join(L)
'mary-had-a-little-lamb'
>>> L = ['m', 'ry h', 'd ', ' little l', 'mb']
>>> 'A'.join(L)
'mAry hAd A little lAmb'
>>> 
>>> 
>>> # -------------------------- Advanced Functions
>>> 
>>> text = "computer"
>>> D = {'p':'pp', 't':'tt'}
>>> M = maketrans(D)
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    M = maketrans(D)
NameError: name 'maketrans' is not defined
>>> M = text.maketrans(D)
>>> M
{112: 'pp', 116: 'tt'}
>>> text.translate(M)
'compputter'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> nmae = "Purushotham"
>>> name = "Purushotham"
>>> age = "40"
>>> 
>>> print("My name is " + str(name) + " age is " + str(age))
My name is Purushotham age is 40
>>> print("My name is %s and age is %d" % (name, age))
Traceback (most recent call last):
  File "<pyshell#136>", line 1, in <module>
    print("My name is %s and age is %d" % (name, age))
TypeError: %d format: a number is required, not str
>>> print("My name is %s and age is %s" % (name, age))
My name is Purushotham and age is 40
>>> 
>>> 
>>> 
>>> 
>>> "My name is {} and age is {}".format(name, age)
'My name is Purushotham and age is 40'
>>> "My name is {0} and age is {1}".format(name, age)
'My name is Purushotham and age is 40'
>>> "My name is {1} and age is {1}".format(name, age)
'My name is 40 and age is 40'
>>> "My name is {0:15} and age is {1:5}".format(name, age)
'My name is Purushotham     and age is 40   '
>>> "My name is {0:>15} and age is {1:<5}".format(name, age)
'My name is     Purushotham and age is 40   '
>>> "My name is {0:^15} and age is {1:^5}".format(name, age)
'My name is   Purushotham   and age is  40  '
>>> 
>>> 
>>> template = "NAME: {0:^15} || AGE: {1:^5}"
>>> template.format('Anil', 30)
'NAME:      Anil       || AGE:  30  '
>>> template.format("Purushotham", 40)
'NAME:   Purushotham   || AGE:  40  '
>>> 
