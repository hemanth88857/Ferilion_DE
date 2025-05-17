'''

1.	Print numbers from 1 to 10 using a for loop

'''
from itertools import count

# for each in range(11):
#     print(each)


'''
2.	Calculate the sum of numbers from 1 to 10 using a for loop

'''
# Value = 0
# for each in range(11):
#     Value += each
# print(Value)



'''

3.	Print the elements of a list using a for loop

'''
# first_names = ['Ava', 'Liam', 'Sophia', 'Noah', 'Mia', 'Elijah', 'Isabella', 'James', 'Harper', 'Lucas']
#
# for each in first_names:
#     print(each)


'''
4.	Calculate the product of elements in a list using a for loop

'''
# product = [3, 7, 1, 10, 6]
# Value  = 1
#
#
# for each in product:
#     Value *= each
#
# print(Value)



'''

5.	Print characters of a string using a for loop

'''
# Name  = "Hemanth"
#
# for each in Name:
#     print(each)

'''

6.	Find the largest number in a list using a for loop


'''
# product = [3, 7, 1, 10, 6]
# Value = product[0]
#
# for each in product:
#     if Value <= each :
#         Value = each
#
# print(Value)

'''

7.	Find the average of numbers in a list using a for loop
'''
# product = [3, 7, 1, 10, 6]
# Value  = 0
# print(len(product))
# for each in product:
#     Value += each
#
# print(Value/len(product))

'''




8.	Calculate factorial of a number using a while loop
'''

# Number = int(input("Enter a valid Number : "))
# Value = 1
#
# while Number > 0 :
#     Value *= Number
#     Number += -1
#
# print(Value)


'''

9.	Find the first occurrence of a number in a list using a while loop

'''

product = [3, 7, 1, 10, 6]
#
# while True:
#     print(product[0])
#     break

'''
10.	Find the common elements in two lists using a for loop

'''
# list1 = [3, 7, 1, 10, 6]
# list2 = [5, 7, 3, 2, 4]
# commonElements = []
#
# for each in list1:
#     if each in list2:
#         commonElements.append(each)
# print(commonElements)
'''
11.	Write a program to display the sum of n terms of even natural numbers

'''
# Number  = int(input("enter a valid number : "))
# value = 0
# for each in range(0,Number+1):
#     if each % 2 == 0 :
#         value += each
# print(value)


'''

12.	Write a program to find the Armstrong number for a given range of number


'''
# Number  = input("enter a valid number : ")
# value = 0
#
# for each in Number:
#     values = int(each)
#     for i in range(1,len(Number)):
#         values *= int(each)
#     value += values
#
# if value == int(Number) :
#     print("Given Number is ARMStrong",value,Number)
# else :
#     print("Given Number is not a ARMStrong",value)

'''



13.	Write a program in to convert a decimal number into binary without using a list
14.	Find the number of occurrences of a character in a String

'''

# text = "PythonnP"
# printed = set()
#
# for char in text:
#     if char not in printed:
#         print(char, text.count(char))
#         printed.add(char)


'''
15.	How to find out if the given two strings are anagrams or not?
'''
# Value1 = input("Enter any name as Value1: ").lower()
# Value2 = input("Enter any name as Value2: ").lower()
#
# if len(Value1) != len(Value2):
#     print("Given strings are Not Anagrams")
# else:
#     freq1 = {}
#     freq2 = {}
#
#     for char in Value1:
#         freq1[char] = freq1.get(char, 0) + 1
#
#     for char in Value2:
#         freq2[char] = freq2.get(char, 0) + 1
#
#     if freq1 == freq2:
#         print("Given strings are Anagrams")
#     else:
#         print("Given strings are Not Anagrams")


'''


16.	How do you remove all occurrences of a given character from the input string
'''
# Value1 = input("Enter any name as Value1: ").lower()
# Char = input("Enter any character: ").lower()
#
# if Char  in Value1 :
#     Value1 =   Value1.replace(Char,"")
#
# print(Value1)



'''



17.	Write a program using while loops to print the first 10 rows of Pascal's Triangle.
18.	Create a program to find the Greatest Common Divisor (GCD) and Least Common Multiple (LCM) of two numbers using a while loop.
19.	Implement a program using a while loop to generate and print the Collatz sequence for a given starting number.
20.	Create a program to find and print the first 5 pairs of consecutive prime numbers using a while loop.
21.	Write a program to transpose a given matrix using a while loop
22.	Implement a program using while loops to print a palindromic pyramid pattern
     1
   121
  12321
 1234321
123454321
23.	Create a program using for loops to generate a 3x3 magic square (a square in which the sums of the numbers in each row, column, and both main diagonals are the same).
24.	Create a program using for loops to print a square matrix in spiral order
1     2   3   4
12 13 14   5
11 16 15   6
10  9    8    7
25.	Write a program using nested for loops to print a triangle of prime numbers
   2
  357
 111317
26.	Implement a program using nested for loops to print a diamond pattern
     1
   212
  32123
 4321234
  32123
   212
    1

27.	Calendar Generator:
Build a program that generates a monthly calendar for a specified year and month. Use loops to iterate through the days of the week and the days of the month. Allow the user to input the year and month.
28.	Simple Inventory System:
Build a basic inventory management system where users can add, remove, and view items in their inventory. Utilize loops to handle user interactions and keep the program running until the user decides to exit.
29.	To-Do List Manager: Implement a simple to-do list manager where users can add, remove, and mark tasks as completed. Utilize loops to repeatedly present the menu and handle user interactions until they choose to exit.
30.	Pattern Recognition in Text: Develop a program that takes a text input and identifies patterns such as repeated words, palindromes, or specific sequences. Use loops to analyze the text and provide relevant information.



'''