""" 1	check given word is palindrome or not """
# def palindrome(word):
#     word2 = ""
#
#     for each in word[::-1]:
#         word2 += each
#
#     if word2 == word :
#         return f"palindrome {word} ---- {word2}"
#     return  "not a palindrome"
#
# print(palindrome("aba"))

"""2	print even and odd numbers """

# def even_odd(numtype = "even",num= int) -> list[int]:
#     num1 = []
#     if numtype.lower() == "even":
#         for each in range(num):
#             if each % 2 == 0 :
#                 num1.append(each)
#     else:
#         for each in range(num):
#             if each % 2 != 0:
#                 num1.append(each)
#     return  num1

# print(even_odd(numtype="odd",num=100))


"""3.print prime numbers"""


# def prime_numbers(num:int) -> list[int]:
#
#     primes = []
#     if num <= 1 :
#         return "not a prime number"
#     else:
#         for i in range(2,num+1):
#             for j in range(2,int(i**0.5)+1):
#                 if i%j == 0:
#                     break
#             else:
#                  primes.append(i)
#     return  primes
#
# print(prime_numbers(1))


"""4	factorial of given number """

# def factorial(num:int) -> str :
#
#     fact = 1
#     for each in range(1,num+1):
#         fact *= each
#     return fact
#
# print(factorial(4))

"""6	find cube/square of a number """

# def cube(num:int) -> int :
#
#     num = (num**num) * num
#     return num
#
# print(cube(2))
#
#
# def saqure(num:int) -> int :
#
#     num *= num
#     return num
#
# print(saqure(3))

"""7	table of the given number"""

# def table(num:int) -> str :
#
#     for each in range(1,11):
#         print(f"{num} X {each} = {num*each}")

#
# table(13)



"""8. find the Max of three numbers"""

# def max_of_number(num = list) -> int:
#         max_num = 0
#
#         for each in num:
#             if each > max_num :
#                 max_num = each
#         return max_num
#
# # max_of_number([10,14,11])
# print(max_of_number([10,14,11]))
#
#
# def max_of_number_tuple(num=tuple) -> int:
#     max_num = 0
#
#     for each in num:
#         if each > max_num:
#             max_num = each
#     return max_num
#
# # max_of_number([10,14,11])
# print(max_of_number_tuple((10,14,11,18)))

"""9	fibonacci series? """

# def fibonacci(num:int) -> int:
#
#     fibo = 0
#     fibo_series = []
#
#     for each in range(num+1):
#         fibo = fibo+(each-fibo)
#         fibo_series.append(fibo)
#     return fibo_series
#
# print(fibonacci(5))

"""10	 sum all the numbers in a list """

# def sum_of_num(num:list) -> int:
#
#     total = 0
#     for each in num:
#         total += each
#     return total
#
# print(sum_of_num([1,2,3,4,5,6,7,8,9,10]))

"""11	multiply all the numbers in a list"""

# def mul_of_num(num:list) -> int:
#
#     total = 1
#     for each in num:
#         total *= each
#     return total
#
# print(mul_of_num([1,2,3,4,5]))



"""12 to reverse a string"""

# def reverse_of_string(word) -> str:
#
#     new_word = ""
#     for each in word:
#         new_word = each + new_word
#
#     return new_word
#
# print(reverse_of_string("hem"))
#
# def reverse_of_string_1(word) -> str:
#
#     return word[::-1]
#
# print(reverse_of_string_1("money"))
#
# def reverse_of_string_2(word) -> str:
#
#     return "".join(reversed(word))
#
# print(reverse_of_string_2("mon"))

"""13	check whether a number is in a given range """
# def check_range(start= int,end=int,num=int) -> bool:
#
#         for each in range(start,end+1):
#                 return True
#             return False
#
# print(check_range(1,5,5))

# def check_range(start= int,end=int,num=int) -> bool:
#
#         for each in range(start,end+1):
#              return start<=num<=end
#
# print(check_range(1,5,6))


"""14 accepts a string and calculate the number of upper case letters and lower case letters"""

# def str_upper_lower(word:str) -> str:
#     count_lower = 0
#     count_upper = 0
#
#     for each in word:
#         if each.islower():
#             count_lower +=1
#         elif each.isupper():
#             count_upper += 1
#         else:
#             pass
#
#     return f"number of upper case letters {count_upper} and lower case letters {count_lower}"
#
# print(str_upper_lower("GYIyhhgjgy&&&&hhjfKKLk"))


''' 15 takes a list and returns a new list with unique elements of the first list.'''


# def unique_list(input_list:list) -> list:
#
#     new_list  = []
#
#     for each in input_list:
#         if each not in new_list:
#             new_list.append(each)
#
#     return new_list
#
#     # new_list = set(input_list)
#     # return list(new_list)
#
# print(unique_list([1,2,3,3,4,4,5,6,6,2,4,5,6]))



'''1	check given word is palindrome or not
2	print even and odd numbers
3	print prime numbers
4	factorial of given number
5	convert list/tuple/set to list/tuple/set
6	find cube/square of a number
7	table of the given number
8	find the Max of three numbers
9	fibonacci series?
10	 sum all the numbers in a list
11	multiply all the numbers in a list
12	to reverse a string
13	check whether a number is in a given range
14	accepts a string and calculate the number of upper case letters and lower case letters
15	takes a list and returns a new list with unique elements of the first list.
16	print the even numbers from a given list
17	print given Pascal's triangle
18	 function to display group of strings
19	function to check whether a string is a pangram or not
20	to match the item in two dictionaries.
'''