"""
Author : GOVIND
Date   : 12-04-2025
"""
"""
variables
operators

req:
----
state    : dt/ds input output
behavior : BL - CRUD - DM LOOPS OPERATORS

immutable  : int float complex bool None str tuple - CRD
mutable    : list set dict - CRUD

iterables  : str list tuple set dict
unordered  : set
sequence   : str, list, tuple

OPERATORS:
----------
AC L MA IB


check the given number is prime or not

input state  : int      7       9               15 
output state : str      prime  not a prime    not a prime

2 3 4 5 6 

7

OPERATORS
---------
keywords , symbols

AC L MA IB


"""
"Arithmetic Operators"
"+ - * / // % **"

# n1 = {10, 20}
# n2 = False
# res = n1 * n2
# print(res)

"Comparison Operators"

"> < >= <= == !="

# n1 = {"b": 0}
# n2 = {"a": 10}
# # print(ord("A"))
# # print(ord("a"))
# print(n1 > n2)

"Logical Operators - DM"
"and or not"

"""
p   q       p and q         p or q
-   -       -------         ------
T   T           T               T
T   F           F               T
F   T           F               T
F   F           F               F


"""
# print(True and True)
# print(True and False)
# print(5 and 10)
# print(100 and 5)
# print("a" and "b")
# print(0 and 5)
# print(10 and 0)
# print(-10 and 5)
# print(5 and "a")
# print("" and "python")
# print(0 and "")
# print([] and 10)
""
# print(True or True)
# print(True or False)
# print(5 or 10)
# print(100 or 5)
# print("a" or "b")
# print(0 or 5)
# print(10 or 0)
# print(-10 or 5)
# print(5 or "a")
# print("" or "python")
# print(0 or "")
# print([] or 10)

'not'
#
# s = 0
# s = 10
# s = ''
# s = None
# s = []
# s = ()
# s = set()
# s = {}
#
# if not s:
#     print("there is no data")
# else:
#     print("data is present")

"""
lowercase  - variable, function      
snake_case - variable, function
UPPERCASE  - constants
PascalCase - Class
camelCase  - special function,class
SCREAMING_SNAKE_CASE - constants


"""
'constants'
URL = ""
TIME_OUT = 500


