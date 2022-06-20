Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # TUPLES
>>> 
>>> L = ["red", "green", "blue"]
>>> type(L)
<class 'list'>
>>> T = ("red", "green", "blue")
>>> type(T)
<class 'tuple'>
>>> 
>>> # ----------------------------- accessing elements
>>> 
>>> T[0]
'red'
>>> T[-1]
'blue'
>>> T[:2]
('red', 'green')
>>> T[::-1]
('blue', 'green', 'red')
>>> 
>>> # ------------------------------ immutability of tuples
>>> 
>>> L[0]
'red'
>>> L[0] = "yellow"
>>> L
['yellow', 'green', 'blue']
>>> T[0]
'red'
>>> T[0] = "yellow"
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    T[0] = "yellow"
TypeError: 'tuple' object does not support item assignment
>>> 
>>> # --------------------------------------------
>>> # Because of immutable nature, you cannot add elements into tuple and
>>> # You cannot remove elements from the tuple
>>> # --------------------------------------------
>>> 
>>> # you cannot do in-place re-arrangement
>>> 
>>> 
>>> sorted(L)
['blue', 'green', 'yellow']
>>> L.sort() # in-place re-arrangement, because it changes the original List
>>> 
>>> sorted(T)
['blue', 'green', 'red']
>>> T
('red', 'green', 'blue')
>>> reversed(T)
<reversed object at 0x000002C38D78DCF8>
>>> tuple(reversed(T))
('blue', 'green', 'red')
>>> T
('red', 'green', 'blue')
>>> 
>>> 
>>> # ---------------------------------- operators
>>> 
>>> (1, 2, 3) + (4, 5, 6)
(1, 2, 3, 4, 5, 6)
>>> (1, 2, 3) * 3
(1, 2, 3, 1, 2, 3, 1, 2, 3)
>>> len(T)
3
>>> 'red' in T
True
>>> type(T) == tuple
True
>>> isinstance(T, tuple)
True
>>> del T
>>> T
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    T
NameError: name 'T' is not defined
>>> 
>>> 
>>> # ------------------------------- searching
>>> 
>>> T = ('red', 'green', 'blue')
>>> 'red' in T
True
>>> T.index('red')
0
>>> T.counf('red')
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    T.counf('red')
AttributeError: 'tuple' object has no attribute 'counf'
>>> T.count('red')
1
>>> 
>>> # ---------------------------- iteration
>>> 
>>> for item in T:
	print(item.upper(), end=' ')

	
RED GREEN BLUE 
>>> 
>>> # ------------------------------ changing/modifying a tuple when needed
>>> 
>>> record = ("Anil Kumar", 35, "CoreCard", "Indore", "India")
>>> record[-2] = 'Bhopal'
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    record[-2] = 'Bhopal'
TypeError: 'tuple' object does not support item assignment
>>> 
>>> 
>>> temp = list(record)
>>> temp
['Anil Kumar', 35, 'CoreCard', 'Indore', 'India']
>>> temp[-1] = "Bhopal"
>>> temp
['Anil Kumar', 35, 'CoreCard', 'Indore', 'Bhopal']
>>> ['Anil Kumar', 35, 'CoreCard', 'Indore', 'Bhopal']
['Anil Kumar', 35, 'CoreCard', 'Indore', 'Bhopal']
>>> record = tuple(temp)
>>> record
('Anil Kumar', 35, 'CoreCard', 'Indore', 'Bhopal')
>>> 
