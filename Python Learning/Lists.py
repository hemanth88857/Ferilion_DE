"""
Author : GOVIND
Date   : 17-04-2025
"""
"""
req:
----
state   : dt/ds input output
behavior : BL - CRUD - DM LOOPS OPERATORS

mutable   : list set dict (CRUD)
immutable : int float complex bool None str tuple (CRD)

iterables : str list tuple set dict range
sequence  : str list tuple range
unordered : set

operators:
-----------
AC L MA IB

DM
---
if elif else

loops
-----
for 
while


for
---
str list tuple set dict range
[] ()

control statements
-------------------
break continue pass

while
------
conditional based iteration
unknown iteration count

conditional based iteration

while condition:
    execute this block of code repeatedly
    condition false

unknown iteration count

while True:
    condition
        break
"""

# s = "python"
# s = ["ramesh", "suresh", "ganesh", "harish", "mahesh", "rakesh", "rajesh"]
# s = {"ramesh", "suresh", "ganesh", "harish", "mahesh", "rakesh", "rajesh"}
# s = {"name": "ramesh", "age": 25, "salary": 25563, "location": "Bangalore"}
# s = range(5, 10)
# for each in s:
#     print(each)

# print("******", each)

"""
each = ramesh
each = suresh
each = ganesh
each = harish
each = mahesh
each = rakesh
each = rajesh

"""
# each = "ramesh"
# each = "suresh"
# each = "ganesh"
# each = "harish"
# each = "mahesh"
# each = "rakesh"
# each = "rajesh"
# print(each)


s = ["ramesh", "suresh", "ganesh", "harish", "mahesh", "rakesh", "rajesh"]

# for each in s:
#     print("give 500 rupees to", each)

# loop_count = 0
# for each in s:
#     loop_count += 1
#     print("give 500 rupees to", each) # task / action part
#     if each == 'harish':
#         print("give 500 rupees to", each)  # task / action part
#         break
#     print("give 500 rupees to", each) # task/action part
#
# print(loop_count)

# for each in s:
#     print("give 500 rupees to", each)  # task/action part
#     if each == "harish":
#      print("give 500 rupees to", each)  # task/action part
#     continue
#print("give 500 rupees to", each)  # task/action part

# for each in s:
#     pass
# print(5 + 5)

# x = 1
# count = 0
# while x == 1:
#     count+=1
#     print(count)
#     x+=1

"factorial"

# num = int(input("enter the num: "))
# res = 1
#
# while num > 1:
#     # res = res * num
#     # num = num - 1
#     res *= num
#     num -= 1
# print(res)

"""
first loop  : num = 5, res = 1  → res = 1 * 5 = 5,  num = 5 - 1 = 4
second loop : num = 4, res = 5  → res = 5 * 4 = 20, num = 4 - 1 = 3
third loop  : num = 3, res = 20 → res = 20 * 3 = 60, num = 3 - 1 = 2
fourth loop : num = 2, res = 60 → res = 60 * 2 = 120, num = 2 - 1 = 1
fifth loop  : num = 1, res = 120 - xxxxxxx



"""

# secret_num = 3
#
# while True:
#     guess = int(input("predict the secret number 0-9: "))
#     if guess == secret_num:
#         print("congratulations")
#         break
#     print("try again!")

"nested loops"

"hello"

# for _ in range(7):
#     print("hello", end=' :: ')

# s = ["ramesh", "suresh", "ganesh", "harish", "mahesh", "rakesh", "rajesh"]
#
# for each in s:
#     if each == "mahesh":
#         print("yes he is present")
#         break
# else:
#     print("no he is not present")


# nums = [1, 2, 3, 4]
# fruits = ["apple", "cherry", "grapes", "mangoes"]
# cities = ["chennai", "pune", "delhi", "goa"]
#
# for num in nums:
#     print(num)
#     for fruit in fruits:
#         print("    ", fruit)
#         for city in cities:
#             print("        ", city)