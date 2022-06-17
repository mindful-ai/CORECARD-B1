Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # LISTS

>>> L = [12, 1.45, -45, "red", "green", "blue", [1, 2, 3]]
>>> type(L)
<class 'list'>
>>> 
>>> # ------------------------------- accessing elements
>>> 
>>> L
[12, 1.45, -45, 'red', 'green', 'blue', [1, 2, 3]]
>>> L[0]
12
>>> L[2]
-45
>>> L[-1]
[1, 2, 3]
>>> L[-1][2]
3
>>> L[1:5]
[1.45, -45, 'red', 'green']
>>> L[::-1]
[[1, 2, 3], 'blue', 'green', 'red', -45, 1.45, 12]
>>> L[::2]
[12, -45, 'green', [1, 2, 3]]
>>> 
>>> # ------------------------------ mutability
>>> 
>>> L
[12, 1.45, -45, 'red', 'green', 'blue', [1, 2, 3]]
>>> L[3]
'red'
>>> L[3] = 'golden'
>>> L
[12, 1.45, -45, 'golden', 'green', 'blue', [1, 2, 3]]
>>> 
>>> L[3]
'golden'
>>> L[3][2]
'l'
>>> L[3][2] = 'x'
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    L[3][2] = 'x'
TypeError: 'str' object does not support item assignment
>>> L[-1]
[1, 2, 3]
>>> L[-1][0]
1
>>> L[-1][0] = 5
>>> L
[12, 1.45, -45, 'golden', 'green', 'blue', [5, 2, 3]]
>>> 
>>> 
>>> # ---------------------------------- operators
>>> 
>>> [1, 2, 3] + [4, 5, 6]
[1, 2, 3, 4, 5, 6]
>>> [1, 2, 3] * 4
[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
>>> L
[12, 1.45, -45, 'golden', 'green', 'blue', [5, 2, 3]]
>>> 'golden' in L
True
>>> len(L)
7
>>> type(L) == list
True
>>> isinstance(L, list)
True
>>> del L
>>> L
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    L
NameError: name 'L' is not defined
>>> 
>>> # ---------------------------------- adding elements
>>> 
>>> L = ["red", "green", "blue"]
>>> L.append("golden")
>>> L
['red', 'green', 'blue', 'golden']
>>> L.append("yellow")
>>> L
['red', 'green', 'blue', 'golden', 'yellow']
>>> L.insert(1, "pink")
>>> L
['red', 'pink', 'green', 'blue', 'golden', 'yellow']
>>> L1 = ["black", "grey", "white']
      
SyntaxError: EOL while scanning string literal
>>> L1 = ["black", "grey", "white"]
>>> L.extend(L1)
>>> L
['red', 'pink', 'green', 'blue', 'golden', 'yellow', 'black', 'grey', 'white']
>>> 
>>> 
>>> # ----------- variations/modifications
>>> 
>>> L
['red', 'pink', 'green', 'blue', 'golden', 'yellow', 'black', 'grey', 'white']
>>> L[0] = "deepred"
>>> L
['deepred', 'pink', 'green', 'blue', 'golden', 'yellow', 'black', 'grey', 'white']
>>> L = ["red", "green", "blue"]
>>> L[1]
'green'
>>> L[1] = ['golden', 'yellow']
>>> L
['red', ['golden', 'yellow'], 'blue']
>>> 
>>> 
>>> L = ["red", "green", "blue"]
>>> L[1:2]
['green']
>>> L[1:2] = ["golden", "orange"]
>>> L
['red', 'golden', 'orange', 'blue']
>>> 
>>> # --------------------------------------- Removing elements
>>> 
>>> L
['red', 'golden', 'orange', 'blue']
>>> L.pop()
'blue'
>>> L
['red', 'golden', 'orange']
>>> L.pop(0)
'red'
>>> L
['golden', 'orange']
>>> L.remove("orange")
>>> L
['golden']
>>> 
>>> 
>>> # -------------------------------------- Re-arranging elements
>>> 
>>> L = ['red', 'pink', 'green', 'blue', 'golden', 'yellow', 'black', 'grey', 'white']
>>> L
['red', 'pink', 'green', 'blue', 'golden', 'yellow', 'black', 'grey', 'white']
>>> L[::-1
  ]
['white', 'grey', 'black', 'yellow', 'golden', 'blue', 'green', 'pink', 'red']
>>> reversed(L)
<list_reverseiterator object at 0x0000028DBEB9C080>
>>> list(reversed(L))
['white', 'grey', 'black', 'yellow', 'golden', 'blue', 'green', 'pink', 'red']
>>> L
['red', 'pink', 'green', 'blue', 'golden', 'yellow', 'black', 'grey', 'white']
>>> 
>>> 
>>> L.reverse()
>>> L
['white', 'grey', 'black', 'yellow', 'golden', 'blue', 'green', 'pink', 'red']
>>> 
>>> 
>>> 
>>> sorted(L)
['black', 'blue', 'golden', 'green', 'grey', 'pink', 'red', 'white', 'yellow']
>>> L
['white', 'grey', 'black', 'yellow', 'golden', 'blue', 'green', 'pink', 'red']
>>> L.sort()
>>> L
['black', 'blue', 'golden', 'green', 'grey', 'pink', 'red', 'white', 'yellow']
>>> # reversed(), sorted() do not change the original array
>>> # reverse() and sort() act on the original array
>>> 
>>> 
>>> # ------------------------- search for elements
>>> 
>>> L
['black', 'blue', 'golden', 'green', 'grey', 'pink', 'red', 'white', 'yellow']
>>> 'black' in L
True
>>> L.index('red')
6
>>> L.count('red')
1
>>> L.append('red')
>>> L.count('red')
2
>>> # ------------------------------ special functions on numeric arrays
>>> 
>>> L = [23, 45, 56, 67]
>>> len(L)
4
>>> sum(L)
191
>>> max(L)
67
>>> min(L)
23
>>> any(L)
True
>>> all(L)
True
>>> L.append(0)
>>> L
[23, 45, 56, 67, 0]
>>> all(L)
False
>>> 
>>> # --------------------------------- iterate on an array
>>> 
>>> L = ["red", "green", "blue"]
>>> for item in L:
	print(item)

	
red
green
blue
>>> 
