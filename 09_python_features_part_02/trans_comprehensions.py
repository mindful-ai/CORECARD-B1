Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Comprehensions
>>> 
>>> L = list(range(1, 11))
>>> L
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> # [1, 2, 9, 16 .... 100]
>>> 
>>> L2 = []
>>> for n in L:
	L2.append(n**2)

	
>>> L2
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>> 
>>> # -------------------- new technique
>>> 
>>> L2 = [x**2 for x in n]
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    L2 = [x**2 for x in n]
TypeError: 'int' object is not iterable
>>> n
10
>>> L2 = [x**2 for x in L]
>>> L2
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>> 
>>> 
>>> # [4, 16, 36 .. 100]
>>> L3 = [x**2 for x in L if  x % 2 == 0]
>>> L3
[4, 16, 36, 64, 100]
>>> 
>>> 
>>> 
>>> 
>>> S = ["red", "green", "blue", "yellow"]
>>> # ["der", "neerg", ....]
>>> L4 = [s[::-1] for s in S]
>>> L4
['der', 'neerg', 'eulb', 'wolley']
>>> 
>>> 
>>> # ------------------ comprehension syntax
>>> 
>>> # comprehension are generally used for creating collections
>>> # [], (), {} {k:v}
>>> 
>>> # Let's say we want to create a list comprehension - choose []
>>> # [<expr> <loop> <condition>]if  x % 2 == 0
>>> 
>>> 
>>> # Syntax: [<expr> <loop> <condition>]
>>> 
>>> # Create a list of numbers between 1 and 1000 which are divisibly by 7 and 13
>>> 
>>> LN = [x for x in range(1, 1000) if x % 7 == 0 and x % 13 == 0]
>>> LN
[91, 182, 273, 364, 455, 546, 637, 728, 819, 910]
>>> 
>>> # Create a list of tuples which has the number and it's square and cube
>>> # [(1, 1, 1), (2, 4, 8)...]
>>> 
>>> LT = [(n, n**2, n**3) for n in range(1, 11)]
>>> LT
[(1, 1, 1), (2, 4, 8), (3, 9, 27), (4, 16, 64), (5, 25, 125), (6, 36, 216), (7, 49, 343), (8, 64, 512), (9, 81, 729), (10, 100, 1000)]
>>> 
>>> 
>>> # Create a dictionary which has the string and the length of the string as it's key value pair
>>> # {'red': 3, 'green':5 .. }
>>> s
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    s
NameError: name 's' is not defined
>>> S
['red', 'green', 'blue', 'yellow']
>>> 
>>> SD = { s : len(s) for s in S }
>>> SD
{'red': 3, 'green': 5, 'blue': 4, 'yellow': 6}
>>> 
>>> SD1 = {s : len(s) for s in S if len(s) > 3 }
>>> SD1
{'green': 5, 'blue': 4, 'yellow': 6}
>>> 
>>> 
>>> # Convert the temperatures from celcius to farenheit
>>> 
>>> T = (12, 34, 45, 56, 67, 98)
>>> F = [t * 1.8 + 32 for t in T]
>>> F
[53.6, 93.2, 113.0, 132.8, 152.60000000000002, 208.4]
>>> 
>>> # Raise the number to the power of 2 if they are multiples of 3 otherwise keep
>>> # the number as is
>>> 
>>> N = list(range(1, 11))
>>> N
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> # [1, 2, 9, 4, 5, 36, 7, 8, 81, 10]
>>> 
>>> N = [x for x in N if x % 3 == 0]
>>> N
[3, 6, 9]
>>> N = [x**2 for x in N if x % 3 == 0]
>>> N
[9, 36, 81]
>>> N = list(range(1, 11))
>>> N1 = [x**2 if x % 3 == 0 else x for x in N]
>>> N1
[1, 2, 9, 4, 5, 36, 7, 8, 81, 10]
>>> 
>>> 
>>> # Multiple for loops
>>> 
>>> P = [(x, y) for x in range(1, 11) for y in range(1, 11) if x + y % 13 == 0]
>>> P
[]
>>> P = [(x, y) for x in range(1, 11) for y in range(1, 11) if (x + y) % 13 == 0]
>>> P
[(3, 10), (4, 9), (5, 8), (6, 7), (7, 6), (8, 5), (9, 4), (10, 3)]
>>> 
>>> 
>>> # Generate a list of all two digit numbers and then
>>> # create a list of all two digit numbers whose individual digits sum is equal to 10
>>> 
>>> # D2 = [10, 11, .... 99]
>>> # D2_10 -> [19, 28, 37, 46 ... 91]
>>> 
>>> 
