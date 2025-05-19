"""
Author : GOVIND
Date   : 21-04-2025
"""
"""
req:
----
state    : dt/ds input output
behavior : BL - CRUD - DM LOOPS OPERATORS

mutable   : list set dict
immutable : int float complex bool None str tuple

iterables  : str list tuple set dict range
sequence   : str list tuple range
unordered  : set

operators:
-----------
AC L MA IB

DM
---
if elif else

loops:
------
for    - finite - iterables
while  - infinite

control statements: break continue pass

string:
-------
immutable
sequence
ordered
'' "" """ """ ''' '''
builtin methods - 47

common sequence ops:
---------------------
indexing   - positive indexing
slicing  
concatenation - with same sequence type
repetition   - only with integers
min
max
in
len

common builtin methods - count index

"""
# s = input("enter a string: ")

# print("first char: ", s[0])
# print("last char: ", s[-1])

# s = "python world"
# print(s[4: 25])
# #print(s[25])
# print(s[-5:])
# print(s[:6])
# print(s[::])
# print(s[::-1])

# name = "ramesh"
# age = 25
# sal = 91222.3863222

# ls = ["suresh", 30, 585896.38852]
# tp = ("ganesh", 32, 5896.38852)
# dc = {"name": "harish", "age": 35, "sal": 8752.98811}

# s = "name is " + name + " age is " + str(age) + " salary is " + str(sal)
# print(s)
# print("name is", name, "age is", age, "salary is", sal)

'f-strings - 3.6+'

# print(f"name is {name}, age is {age} and salary is {sal}")
# print(f"name is {name}, age is {age} and salary is {sal:.2f}")
# print(f"name is {ls[0]}, age is {ls[1]} and salary is {ls[2]:.2f}")
# print(f"name is {tp[0]}, age is {tp[1]} and salary is {tp[2]:.2f}")
# print(f"name is {dc['name']}, age is {dc["age"]} and salary is {dc["sal"]:.2f}")

'.format()'

# print("name is {}, age is {}, salary is {}".format(name, age, sal))
# print("name is {}, age is {}, salary is {:.2f}".format(name, age, sal))
# print("name is {}, age is {}, salary is {:.2f}".format(ls[0], ls[1], ls[2]))
# print("name is {}, age is {}, salary is {:.2f}".format(*ls))
# print("name is {}, age is {}, salary is {:.2f}".format(*tp))
# print("name is {}, age is {}, salary is {:.2f}".format(dc['name'], dc['age'], dc['sal']))
# print("name is {name}, age is {age}, salary is {sal:.2f}".format(**dc))

'old style formatting - %s %d %f (db, logging)'

# print("name is %s age is %d and salary is %f"%(name, age, sal))
# print("name is %s age is %d and salary is %.2f"%(name, age, sal))
# print("name is %s age is %s and salary is %s"%(name, age, sal))
# print("name is %s age is %s and salary is %s"%(ls[0], ls[1], ls[2]))
# print("name is %s age is %s and salary is %s"%tp)
# print("name is %(name)s age is %(age)s and salary is %(sal)s"%dc)


""""""
# it's good to learn python
# "python" is easy
# it's good to learn "python"

# s = "it's good to learn python"
# print(s)
# s = '"python" is easy'
# print(s)
# s = """it's good to learn "python" """
# print(s)

# s = r"tabspace\ttabspace\nnewline \'single quote\' \"double quote\""
# print(s)
# s = r"D:\Class\B34 B35\7. Data structures in detail\7.0.1 Datastructures in detail - String - 2\_7.0.1_strings\_7_01_str_.py"
# print(s)

# s = b"python"
# print(s, type(s))

'string conversions - str()'
# # s = 100
# s = [10, 20, 30]
# res = str(s)
# print(res, type(res))
# '[10, 20, 30]'

"""
s = "python"
print(s[0])
s[0] = "b"
print(s)
"""

# print(dir(str))

str_meth = ['capitalize', 'casefold', 'center', 'count', 'encode',
            'endswith', 'expandtabs', 'find', 'format', 'format_map',
            'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal',
            'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable',
            'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip',
            'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace',
            'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split',
            'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate',
            'upper', 'zfill']

# print(len(str_meth))

"""
lower upper title capitalize swapcase casefold - 6
count index rindex find rfind                  - 5
startswith endswith removeprefix removesuffix  - 4

isupper islower istitle isalpha isalnum isascii
isdigit isnumeric isdecimal isspace isprintable
isidentifier                                   - 12

strip rstrip lstrip                            - 3
split rsplit splitlines                        - 3

zfill rjust ljust center                       - 4

format format_map encode maketrans translate   - 5
expandtabs partition rpartition                - 3
join replace                                   - 2
"""

# s = "python ProgrMMIng LanguagE"
# s = "Straße"
# s = "100"
# res = s.lower()
# print(res)

# s = "python ProgrMMIng LanguagE"
# s = "pytphonp"
# print(s.rindex('p'))
# print(s.rfind('p'))

# res = s.find('z')
# if res == -1:
#     print("there is no such char ")
# else:
#     print("char is presnt")

# s = '¼'
# # s = "10"
# print(s.isdigit())
# print(s.isnumeric())

# s = "python progamming, language hello, world, good to learn"
# res = s.split(',', maxsplit=2)
# print(res)

# "['python progamming', ' language hello', ' world, good to learn']"
# "['python progamming, language hello', ' world', ' good to learn']"
#
# s = """first line
# second line
# third line"""
# print(s.splitlines())

# s = "python"
# print(s.zfill(10))
# print(s.center(11, "*"))
# print(s.ljust(10, "="))
# print(s.rjust(10, "$"))

# s = ["python", "flask", "django", "fastapi"]
# res = ", ".join(s)
# print(res)