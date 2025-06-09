import copy
import random
from itertools import count
from numbers import Number
from tkinter.font import names


'''    1.Sum of elements     '''

# elements = [1,5,6,7,5,4,6,9,4,3,2]
# def sum_of_elements_case_1(Num):
#     # num = sum(Num)
#     # print(num)
#     pass
# sum_of_elements_case_1(elements)
#
# def sum_of_elements_case_2(num):
#     # val = 0
#     # for each in num:
#     #     val += each
#     # print(val)
#     pass
# sum_of_elements_case_2(elements)

# ----------------------------------------------------------------------------------------
''' 2 Mulitply of elements    '''
# Numbers = [1,5,6,7,5,4,6,9,4,3,2]
# elements = [1,5,6,7,5,4,6,9,4,3,2]

# def multi_of_elements_case_1(num):
#     # val = 1
#     # for each in num:
#     #     val *= each
#     # print(val)
#     pass
# multi_of_elements_case_1(elements)
# ----------------------------------------------------------------------------------------


''' 3	Largest number from list   '''
# val = Numbers[0]
# for each in Numbers:
#     if each >= val:
#         val  = each
# print(val)
# ----------------------------------------------------------------------------------------

'''  4	List	Basic	Smallest number from list  '''
# Numbers = [1,5,6,-7,5,4,6,9,4,3,2,-1]
# val = Numbers[0]
# for each in Numbers:
#     if each <= val:
#         val  = each
# print(val)
## ----------------------------------------------------------------------------------------

'''  5	Count no of strings whose length is 2  '''
# Names = ["Ayesha Sharma", "Ra", "Sneha Reddy", "Karan Patel", "Priya Nair"]
# StringCount = 0
#
# for each in Names:
#     if len(each) == 2 :
#         StringCount += 1
#
# if StringCount > 1 :
#     print(f"No of string {StringCount}")
# else:
#     print(f"No of string {StringCount}")

# ----------------------------------------------------------------------------------------

''' 6	Sort elements in increasing order   '''
Numbers = [1,5,6,7,5,4,6,9,4,3,2]
#case-1

# num = sorted(Numbers)
# print(num)

#Case -2
# Value = []
# for _ in range(0,len(Numbers)):
#     Value.append(min(Numbers))
#     Numbers.remove(min(Numbers))
#
# Numbers = Value
# print(Numbers)

# ----------------------------------------------------------------------------------------

''' 7	Remove duplicates '''
#numbers = [1, 5, 6, 7, 5, 4, 6, 9, 4, 3, 2]

#Case-1
# for num in numbers[:]:
#     if numbers.count(num) > 1:
#         numbers.remove(num)
#
# print(numbers)



#Case-2

# unique_numbers = []
#
# for num in numbers:
#     if num not in unique_numbers:
#         unique_numbers.append(num)
#
# print("List after removing duplicates:", unique_numbers)

# ----------------------------------------------------------------------------------------

''' 8	Check list is empty or not '''

# Numbers = []
#
# #case-1
# if len(Numbers) >= 1 :
#     print("Not empty")
# else:
#     print("Empty")


# ----------------------------------------------------------------------------------------


''' 9	Clone or copy '''

lst = [1,3,4,5,6,6,7,8,2,4,5,6,6]

#case -1
# lst2 = lst.copy()
# lst3 = copy.deepcopy(lst)
# print(lst3)
# print(lst2)
#
# #case =
# lst4 = []
# for each in lst:
#     lst4.append(each)
# print(lst4)


# ----------------------------------------------------------------------------------------

''' 10	Words that are longer than any element  '''
input_words = [
    "apple",        # length = 5
    "banana",       # length = 6
    "kiwi",         # length = 4
    "watermelon",   # length = 10
    "pear",         # length = 4
    "strawberry",   # length = 10
    "fig"           # length = 3
]
#case = 1 print strawberry
# val =input_words[0]
# for each in range(len(input_words)):
#     if len(input_words[each]) >= len(val):
#         val = input_words[each]
# print(val)


#case = 2 print watermelon

# val = max(input_words)
# print(val)

#case = 3 print strawberry,watermelon
# lst = []
#
# val =input_words[0]
# for each in range(len(input_words)):
#     if len(input_words[each]) >= len(val):
#         val = input_words[each]
# lst.append(val)
#
# if len(lst) >= 1 :
#     for  i in input_words:
#         if len(i) == len(lst[0]) and i  not in lst:
#             lst.append(i)
# print(lst)


