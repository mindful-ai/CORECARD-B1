Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> L = ["anil", 35, "1500000 INR", "CoreCard", "Bhopal", "India"]
>>> print(L[2])
1500000 INR
>>> D = {"name":"anil", "age":35, "salary":"1500000 INR", "company":"CoreCard", "place":"Bhopal", "country":"India"}
>>> type(D)
<class 'dict'>
>>> L[2]
'1500000 INR'
>>> D['salary']
'1500000 INR'
>>> 
>>> 
>>> 
>>> D['salary']
'1500000 INR'
>>> D['salary'] = '1600000 INR'
>>> D
{'name': 'anil', 'age': 35, 'salary': '1600000 INR', 'company': 'CoreCard', 'place': 'Bhopal', 'country': 'India'}
>>> 
>>> D.pop('age')
35
>>> D
{'name': 'anil', 'salary': '1600000 INR', 'company': 'CoreCard', 'place': 'Bhopal', 'country': 'India'}
>>> D['dob']
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    D['dob']
KeyError: 'dob'
>>> D['dob'] = "15/09/1999"
>>> D
{'name': 'anil', 'salary': '1600000 INR', 'company': 'CoreCard', 'place': 'Bhopal', 'country': 'India', 'dob': '15/09/1999'}
>>> 
>>> 
>>> 
>>> D.keys()
dict_keys(['name', 'salary', 'company', 'place', 'country', 'dob'])
>>> D.value()
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    D.value()
AttributeError: 'dict' object has no attribute 'value'
>>> D.values()
dict_values(['anil', '1600000 INR', 'CoreCard', 'Bhopal', 'India', '15/09/1999'])
>>> D.items()
dict_items([('name', 'anil'), ('salary', '1600000 INR'), ('company', 'CoreCard'), ('place', 'Bhopal'), ('country', 'India'), ('dob', '15/09/1999')])
>>> 
>>> 
>>> 
