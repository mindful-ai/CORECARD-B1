Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # SETS
>>> 
>>> s = "mississippi"
>>> list(s)
['m', 'i', 's', 's', 'i', 's', 's', 'i', 'p', 'p', 'i']
>>> tuple(s)
('m', 'i', 's', 's', 'i', 's', 's', 'i', 'p', 'p', 'i')
>>> set(s)
{'i', 'p', 'm', 's'}
>>> 
>>> 
>>> s1 = set("abcdefg")
>>> s2 = {'e', 'f', 'g', 'h', 'i', 'j'}
>>> 
>>> s1
{'f', 'd', 'c', 'g', 'e', 'b', 'a'}
>>> s2
{'j', 'i', 'h', 'g', 'e', 'f'}
>>> s1 & s2
{'f', 'g', 'e'}
>>> s1 | s2
{'f', 'j', 'd', 'c', 'i', 'h', 'g', 'e', 'b', 'a'}
>>> s1 ^ s2
{'j', 'd', 'c', 'i', 'h', 'b', 'a'}
>>> 
>>> 
>>> s1.add('x')
>>> s1
{'f', 'd', 'c', 'g', 'e', 'x', 'b', 'a'}
>>> s3 = {'y', 'z'}
>>> s1.update(s3)
>>> s1
{'f', 'z', 'd', 'c', 'y', 'g', 'e', 'x', 'b', 'a'}
>>> 
>>> # You cannot access the elements with a subscript
>>> 
>>> 'x' in s1
True
>>> s1.remove('x')
>>> s1
{'f', 'z', 'd', 'c', 'y', 'g', 'e', 'b', 'a'}
>>> 
>>> 
>>> s1.union(s2)
{'z', 'a', 'j', 'd', 'c', 'i', 'y', 'h', 'g', 'e', 'b', 'f'}
>>> s1.intersection(s2)
{'f', 'g', 'e'}
>>> 