# case 4

# lst = []
# val = max(input_words)
# for each in range(len(input_words)):
#     if len(input_words[each]) == len(val) and input_words[each] not in lst:
#         lst.append(input_words[each])
#
# print(lst)

# ----------------------------------------------------------------------------------------

''' 11	Find common element from 2 lists  '''
#
# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]
#
# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {'b': 4, 'c': 5, 'd': 6}
#
# str1 = "python"
# str2 = "notebook"
#
# tuple1 = [(1, 2), (3, 4), (5, 6)]
# tuple2 = [(3, 4), (7, 8), (1, 2)]
#
#
#
# def Comm_Elements_Case_1() :
#     fruits_list1 = ["Apple", "Banana", "Mango", "Cherry", "Grapes"]
#     fruits_list2 = ["Pineapple", "Banana", "Kiwi", "Apple", "Papaya"]
#     val = []
#
#     for each in fruits_list1:
#         if each in fruits_list2:
#             val.append(each)
#
#     if len(val) >= 1:
#         print(val)
#     else:
#         print("no matching")
# # Comm_Elements_Case_1()
#
# def Comm_Elements_Case_2(lst1,lst2) :
#
#     val = False
#     for each in lst1:
#         if each in lst2:
#             val = True
#     print(val)
# # Comm_Elements_Case_2(list1,list2)
#
# def Comm_Elements_Case_3(lst1,lst2) :
#
#     val = 0
#     for each in lst1:
#         if each in lst2:
#             val += 1
#     print(f"Comm_Elements_Case_3 ----{val}")
# # Comm_Elements_Case_3(list1,list2)
#
# def Comm_Elements_Case_4(dic1,dic2) :
#
#     val = []
#     for value in dic1:
#         if value in dic2:
#             val.append(value)
#     print(f"Comm_Elements_Case_4 ----{val}")
# # Comm_Elements_Case_4(dict1,dict2)
#
# def Comm_Elements_Case_tuple(tip1,tip2) :
#
#     val = []
#     for value in tip1:
#         if value in tip2:
#             val.append(value)
#     print(f"Comm_Elements_Case_4 ----{val}")
# Comm_Elements_Case_tuple(tuple1,tuple2)



''' 12 Remove specified index from list and print '''
fruits_list1 = ["Apple", "Banana", "Mango", "Cherry", "Grapes"]
# Case-1
# val = fruits_list1.pop(4)
# print(val)
# print(fruits_list1)

# Case -2

# del fruits_list1[2]
# print(fruits_list1)




''' 13 Write 3D array '''


''' 14 Remove even elements and print list '''

# even_list = [10, 15, 20, 25, 30]
# for each in even_list:
#     if each%2 == 0 :
#         even_list.remove(each)
# print(even_list)

''' 15  Shuffle list and print '''

# shuf_list = [1, 2, 3, 4, 5]
# #
# # for i in range(len(shuf_list)):
# #     for j in range(len(shuf_list)-1,-1,-1):
# #         shuf_list[i] ,shuf_list[j] =   shuf_list[j] ,shuf_list[i]
# #
# # print(shuf_list)
#
# # case2
#
# random.shuffle(shuf_list)
# print(shuf_list)



''' 16  First,Last elements whose square value is between 1 and 30 '''
# my_list  = []
#
# for each in range(1,30):
#     if each**2 > 30:
#         break
#     else:
#         my_list .append(each**2)
#
# first_element = my_list [0]
# last_element = my_list [-1]
#
# print(f"first element is {first_element} and second element is {last_element}")


''' 17 First,Last elements whose square value is between 1 and 30,except first 5'''

#
#
# def first_last_elements(input_list:list[int],expect_val):
#
#     list = input_list[expect_val:]
#     new_list  = []
#     for i in list:
#         if i * i in range(1,30):
#             new_list.append(i)
#
#     if len(new_list) >= 1 :
#         return new_list[0],new_list[-1]
#     return None
#
#
# print(first_last_elements([1,3,4,5,5,9,6,7,8,8,8,9],5))


''' 20 Difference betweeen 2 lists'''



