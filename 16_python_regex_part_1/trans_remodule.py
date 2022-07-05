Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s = "This contain 45.67 floating 98.442 point numbers"
>>> p = r"\d+\.?\d*"
>>> import re
>>> m = re.search(p, s)
>>> m
<re.Match object; span=(13, 18), match='45.67'>
>>> s[13:18]
'45.67'
>>> re.findall(p, s)
['45.67', '98.442']
>>> 
>>> m.group()
'45.67'
>>> m.span()
(13, 18)
>>> m.start()
13
>>> m.end()
18
>>> 
>>> 
>>> p = r"(\d+)\.?(\d*)"
>>> m = re.search(p, s)
>>> m.group()
'45.67'
>>> m.groups()
('45', '67')
>>> 
>>> 
>>> p = r"(?P<integer>\d+)\.?(?P<decimal>\d*)"
>>> m = re.search(p, s)
>>> m.group()
'45.67'
>>> m.groups()
('45', '67')
>>> m.groupdict()
{'integer': '45', 'decimal': '67'}
>>> 
>>> 
>>> 
>>> 
