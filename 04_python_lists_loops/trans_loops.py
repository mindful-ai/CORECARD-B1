Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> for ch in "python":
	print(ch)

	
p
y
t
h
o
n
>>> for ch in "python":
	print(ch, end=' ')

	
p y t h o n 
>>> for item in ["red", "green", "blue"]:
	print(item.upper(), end=' ')

	
RED GREEN BLUE 
>>> for i in [1, 2, 3, 4, 5]:
	print(5, ' X ', i, ' = ', 5*i)

	
5  X  1  =  5
5  X  2  =  10
5  X  3  =  15
5  X  4  =  20
5  X  5  =  25
>>> 
>>> 
>>> range(10)
range(0, 10)
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(10, 20))
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> list(range(1, 100, 5))
[1, 6, 11, 16, 21, 26, 31, 36, 41, 46, 51, 56, 61, 66, 71, 76, 81, 86, 91, 96]
>>> list(range(10, 1, -1))
[10, 9, 8, 7, 6, 5, 4, 3, 2]
>>> 
>>> 
>>> for i in range(1, 11):
	print(5, ' X ', i, ' = ', 5*i)

	
5  X  1  =  5
5  X  2  =  10
5  X  3  =  15
5  X  4  =  20
5  X  5  =  25
5  X  6  =  30
5  X  7  =  35
5  X  8  =  40
5  X  9  =  45
5  X  10  =  50
>>> 
>>> i = 1
>>> while i <= 10:
	print(5, ' X ', i, ' = ', 5*i)
	i += 1

	
5  X  1  =  5
5  X  2  =  10
5  X  3  =  15
5  X  4  =  20
5  X  5  =  25
5  X  6  =  30
5  X  7  =  35
5  X  8  =  40
5  X  9  =  45
5  X  10  =  50
>>> 
>>> 
>>> # ------------------------- Loop control statements
>>> 
>>> for i in range(1, 11):
	if(i == 5):
		break
	print(5, ' X ', i, ' = ', 5*i)

	
5  X  1  =  5
5  X  2  =  10
5  X  3  =  15
5  X  4  =  20
>>> 
>>> for i in range(1, 11):
	if(i % 3 == 0):
		continue
	print(5, ' X ', i, ' = ', 5*i)

	
5  X  1  =  5
5  X  2  =  10
5  X  4  =  20
5  X  5  =  25
5  X  7  =  35
5  X  8  =  40
5  X  10  =  50
>>> 
