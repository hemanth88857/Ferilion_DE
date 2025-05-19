"""
Author : GOVIND
Date   : 18-04-2025
"""
"""
req:
----
state    : dt/ds input output
behavior : BL - CRUD - DM LOOPS OPERATORS

mutable   : list set dict - CRUD
immutable : int float complex bool None str tuple

iterables  : str list tuple set dict range
sequence   : str list tuple range
unordered  : set

operators: 
----------
AC L MA IB

DM
---
if elif else

loops:
------
for    - finite - iterables
while  - conditional based iteration, unknown iteration count

control statements :
----------------------
break continue pass


string:
-------
immutable
sequence
ordered
'' "" ''' ''' """ """
builtin methods - 47

sequence ops:
--------------
indexing      - positive negative
slicing       -
concatenation - only with same sequence type
repetition    - only with integers
min
max
in
len
common builtin methods: count index

s = "python world"

-12 -11 -10 -9  -8  -7  -6  -5  -4  -3  -2  -1
p   y   t   h   o   n   .   w   o   r   l   d
0   1   2   3   4   5   6   7   8   9   10  11

-12 -11 -10 -9  -8  -7  -6  -5  -4  -3  -2  -1 0   1   2   3   4   5   6   7   8   9   10  11

ASCII - 128
"""
# s = 'python'
# s = """first line
# second line
# third line
# """
# print(s, type(s))
#
# def add(num1, num2):
#     """
#     add is going to take two int and returns value
#     :param num1: int
#     :param num2: int
#     :return: int
#     """
# s = "python"
# print(s)
# del s


# s = input("enter a string: ")
s = "python world"
# print(s[0])
# print(s[-1])
# print(s[5])
# print(s[-5])
# print(s[11])
# print(s[15])
# print(s[0: 4])
# print(s[5: 9])
# print(s[-10: -2])
# print(s[3: 20])
# print(s[-6: -1])
# print(s[-8: 10])
# print(s[-3: -10: -1])
# print(s[2: 10: 3])
# print(s[10: 2: -2])
# print(s[3:])
# print(s[-5:])
# print(s[:6])
# print(s[:-6])
# print(s[::])
# print(s[::-1])
'concatenation'
# s1 = "100"
# s2 = "200"

# s3 = s1 + s2
# print(s3)
#
# ls = ["python", "world", "hello"]
# s = ", ".join(ls)
# print(s)
# a = "python"
# b = "world"
# c = "hello"
#
# print(a + b + c)

# s3 = s1 * False
# print(s3)

'in'
# s = "python world"
# x = s[0:3]
# print(x)
# print("pt" in s)
#
# s = "python world"
# print(len(s))

"min max"

# s = "அఈಘAa"
# print("min is", min(s))
# print("max is", max(s))

# print(ord("அ"))
# print(ord("ఈ"))
# print(ord("ಘ"))
# print(chr(1114111))

# s = "python"
# print(s[0])
# print(s[1])
# print(s[2])
# print(s[3])
# print(s[4])
# print(s[5])

"""
-6  -5  -4  -3  -2  -1
p   y   t   h   o   n
0   1   2   3   4   5


for +ve indexing range len

0   1   2   3   4   5
range(6)
len(s) = 6
range(len(s))

for each in range(len(s)):
    print(s[each])


-6  -5  -4  -3  -2  -1
p   y   t   h   o   n
0   1   2   3   4   5

for -ve indexing range len

-6  -5  -4  -3  -2  -1
range(-6, 0)
len(s) = 6
range(-len(s), 0)


reverse order
=================
-6  -5  -4  -3  -2  -1
p   y   t   h   o   n
0   1   2   3   4   5


for +ve indexing range len

5 4 3 2 1 0
range(5, -1, -1)
len(s) = 6
range(len(s)-1, -1, -1)


-6  -5  -4  -3  -2  -1
p   y   t   h   o   n
0   1   2   3   4   5


for -ve indexing range len

-1 -2 -3 -4 -5 -6
range(-1, -7, -1)
len(s) = 6
range(-1, -len(s)-1, -1)
range(-1, -(len(s)+1), -1)


"""
s = "python"
"""
for each in s:
    print(each)

for each in range(len(s)):
    print(s[each])

for each in range(-len(s), 0):
    print(s[each])

"""

"""
for each in range(len(s)-1, -1, -1):
    print(s[each])


for each in range(-1, -len(s)-1, -1):
    print(s[each])
"""
