Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> T = [12, 34, 56, 67, 78, 100] # These temperatures are in celcius
>>> F = []
>>> for t in T:
	F.append(t * 1.8 + 32)

	
>>> F
[53.6, 93.2, 132.8, 152.60000000000002, 172.4, 212.0]
>>> 
>>> 
>>> 
>>> # Lambda functions
>>> # It is a simple expression that can create a function objects
>>> 
>>> f = lambda x : x**2
>>> type(f)
<class 'function'>
>>> f(5)
25
>>> f(10)
100
>>> 
>>> 
>>> # map()
>>> 
>>> T
[12, 34, 56, 67, 78, 100]
>>> F1 = map(lambda t : t * 1.8 + 32, T)
>>> F1
<map object at 0x0000011F4DEC3208>
>>> list(F1)
[53.6, 93.2, 132.8, 152.60000000000002, 172.4, 212.0]
>>> 
>>> 
>>> 
>>> N = [1, 2, 3, 4, 5]
>>> # [1, 4, 9, 16, 25]
>>> N1 = map(lambda x : x**2, N)
>>> N1
<map object at 0x0000011F4DEC3240>
>>> list(N1)
[1, 4, 9, 16, 25]
>>> 
>>> 
>>> N1
<map object at 0x0000011F4DEC3240>
>>> for item in N1:
	print(item)

	
>>> N1 = map(lambda x : x**2, N)
>>> for item in N1:
	print(item)

	
1
4
9
16
25
>>> for item in N1:
	print(item)

	
>>> 
>>> # ------------------------------------------- filter()
>>> 
>>> import random
>>> R = []
>>> for i in range(100):
	R.append(random.randint(1, 100))

	
>>> R
[58, 22, 27, 85, 59, 11, 47, 12, 65, 84, 46, 82, 27, 74, 76, 81, 62, 98, 82, 72, 64, 5, 39, 19, 90, 99, 22, 38, 13, 25, 1, 61, 84, 30, 15, 94, 90, 13, 73, 75, 87, 62, 57, 23, 78, 87, 41, 50, 45, 58, 7, 48, 86, 60, 70, 95, 96, 96, 41, 50, 36, 81, 89, 2, 49, 83, 57, 25, 34, 2, 45, 20, 84, 7, 59, 49, 45, 20, 34, 61, 39, 36, 47, 35, 75, 76, 26, 40, 99, 42, 54, 21, 2, 3, 23, 14, 84, 47, 95, 47]
>>> 
>>> 
>>> # I need to extract all the 1 digit numbers
>>> 
>>> R10 = []
>>> for n in R:
	if(n < 10):
		R10.append(n)

		
>>> R10
[5, 1, 7, 2, 2, 7, 2, 3]
>>> 
>>> 
>>> R10F = filter(lambda n : (n < 10), R)
>>> R10F
<filter object at 0x0000011F4DEC3518>
>>> list(R10F)
[5, 1, 7, 2, 2, 7, 2, 3]
>>> 
>>> 
>>> # How to extract all the double digit numbers
>>> 
>>> R2D = filter(lambda n : (9 < n < 100), R)
>>> R2D
<filter object at 0x0000011F4DEC3860>
>>> list(R2D)
[58, 22, 27, 85, 59, 11, 47, 12, 65, 84, 46, 82, 27, 74, 76, 81, 62, 98, 82, 72, 64, 39, 19, 90, 99, 22, 38, 13, 25, 61, 84, 30, 15, 94, 90, 13, 73, 75, 87, 62, 57, 23, 78, 87, 41, 50, 45, 58, 48, 86, 60, 70, 95, 96, 96, 41, 50, 36, 81, 89, 49, 83, 57, 25, 34, 45, 20, 84, 59, 49, 45, 20, 34, 61, 39, 36, 47, 35, 75, 76, 26, 40, 99, 42, 54, 21, 23, 14, 84, 47, 95, 47]
>>> 
>>> 
>>> # Filter all strings that has a 'e' in it
>>> 
>>> S = ['red', 'green', 'blue', 'maroon', 'pink', 'white']
>>> 'e' in 'red'
True
>>> f = lambda s : 'e' in s
>>> f('red')
True
>>> f('maroon')
False
>>> SE = filter(lambda s : 'e' in s, S)
>>> list(SE)
['red', 'green', 'blue', 'white']
>>> 
>>> 
>>> 
>>> # Convert all the words in to uppercase
>>> 
>>> SU = list(map(lambda s : s.upper(), S))
>>> SU
['RED', 'GREEN', 'BLUE', 'MAROON', 'PINK', 'WHITE']
>>> 
>>> 
>>> SUe = filter(lambda s : 'e' in s, list(map(lambda s : s.upper(), S)))
>>> SUe
<filter object at 0x0000011F4DEC3908>
>>> list(SUe)
[]
>>> SUe = filter(lambda s : 'e' in s, SU)
>>> SUe
<filter object at 0x0000011F4DEC39B0>
>>> list(SUe)
[]
>>> SU
['RED', 'GREEN', 'BLUE', 'MAROON', 'PINK', 'WHITE']
>>> SUe = filter(lambda s : 'E' in s, list(map(lambda s : s.upper(), S)))
>>> SUe
<filter object at 0x0000011F4DEC3438>
>>> list(SUe)
['RED', 'GREEN', 'BLUE', 'WHITE']
>>> 
>>> 
>>> 
>>> 
>>> # --------------------------------------- zip()
>>> 
>>> T1 = ("Anil", "Sunil", "Vinil")
>>> T2 = (34, 35, 36)
>>> 
>>> zip(T1, T2)
<zip object at 0x0000011F4DE48AC8>
>>> list(zip(T1, T2))
[('Anil', 34), ('Sunil', 35), ('Vinil', 36)]
>>> dict(zip(T1, T2))
{'Anil': 34, 'Sunil': 35, 'Vinil': 36}
>>> 
>>> 
>>> 
>>> D = {'Anil': 34, 'Sunil': 35, 'Vinil': 36}
>>> D.items()
dict_items([('Anil', 34), ('Sunil', 35), ('Vinil', 36)])
>>> zip(*D.items())
<zip object at 0x0000011F4DE48AC8>
>>> list(zip(*D.items()))
[('Anil', 'Sunil', 'Vinil'), (34, 35, 36)]
>>> 
