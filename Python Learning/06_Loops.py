'''1.	Print numbers from 1 to 10 using a for loop'''
# x = 10
# for each in range(x):
#     print(each)

# '''2.	Calculate the sum of numbers from 1 to 10 using a for loop'''
# num = 10
# sum = 0
# for i in range(num+1):
#     sum += i
# print(sum)

''' 3.	Print the elements of a list using a for loop'''
# list = [2,"python",3,4,"pavan",6,(4,6),9]
# # print(list[4])
# for each in list:
#     print(each)


# 4.	Calculate the product of elements in a list using a for loop
# list = [2,4,5,6]
# res = 1
# for val in list:
#     res *=val
# print(res)

# 5.	Print characters of a string using a for loop
# str = "python world"
# for each in str:
#     print(each, end = '')

# 6.	Find the largest number in a list using a for loop
# list = [2,5,6,67,69,55,44]
# large = list[0]
# for each in list:
#     if each > large:
#         large = each
# print(large)

# 7.	Find the average of numbers in a list using a for loop
# list = [2,5,6,67,69,55,44]
# sum = 0
# count = 0
# for each in list:
#     sum = sum+each
#     count= count+1
# print(sum/count)

# 8.	Calculate factorial of a number using a while loop
# num = 5
# fact = 1
# while num>0:
#     fact *= num
#     num = num-1
# print(fact)

# 9.	Find the first occurrence of a number in a list using a while loop
# numbers = [5, 8, 12, 8, 20]
# target = 8
# i = 0
# while i < len(numbers):
#     if numbers[i] == target:
#         print("First occurrence of is {target} at index {i}")
#         break
#     i += 1
# else:
#     print("It is not found in the list.")

# 10.	Find the common elements in two lists using a for loop
# lst1 = [2,5,7,9,4,5,4,6]
# lst2 = [4,2,5,7,6,8,7,9]
#
# common = []
# for item in lst1:
#     if item in lst2 and item not in common:
#         common.append(item)
# print("Common elements:", common)


# 11.	Write a program to display the sum of n terms of even natural numbers
# n = int(input("Enter the number of even natural numbers to sum: "))
# sum_even = 0
# count = 1
# even_num = 2
# while count <= n:
#     sum_even += even_num
#     even_num += 2
#     count += 1
# print(f"The sum of the first {n} even natural numbers is: {sum_even}")

# 12.	Write a program to find the Armstrong number for a given range of number
# num = int(input("Enter a number: "))
# sum = 0
# temp = num
# while temp > 0:
#    digit = temp % 10
#    sum += digit ** 3
#    temp //= 10
# if num == sum:
#    print(num,"is an Armstrong number")
# else:
#    print(num,"is not an Armstrong number")

# 13.	Write a program in to convert a decimal number into binary without using a list
# n = int(input("Enter a decimal number: "))
# #n = 7  # decimal number
# res = ''  # binary result
#
# while n > 0:
#     res = str(n % 2) + res
#     n //= 2
# print(res)

# 14.	Find the number of occurrences of a character in a String
# string = input("Enter a string: ")
# char = input("Enter the character to count: ")
# count = string.count(char)
##print(count)
# print(f"The character '{char}' occurs {count} times in the string.")

# 15.	How to find out if the given two strings are anagrams or not?
# str1 = input("Enter a string: ")
# str2 = input("Enter a string: ")
# str1 = str1.lower()
# str2 = str2.lower()
# if(len(str1) == len(str2)):
#     sorted_str1 = sorted(str1)
#     sorted_str2 = sorted(str2)
#     if(sorted_str1 == sorted_str2):
#         print(str1 + " and " + str2 + " are anagram.")
#     else:
#         print(str1 + " and " + str2 + " are not anagram.")
# else:
#     print(str1 + " and " + str2 + " are not anagram.")
#or
# word1 = input("Enter first word: ").lower()
# word2 = input("Enter second word: ").lower()
# if len(word1) != len(word2):
#     print("Not Anagrams")
# else:
#     # Convert to lists and sort manually (without using sort or sorted)
#     count1 = [0] * 26
#     count2 = [0] * 26
#     print(count1,count2)
#     i = 0
#     while i < len(word1):
#         count1[ord(word1[i]) - ord('a')] += 1
#         count2[ord(word2[i]) - ord('a')] += 1
#         print(count1,count2)
#         i += 1
#
#     if count1 == count2:
#         print("Anagram Words")
#     else:
#         print("Not Anagram Words")
#
# 16.	How do you remove all occurrences of a given character from the input string
# input_str = input("Enter a string: ")
# result = ""
# for ch in input_str:
#     if input_str.count(ch) == 1:
#         result += ch
# print("String after removing all repeated characters:", result)
#or

# input_string = input("Enter a string: ")
# char_to_remove = input("Enter the character to remove: ")
# result = ""
# for ch in input_string:
#     if ch != char_to_remove:
#         result += ch
# print("Resulting string:", result)
#or
# input_string = input("Enter a string: ")
#
# if input_string:  # make sure it's not empty
#     char_to_remove  = input_string[0]
#     result = ""
#
#     for ch in input_string:
#         if ch != char_to_remove:
#         #if ch != char_to_remove.count(ch) == 1: not working
#             result += ch
#
#     print("Original string:", input_string)
#     print("Character removed:", char_to_remove)
#     print("Resulting string:", result)
# else:
#     print("You entered an empty string.")

