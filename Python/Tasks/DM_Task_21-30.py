'''
21. IP Address Validator
•	Task: Take a string as input from the user and find whether it is a valid IP address or not.
'''
from itertools import count
from numbers import Number
from operator import index

#IP_Address = input("Enter Valid IP_Address: ")


'''
22. Average of N Numbers
•	Task: Take N numbers as input from the user and find their average.

'''

# Number = input("Enter N NUmber : ")
# Total = 0
# elements = 0
# for i in Number.split(",") :
#     Total += int(i)
#     elements += 1
#
# print("Avg of their ",float (Total//elements))

'''

23. Power of Two Checker
•	Task: Take a number as input from the user and find whether it is a power of two or not.
'''


# Number = int(input("Enter Number: "))
# Power = 1
#
# for i in range(1, Number + 1):
#     if Power == Number:
#         print(Number,"is a power of 2.")
#         break
#     Power *= 2
# else:
#     print(Number, "is NOT a power of 2.")


'''
24. Compound Interest Calculator
•	Task: Take principal, rate, and time as input from the user and find the compound interest.
'''


# Principle = float(input("Enter Principal : "))
# Rate = float(input("Enter Rate : "))
# Time = float(input("Enter Time : "))
# Rate = Rate/100
#
# Compound_Interest = Principle * (1 + Rate)**Time
# print("compound interest is  : ",Compound_Interest-Principle)


'''
25. Reverse a Number
•	Task: Take a number as input from the user and find its reverse.
'''
# Number = input("Enter Number : ")
# reverse = ""
#
# for each in Number :
#     reverse = each + reverse
# print(reverse)


'''
26. Strong Number Checker
•	Task: Take a number as input from the user and find whether it is a strong number or not.
'''

# Number = input("Enter a Number : ")
# list = []
# for each in Number:
#     factorial = 1
#     for i in range(1,int(each)+1):
#         factorial *= i
#     list.append(factorial)
#
# if sum(list) == int(Number) :

#     print("Given Number",Number," is Strong Number")
# else:
#     print("Given Number" ,Number," is Not a Strong Number")


'''

27. Simple Interest Calculator
•	Task: Take principal, rate, and time as input from the user and find the simple interest.
'''

# Principle = float(input("Enter Principal : "))
# Rate = float(input("Enter Rate : "))
# Time = float(input("Enter Time : "))
#
# Simple_Interest = (Principle * Rate * Time ) % 100
# print("Simple interest is  : ",Simple_Interest)

'''
28. Simple Calculator
•	Task: Take two numbers and an operator as input from the user and
 perform the corresponding arithmetic operation.
'''

# First_Number = int(input("Enter First_NUmber"))
# Second_Number = int(input("Enter Second_Number"))
# Operator_type = input("Enter Operator_type")
#
# if Operator_type == "+" :
#     print(" Sum of 2 Given numbers is " , First_Number + Second_Number)
# elif Operator_type == "-" :
#     print(" Sub of 2 Given numbers is " , First_Number - Second_Number)
# elif Operator_type == "*" :
#     print(" Multiplication of 2 Given numbers is " , First_Number * Second_Number)
# elif Operator_type == "%" :
#     print(" Modulos of 2 Given numbers is " , First_Number % Second_Number)
# elif Operator_type == "/" :
#     print(" Division of 2 Given numbers is " , First_Number / Second_Number)
# elif Operator_type == "//" :
#     print(" Floor Division of 2 Given numbers is " , First_Number // Second_Number)
# else:
#     print("enter Valid Operator ")

'''

29. Perfect Square Checker
•	Task: Take a number as input from the user and find whether it is a perfect square or not.

'''



'''
30. Smallest of Three Numbers
•	Task: Take three numbers as input from the user and find the smallest number.


'''




# num = 4
# l1 = [6,1,2,4,5,6,4,7,2,8,5,4]
#
#
# if len(l1) == 0 or num not in l1 :
#     print("[-1,-1]")
# elif num in l1:
#     l1.count(num)
#     if l1.count(num) == 1:
#         print("Prest [",l1.index(num),l1.index(num),"]")
#     elif l1.count(num) == 2:
#         if num in range(l1.index(num) ,len(l1)) :
#             l11 = l1.index(num)
#             l12 = l1.index(num,l11+1)
#             print("[",l11,l12, "]")
#     else:
#         first_index = l1.index(num)
#         # Finding the last occurrence without using [::-1]
#         last_index = len(l1) - 1
#         while l1[last_index] != num:
#             last_index -= 1
#         print("[", first_index, last_index, "]")
#
#


