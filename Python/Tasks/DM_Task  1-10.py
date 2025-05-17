"""
1. Check if a Rectangle is a Square
•	Task: Take the length and breadth of a rectangle as input from the user and find whether it is a square or not.
"""
from itertools import count

# length = int(input("enter Length"))
# breadth = int(input("enter breadth"))
#
# if length == breadth :
#     print("Its a square")
# else :
#     print("It is not a square")


'''
2. Check Case of Entered Character
•	Task: Take a single Character as input from the user and find whether it is uppercase or lowercase.

'''


# Char = input("enter a single Character")
#
# if len(Char) <= 1:
#     print("enter only one Char")
# elif Char == Char.lower():
#     print("its a lower case")
# elif Char == Char.upper():
#     print("its a upper case")
# else:
#     print("its not a  upper case / Lower case")


'''



3. Check if Number is Positive or Negative
•	Task: Take a Number as input from the user and find whether it is positive or negative.

'''

#
# Number = int(input("Enter a Valid Number"))
#
# if Number < 0 :
#     print("Its a Negative value")
# elif Number > 0 :
#     print("Its a Positive value")
# else:
#     print("Its a Zero Please Enter Positive/Negative Values")



'''
4. Floating Point Number Classification
•	Task: Take a floating-point Number as input from the user and
 find whether it is zero, positive, or negative. 
 Also determine if it is small (absolute value < 1) or large (absolute value > 1,000,000).


'''



# Number = float(input("Enter a Valid Number: "))
#
# if Number < 0 :
#     print("Its a Negative value")
# elif Number > 0 :
#     print("Its a Positive value")
# else:
#     print("Its a Zero Please Enter Positive/Negative Values")



'''
5.Weekday from Number
•	Task: Take a Number between 1 to 7 as input from the user and find the corresponding weekday name.


'''


# Number = int(input("Enter a Valid Number: "))
#
# match Number :
#     case 1 :
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3 :
#         print("Wednesday")
#     case 4:
#         print("Thursday")
#     case 5:
#         print("Friday")
#     case 6:
#      print("Saturday")
#     case 7:
#      print("Sunday")
#     case _ :
#         print("Enter valid day")
#
# Number = int(input("Enter a valid Number: "))
# #
# if 1 <= Number <= 7 :
# if Number == 1:
#     print("Monday")
# elif Number == 2:
#     print("Tuesday")
# elif Number == 3:
#     print("Wednesday")
# elif Number == 4:
#     print("Thursday")
# elif Number == 5:
#     print("Friday")
# elif Number == 6:
#     print("Saturday")
# else :
#     print("Sunday")
#else :
#     print("enter valid day")



'''
6.Vowel or Consonant Checker
•	Task: Take a single alphabet Character as input from the user and find whether it is a vowel or consonant.


'''


# Char = input("enter a single Character : ")
#
# if len(Char) > 1 > len(Char):
#     print("enter only one Char")
# elif Char in ["a","e","i","o","u","A","E","I","O","U"]:
#     print("Its a Vowel")
# else:
#     print("Its Constant")
#

'''
7. Cube Display up to a Given Number
    •	Task: Take an integer as input from the user and find the cube of all Numbers up to that integer.
'''



# Number = int(input("Enter a Valid Number: "))
#
#
# if Number <= 1 :
#     print("Please enter a valid Number")
# else:
#     for each in range(1,Number+1):
#         print(each*each*each)

'''
8. Sum of N Odd Natural Numbers
•	Task: Take a Number n as input from the user and find the sum of first n odd natural Numbers.
'''
# Number = int(input("enter a valid Number: "))
#
# if Number <= 1 :
#     print("Please enter a valid Number")
# else:
#
#     Odd_Number = []
#     for each in range(1,Number+1):
#         value = 2 * each - 1
#         if value <= Number:
#             Odd_Number.append(value)
#     sumOfOdd = len(Odd_Number) ** 2
#     print("Sum of odd Number is ", int(sumOfOdd))


'''
9. Order of Three Numbers
•	Task: Take three Numbers as input from the user and
 find whether they are in increasing, decreasing, or neither order.
'''
# First_Number = int(input("Enter valid First Number : "))
# Second_Number = int(input("Enter valid Second Number : "))
# Third_Number = int(input("Enter valid Third Number : "))
#
# if [First_Number, Second_Number, Third_Number] == [0, 0, 0]:
#     print("Please enter proper (non-zero) values.")
# elif First_Number <= Second_Number <= Third_Number:
#     print("They are in increasing")
# elif First_Number >= Second_Number  >= Third_Number:
#     print("They are in decreasing")
# else :
#     print("They are in neither order")




'''
10. Descending Order of Names
•	Task: Take three names as input from the user and find their order in descending alphabetical order.
'''

# First_Name = input("Enter valid First Name : ")
# Second_Name = input("Enter valid Second Name : ")
# Third_Name = input("Enter valid Third Name : ")
#
# Names_order = [First_Name,Second_Name,Third_Name]
# Names_order.sort(reverse=True)
# print(Names_order)