# 17.	Write a program using while loops to print the first 10 rows of Pascal's Triangle.
# rows = 10
# i = 0
# while i < rows:
#     # Print leading spaces for triangle shape
#     print(" " * (rows - i), end="")
#     j = 0
#     num = 1
#     while j <= i:
#         print(num, end=" ")
#         # Update num using in-place formula for binomial coefficient
#         num = num * (i - j) // (j + 1)
#         j += 1
#     print()  # Move to next line
#     i += 1

# 18.	Create a program to find the Greatest Common Divisor (GCD) and Least Common Multiple (LCM) of two numbers using a while loop.
# 19.	Implement a program using a while loop to generate and print the Collatz sequence for a given starting number.
# n = int(input("Enter a number: "))
# while n != 1:
#         print(n, end=' ')
#         # If n is odd
#         if n & 1:
#             n = 3 * n + 1
#         # If even
#         else:
#             n = n // 2
# print(n)
# or
# n = int(input("Enter a positive integer: "))
#
# while n != 1:
#     print(n, end=' ')
#     if n % 2 == 0:
#         n = n // 2
#     else:
#         n = 3 * n + 1
#
# print(n)

# 20.	Create a program to find and print the first 5 pairs of consecutive prime numbers using a while loop.
# count = 0
# num = 2
# prev_prime = None
# while count < 5:
#     is_prime = True
#     for i in range(2, num):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         if prev_prime is not None and num - prev_prime == 2:
#             print(prev_prime, num)
#             count += 1
#         prev_prime = num
#     num += 1

# 21.	Write a program to transpose a given matrix using a while loop
# matrix = [           # Original 2x3 matrix
#     [1, 2, 3],
#     [4, 5, 6]
# ]
# transpose = [[], [], []] # Initialize the transposed matrix (3x2)
#
# i = 0
# while i < 3:  # number of columns in original matrix
#     j = 0
#     while j < 2:  # number of rows in original matrix
#         transpose[i].append(matrix[j][i])
#         j += 1
#     i += 1
#
# k = 0             # Print the transposed matrix
# while k < 3:
#     print(transpose[k])
#     k += 1

# 22.	Implement a program using while loops to print a palindromic pyramid pattern
#      1
#    121
#   12321
#  1234321
# 123454321
# 23.	Create a program using for loops to generate a 3x3 magic square (a square in which the sums of the numbers in each row, column, and both main diagonals are the same).
# 24.	Create a program using for loops to print a square matrix in spiral order
# 1     2   3   4
# 12 13 14   5
# 11 16 15   6
# 10  9    8    7
# 25.	Write a program using nested for loops to print a triangle of prime numbers
#    2
#   357
#  111317
# 26.	Implement a program using nested for loops to print a diamond pattern
#      1
#    212
#   32123
#  4321234
#   32123
#    212
#     1
#
# 27.	Calendar Generator:
# Build a program that generates a monthly calendar for a specified year and month. Use loops to iterate through the days of the week and the days of the month. Allow the user to input the year and month.
# 28.	Simple Inventory System:
# Build a basic inventory management system where users can add, remove, and view items in their inventory. Utilize loops to handle user interactions and keep the program running until the user decides to exit.
# 29.	To-Do List Manager: Implement a simple to-do list manager where users can add, remove, and mark tasks as completed. Utilize loops to repeatedly present the menu and handle user interactions until they choose to exit.
# 30.	Pattern Recognition in Text: Develop a program that takes a text input and identifies patterns such as repeated words, palindromes, or specific sequences. Use loops to analyze the text and provide relevant information.
#

#Palindrome
# num = int(input("Enter a number: "))  # Take user input
# original = num                        # Store original number
# reverse = 0                           # Variable to store reversed number
#
# while num > 0:
#     digit = num % 10                  # Get last digit
#     reverse = reverse * 10 + digit    # Append digit to reverse
#     num = num // 10                   # Remove last digit
#
# if original == reverse:
#     print("Palindrome Number")
# else:
#     print("Not a Palindrome")

#or
# value = input("Enter a number or string: ")
# if value == value[::-1]:
#     print("Palindrome")
# else:
#     print("Not a palindrome")

#strong numbers
# num = int(input("Enter a number: "))
# temp = num
# sum = 0
# while temp > 0:
#     digit = temp % 10
#     fact = 1
#     for i in range(1, digit + 1):
#         fact *= i
#     sum += fact
#     temp //= 10
# if sum == num:
#     print("Strong number")
# else:
#     print("Not a strong number")

#ARM strong  number
# num = int(input("Enter a number: "))
# temp = num
# sum = 0
# while temp > 0:
#     digit = temp % 10
#     sum += digit ** len(str(num))
#     temp //= 10
# if sum == num:
#     print("Armstrong number")
# else:
#     print("Not an Armstrong number")



