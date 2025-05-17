
"longest Palindrome"
from itertools import count

# Palindrome = "badad"
#
# l1 = []
#
# l2 = ""
#
# for each in Palindrome:
#     l2 += each
#


"2.remove dupilcates from string ,lower letters,"
#
# def palindrome(s:str):
#     unique_str = ""
#
#     s = s.replace(" ", "")
#     for each in s:
#
#         if each == each.lower():
#             s = s.replace(each, "")
#         if not unique_str.__contains__(each) and each != each.lower():
#             unique_str = unique_str + each
#     s = unique_str
#     return s
#
# str = "hE caN ToUght Me EnGLIsh EEE UUUU"
#
# print(palindrome(str))

"Fibonacci series"

#
# def fibonacci(num):
#     fib_series = [0,1]
#
#     for each in range(num+1):
#         nxt_num = fib_series[-1] + fib_series[-2]
#         fib_series.append(nxt_num)
#     return fib_series[:num]
#
# print(fibonacci(10))
#
# def fibonacci_series(n):
#     fib = [0, 1]
#     for i in range(2, n):
#         next_num = fib[-1] + fib[-2]
#         fib.append(next_num)
#     return fib
#
# # Example
# print(fibonacci_series(5))


"4.second largest element"

# lst = [5,6,7,8,9,446,797,454,232,686,454,798,808]
# num = 0
#
# for each in lst:
#
#     if each >= num:
#         num = each
# print(num)
#
#
# lst = ["hf","5hfg","gfgfd"]
# num = ""
# for each in lst:
#     for j in each:
#         num += j
#     if each >= num:
#         num = each
#     else:
#         num = ""
# print(num)

"5.dict swap"

# dict_swap = {"a":1 , "b" :2 , "c" :3}
#
# new_dict = {}
#
# for each in dict_swap:
#     new_dict[dict_swap[each]] = each
#
# print(new_dict)

"6.vowels and constancts in given string"

# def vowels_const(word):
#     vowels = ["a","e","i","o","u"]
#     vowels_const_dict  = {"vowels" : 0, "Constant" : 0}
#     word = word.replace(" ","")
#     for each in word:
#         if each.lower() in vowels:
#             vowels_const_dict["vowels"] += 1
#         else:
#             vowels_const_dict["Constant"] += 1
#     return vowels_const_dict
#
# print(vowels_const("Hello World"))

"13 odd numbers in list using filter"


nums = [1,3,4,5,6,7,8,9,11,13,15]


# num = for each in odd : if each%2 == 0 :odd.append(each)
odd = list(filter(lambda x:x%2 != 0 , nums))
# print(odd)


cubes = list(map(lambda  x:(x**x)*x,nums))
print(cubes)
