# 1,Length of string
# name = "Python"
# print(len(name))

# 2,Count characters in string
# name = "Python"
# name1  = name.count("")
# print(name1)

# 3,String slicing
# b = "Hello, World!"
# print(b[0:4])

# 4,Replace first occurance character
# name = "ramesh"
# x = name.replace("ramesh","ganesh")
# print(x)

# 5,Swapping chars in string
# a = "Apple"
# b = "Banana"
# a,b = b,a
# print(a)
# print(b)

# 6,Append chars to string at end
# string1 = "python"
# string2 = " World"
# result = string1 + string2
# print(result)

# 7,Substring replacement
# str = "Hello World"
# str1 = str.replace("World", "Python")
# print(str1)

# 8,Length of longest string in python
# words = ["apple", "banana", "cherry", "dragonfruit"]
# longest_length = len(max(words))
# print("Length of longest string:", longest_length) # dragonfruit(11)

# 9,nth index character from string
# str = "Hello, World!"
# n = 7
# print("Character at index", n, "is:", str[n])

# 10,First last chars swapping
# str = "python"
# if len(str) > 1:
#     swapped = str[-1] + str[1:-1] + str[0]
# else:
#     swapped = str  #
# print("After swapping:", swapped)
#text[-1] -> last char
#text[1:-1]-> middle part of the string(Excluding first and last)
#text[0] -> First char

# 11,Remove odd index values
# str = "Pythonworld"
# print(str[::2])
#or
# str = "Pythonworld"
# str1 = " "
# for i in range(len(str)):
#     if i % 2 == 0:
#      str1 += str[i]
# print(str1)


# 12,Count words in a string
# str = "Hello world, it is easy to learn"
# str1 = str.split()
# words = len(str1)
# print(words)

# 13,Upper lower case of a string
# str = "Hello world, it is easy to learn"
# str1 = str.upper()
# print(str1)

# 14,Sort unique words alphanumerically
# s = input("Enter a string: ")
# words = s.split()
# unique_words = set(words)
# sorted_words = sorted(unique_words)
# print("Sorted unique words:")
# for word in sorted_words:
#     print(word)

# 15,Create html from string
# html_content = """
# <html>
# <head>
#     <title>My HTML Page</title>
# </head>
# <body>
#     <h1>Hello, World!</h1>
#     <p>This is a paragraph generated from Python.</p>
# </body>
# </html>
# """
#
# # Write the string into an HTML file
# with open("output.html", "w") as file:
#     file.write(html_content)
#
# print("HTML file created successfully!")

# 16,Insert string in middle of special chars
# special = "****"
# insert = "hello"
# mid = len(special)//2
# result = special[:mid] + insert + special[mid:] # We are expecting output of string format
# print(result)

# 17,4 Copies of last 2 chars
# s = input("Enter a string: ")
# if len(s) >= 2:
#     result = s[-2:] * 4
#     print("Result:", result)
# else:
#     print("String must have at least 2 characters.")

# 18,Length of first 3 chars
# s = input("Enter a string: ")
# first_three = s[:3]
# print(first_three)
# print(len(first_three))
# print("First 3 characters:", first_three)
# print("Length of first 3 characters:", len(first_three))

# 19,Last part of string
# s = input("Enter a string: ")
# last_part = s[-3:]
# print(last_part)

# 20,reverses a string if it's length is a multiple of 4
# s = input("Enter a string: ")
# if len(s) % 4 == 0:
#     reversed_str = s[::-1]
#     print("Reversed string:", reversed_str)
# else:
#     print("Length is not a multiple of 4. Original string:", s)

# Convert a given string to all uppercase
# program to sort a string lexicographically
# program to remove a newline in Python
# program to check whether a string starts with specified characters
# program to create a Caesar encryption
# display formatted text (width=50) as output
# remove existing indentation from all of the lines in a given text
# to add a prefix text to all of the lines in a string
# to set the indentation of the first line
# to print the following floating numbers upto 2 decimal places
# print the following floating numbers upto 2 decimal places with a sign
# print the following floating numbers with no decimal places
# print the following integers with zeros on the left of specified width
# print the following integers with '*' on the right of specified width
# to display a number with a comma separator
# to format a number with a percentage
# to display a number in left, right and center aligned of width 10
# to count occurrences of a substring in a string
# reverse a string
# reverse words in a string
# strip a set of characters from a string
# count repeated characters in a string
#  square and cube symbol in the area of a rectangle and volume of a cylinder
# print the index of the character in a string
# check if a string contains all letters of the alphabet
# convert a string in a list
# lowercase first n characters in a string
# swap comma and dot in a string
# count and display the vowels of a given text
# split a string on the last occurrence of the delimiter
# find the first non-repeating character in given string
# print all permutations with given repetition number of given string
# find the first repeated character in a given string
# find the first repeated character of a given string where the index of first occurrence is smallest
# find the first repeated word in a given string
# find the second most repeated word in a given string
# remove spaces from a given string
# move spaces to the front of a given string
#  find the maximum occurring character in a given string
# capitalize first and last letters of each word of a given string
# remove duplicate characters of a given string
# compute sum of digits of a given string
# remove leading zeros from an IP address
# Reverse a given string  Input : "Python"   Output : "nohtyP"
# Reverse each word in given string Input
# Reverse each word and reverse word again. Input
# that accepts a string and calculate the number of digits and letters

