# import logging

# import logger_config  # Ensures logger is configured


# logger = logging.getLogger(__name__)
#
# def process1():
#     logger.info("This is a log from module 1 filter")
#
#
# process1()

"""find even and  odd"""

# val = [1,34,54,6,7,88,4,6,46,6,43,3,35,5,66,7,]
#
#
# even = list(filter(lambda x:x%2==0,val))
# odd = list(filter(lambda x:x%2 != 0 ,val))
#
# print(even)
# print(odd)
#
"2. Filter Strings Starting with a Specific Letter a "
#
# words = ['Apple', 'Banana', 'Avocado', 'Cherry']
#
# word = list(filter(lambda x:x.endswith("y"),words))
#
# print(word)

"""3. Filter Positive Numbers """

# numbers = [-10, 0, 5, -3, 8]
#
# num = list(filter(lambda x:x>0,numbers))
# print(num)


"""4. Filter Palindromic Strings """

# words = ['radar', 'hello', 'level', 'world']
#
# palin = list(filter(lambda x:x == x[::-1] ,words ))
# print(palin)
#


"""5. Filter Prime Numbers """

# def is_prime(num):
#     if num < 2:
#         return False
#     for each in range(2,int(num**0.5)+1):
#         if num%each == 0:
#             return False
#     return True
#
#
# print(is_prime(2))
#
#
# number = 10
#
#
#
# def pirme_numbers(num):
#     numr = []
#     for each in range(2,num):
#
#         for i in range(2,int(each**0.5)+1):
#
#             if each%i == 0 :
#                 break
#         else:
#             numr.append(each)
#     return numr
#
# print(pirme_numbers(10))
# print(pirme_numbers(20))
#
#
# nu = 10
# prime_numbers = list(filter(
#     lambda x: x > 1 and len([i for i in range(2, x) if x % i == 0]) == 0,
#     range(2, nu+1)
# ))
#
# print(prime_numbers)

"""
6. Filter Strings of a Certain Length
Task: From a list of strings, filter out those with more than 5 characters.

"""

# words = ['apple', 'banana', 'cherry', 'date']
#
# word = list(filter(lambda x:len(x)>=5,words ))
# print(word)

"""
7. Filter Non-Empty Strings
Task: Given a list of strings, use filter() to remove all empty strings.
"""

# strings = ['hello', '', 'world', '', 'python']
#
# new = list(filter(lambda x:len(x)>=1 , strings))
# print(new)


"""
8. Filter Numbers Divisible by Both 2 and 3
Task: From a list of integers, filter out numbers divisible by both 2 and 3.

"""

# numbers = [6, 12, 15, 18, 20, 24]
#
# num = list(filter(lambda x:(x%2==0) and (x%3==0),numbers))
#
# print(num)


"""
9. Filter Vowels from a String
Task: Given a string, use filter() to extract all vowels
"""

# text = 'Hello World'
# vowels = list(filter(lambda x:x in "aeiou",text.lower()))
# print(vowels)


"""
10. Filter Unique Elements
Task: From a list with duplicate elements, use filter() to extract unique elements.

"""
# numbers = [1, 2, 2, 3, 4, 4, 5]
#
# num = list(filter(lambda x:numbers.count(x)==1,numbers))
# print(num)
#


"""
11. Filter Negative Numbers
Task: Given a list of numbers, use filter() to extract all negative numbers.
"""

# numbers = [10, -5, 0, -2, 8, -1]
#
# num = list(filter(lambda x:x<0,numbers))
# print(num)

"""
12. Filter Out Non-Integer Values
Task: Given a list containing integers and other data types, use filter() to extract only the integer values.
"""

# items = [1, 'a', 3.5, 2, 'b', 4]
# num = list(filter(lambda x: isinstance(x,int),items))
# print(num)


"""
5. Filter Strings Containing a Specific Substring
Task: Given a list of strings, use filter() to extract those that contain the substring 'py'.
"""

# words = ['python', 'java', 'pycharm', 'javascripy']

# num = list(filter(lambda x:x.__contains__("py"),words))
# num = list(filter(lambda x:'py' in x,words))
# print(num)


"""
6. Filter Palindromic Numbers
Task: From a list of integers, use filter() to extract palindromic numbers (numbers that read the same backward).
"""

# numbers = [121, 131, 20, 33, 45]
# num = list(filter(lambda x:str(x) == str(x)[::-1],numbers))
# print(num)


"""
8. Filter Numbers Within a Range
Task: From a list of numbers, use filter() to extract those between 10 and 20 (inclusive).
"""

# numbers = [5, 10, 15, 20, 25]
# num = list(filter(lambda x:10 <=x<=20,numbers))
# print(num)

"""
9. Filter Strings That Are Digits
Task: Given a list of strings, use filter() to extract those that represent digits.
"""

# strings = ['123', 'abc', '456', '78a', '90']
#
# num = list(filter(lambda x:x.isdigit(),strings))
# print(num)



"""
1. Filter Dictionary by Value Threshold
Task: Given a dictionary of items and their prices, filter out items with prices above ₹20,000.
"""


# products = {
#     "Laptop": 50000,
#     "Phone": 30000,
#     "Headphones": 2000,
#     "Keyboard": 1500,
#     "Mouse": 800
# }
#
# # num = list(filter(lambda x:x >=20000,products.values()))
# num = {k:v for k,v in products.items() if v>= 20000}
# print(num)



"""
2. Filter Dictionary by Key Prefix
Task: From a dictionary of student names and their scores, filter out students whose names start with 'A'.
"""

# scores = {
#     "Alice": 85,
#     "Bob": 90,
#     "Amanda": 78,
#     "Charlie": 92
# }

# num = {k for k in scores.keys() if 'A' in k }
# num = {k:v for k,v in scores.items() if k.startswith('A') }
# num = list(filter(lambda x: 'A' in x , scores.keys()))

# print(num)

"""
4. Filter Dictionary by Value in List
Task: From a dictionary of fruits and their quantities, filter out the fruits that are in a given list.
"""


# fruits = {
#     "apple": 10,
#     "banana": 20,
#     "cherry": 30,
#     "date": 40
# }
# selected = ["apple", "cherry"]
#
# num  = {k:v for k,v in fruits.items() if k in selected}
# print(num)



"""
6. Filter Dictionary Using filter() Function
Task: Use the filter() function to extract key-value pairs from a dictionary where the value is greater than 50.

"""

numbers = {
    "a": 10,
    "b": 60,
    "c": 30,
    "d": 80
}


num  = dict(filter(lambda item:item[1]>= 50,numbers.items()))
print(num)