# def list_difference_in_twolists(list1,list2)->list:
#
#     new_list = []
#     for each in list2:
#         if each not in list1:
#             new_list.append(each)
#
#     for each in list1:
#         if each not in list2:
#             new_list.append(each)
#
#     # return new_list
#
#
#     lst = [item for item in list1 if item not in list2] + \
#           [item for item in list2 if item not in list1]
#     return lst
#
#
# def list_difference(list1,list2):
#
#     new_list = []
#
#     for each in list1:
#         if each not in list2:
#             new_list.append(each)
#
#     return new_list
#
#
# print(list_difference_in_twolists([1, 2, 3, 4, 5],[2,4,6]))
# print(list_difference([1, 2, 3, 4, 5],[2,4,6]))
#
#
# list1 = ['a', 'b', 'c', 'd']
# list2 = ['b', 'e', 'f']
# print(list_difference_in_twolists(list1,list2))
# print(list_difference(list1,list2))
#
#
# list1 = [10, 20, 30]
# list2 = [10, 20, 30]
#
# print(list_difference_in_twolists(list1,list2))
# print(list_difference(list1,list2))



''' 20 To access index of list'''

input_list = ['apple', 'banana', 'cherry']

if len(input_list) >= 1:
    for each in range(len(input_list)):
        print(f"index {each} : {input_list[each]}")


'''
18	List	Medium	All permutations of list elements
19	List	Basic	Difference betweeen 2 lists
20	List	Basic	To access index of list
21	List	Basic	List of characters into string
22	List	Basic	Finding index of an item in specified list
23	List	Basic	Flatten a shallow
24	List	Basic	Append a list to second list
25	List	Basic	Select an item randomly
26	List	Basic	Check circularly identical in two lists
27	List	Basic	Finding a second smallest number
28	List	Basic	Finding a second largest number
29	List	Basic	Get unique values
30	List	Basic	Frequency of elements
31	List	Basic	Counting number elementswithin a specified ranges
32	List	Basic	Check a list contains sublist
33	List	Basic	Generate all sublists
34	List	Basic	Printing elements in ascending order
35	List	Basic	Create a list by concatenating a given list which range goes from 1 to n
36	List	Basic	Variable unique identification number
37	List	Basic	Finding common items from two lists
38	List	Basic	Change the position of every nth value with (n+1)th value
39	List	Basic	Converting multiple integers into single integer
40	List	Basic	Split a list based on first character of word
41	List	Basic	Create multiple list
42	List	Basic	Find missing and additional values
43	List	Basic	Split a list into different variables
44	List	Basic	Generate group of five consecutive numbers in a list
45	List	Basic	Convert a pair of values into a sorted unique array
46	List	Basic	Slect odd items of a list
47	List	Basic	Insert an element before each element of a list
48	List	Basic	Print a nested lists (each list on a new line) using the print() function
49	List	Basic	Convert list to list of dictionaries
50	List	Basic	Sort a list of nested dictionaries
51	List	Basic	Split a list every Nth element
52	List	Basic	Compute the similarity between two lists
53	List	Basic	Create a list with infinite elements
54	List	Basic	Concatenate elements of a list
55	List	Basic	Remove key values pairs from a list of dictionaries
56	List	Basic	Convert a string to a list
57	List	Basic	Check if all items of a list is equal to a given string
58	List	Basic	Replace the last element in a list with another list
59	List	Basic	Check if the n-th element exists in a given list
60	List	Basic	Find a tuple, the smallest second index value from a list of tuples
61	List	Basic	Create a list of empty dictionaries
62	List	Basic	Print a list of space-separated elements
63	List	Basic	Insert a given string at the beginning of all items in a list
64	List	Basic	Iterate over two lists simultaneously
65	List	Basic	Access dictionary keys element by index
66	List	Basic	Find the list in a list of lists whose sum of elements is the highest
67	List	Basic	Find all the values in a list are greater than a specified number
68	List	Basic	Extend a list without append
69	List	Basic	Remove duplicates from a list of lists
70	List	Basic	Get the depth of a dictionary
71	List	Basic	Check if all dictionaries in a list are empty or not
72	List	Basic	Two digits m (row) and n (column) as input and generates a two-dimensional array. The element value in the i-th row and j-th column of the array should be i*j
73	List	Basic	A list contains group of strings.Convert each word to capital letter and print
74	List	Basic	Reverse list of elements and print in upper case
75	List	Basic	Write a Python program to convert month name to a number of days



'''