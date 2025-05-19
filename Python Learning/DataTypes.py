"""
req:
----
state   : dt/ds input output
behavior : BL - CRUD - DM LOOPS OPERATORS

mutable   : list set dict  - CRUD
immutable : int float complex bool None str tuple - CRD

iterables : str list tuple set dict
unordered : set
sequence  : str list tuple

operators:
-----------
AC L MA IB


numbers:(immutable)
---------
int      : ....-3 -2 -1 0 1 2 3.......... 
float    : 3.5
complex  : 4+65j

bool:(immutable)
-----
True(1) False(0)

is_prime
is_active
is_permanent

None type:(immutable)
----------
None
no data, NA, nothing

0 vs None

datastructures
--------------
sequence, set, mapping type

sequence:
=========
str list tuple - (count, index)

str: (sequence of characters - 1114112 - ☻K#%^&*(98&)
---
-> immutable
-> sequence
-> ordered
-> '' "" ''' ''' """ """
-> builtin methods - 47

list:
-----
-> mutable
-> sequence
-> ordered
-> []
-> all dt/ds
-> homogenous data heterogeneous data
-> builtin methods - 11

tuple:
------
-> immutable
-> sequence
-> ordered
-> (), (ele,)
-> all dt/ds
-> homogenous data heterogeneous data
-> builtin methods - 2

-6  -5  -4  -3  -2  -1
p   y   t   h   o   n
0   1   2   3   4   5 - indexing

set type:
---------
set
---
-> mutable
-> unordered
-> set(), {ele}
-> set elements -> immutable, unique
-> builtin methods - 17

mapping type:
-------------
dict
----
-> mutable
-> ordered(3.7+)
-> {}, {key: value}
-> keys: immutable, unique
-> values : any dt/ds
-> builtin methods - 11
"""
#
# s = "python"
# print(s)
# print(s[2])
# print(s[-2])
#
# for each in s:
#     print(each)

# s = "it's good to learn python"
# s = '"python" is a good subject'
# s = """first line
# second line
# third line
# fourth line
# """
# print(s)

# s = "pytHOn ProGramming LANGUAGE"
# x = s.title()
# print(x)
# ls = [1, 3.5, 6j, True, None, "python", [10, 20], (30, 40), {50,60}, {"A":10, "B":20}]
# #    0   1     2   3       4       5       6       7           8           9
# print(ls, type(ls))
# print(ls[6])
# ls1 = ["python", "world", "programming"]

# tp = (1, 3.5, 6j, True, None, "python", [10, 20], (30, 40), {50,60}, {"A":10, "B":20})
# print(tp, type(tp))
#
# st = {1, 3.5, 6j, 1,1,1, None, "python", (30, 40)}
# print(st, type(st))
# """
# list set dict - mutable
# """
#
# dc= {1:"a", 3.5:2, 6j:3.5, True:[10], None:(10,20), "python":{50,60},
#      (30, 40):True}
# print(dc)

# ls = ["ramesh", 25, 6000, 70000, True, "chennai", "bangalore"]
#
# emp_names = ["ramesh", "suresh", "ganesh", "harish"]
#
# dc = {"name": "ramesh", "age": 25, "incentives": 6000, "salary": 70000,
#       "is_perm": True,"curr_location": "chennai", "client_location": "bangalore"}

"range"
"""
range(n)    -> range(0, n) :: start -> 0, last_val -> n-1, stop: n -> steps: +1 -> num of val: stop -start -> n - 0 = n
range(m, n) -> start:: m, stop:: n, last_val -> n-1, steps: +1, -> num of vals -> n-m
range(p, q, r) -> start: p, stop:q, step:r
"""
# rg = range(-3, -9, -1)
# print(rg, type(rg))
# print(rg)
#
# for each in rg:
#     print(each)

# rg = range(5, 20)
# "5 6 7 8 9 10 11 12 13 14 15 16 17 18 19"
# "0 1 2 3 4 5   6 7   8  9 10 11 12 13 14"
#
# print(rg[12])