''' 1.create a tuple '''
import copy

# tuple = ("hemanth","raja","mani",12,True,89.0)
# print(tuple)
# print(tuple[1])

''' 2.create a tuple with different data types '''

# tuple1 = ("hemanth","raja","mani",12,True,89.0,[23,24],{"age":25})
# print(tuple1)


''' 3.create a tuple with numbers and print one item '''
# tuple1 = ("hemanth","raja","mani",12,True,89.0,[23,24],{"age":25})
# print(tuple1)

'''4. unpack a tuple in several variables'''

# data = ("John", 25, "New York")
# print(f"Name: {data[0]}, Age : {data[1]}, City :{data[2]}")


# info = (101, "Alice", "Engineer", 50000)
#
# for each in info:
#     print(each,end = " ")

# items = (5, 10, 15, 20, 25, 30,35)
# val = len(items)//2
#
# print(f" First: {items[0]}, Middle: {val} , Last: {items[-1]}")

''' 5. add an item in a tuple '''

# items = (5, 10, 15, 20, 25, 30,35)
#
# items = list(items)
# items.append(9)
# items = tuple(items)
# print(items)


''' 6. convert a tuple to a string '''

# items = (5, 10, 15, 20, 25, 30,35)
# items = str(items)
# print(items)

# string_items = " ".join(str(i) for i in items)
# print(string_items)
#

''' 7. get the 4th element and 4th element from last of a tuple '''


# items = (5, 10, 15, 20, 25, 30, 35,40)
#
# # 4th element → index 3
# print(items[3])
#
# # 4th element from last → index -4
# print(items[-4])
#
# # swap 4th & 4th
#
# items = list(items)
# items[3],items[-4] = items[-4],items[3]
# items = tuple(items)
# print(items)
'''  8	create the colon of a tuple'''


# items = (5, 10, 15, 20, 25, 30,35,[])
#
# tuple_colon = copy.deepcopy(items)
# tuple_colon[-1].append(44)
# print(items)
# print(tuple_colon)

'''9. find the repeated items of a tuple '''
# items = (5, 10, 15, 20, 5, 30,15)
#
# items_rep = []
#
# for each in items:
#     if items.count(each) > 1 and each not in items_rep:
#         items_rep.append(each)
#
# print(items_rep)

'''10	check whether an element exists within a tuple '''

# items = (5, 10, 15, 20, 5, 30,15)
# ele = 5
#
# if ele in items :
#     print("preset")

'''   '''

'''

11	Tuple	Basic	convert a list to a tuple
12	Tuple	Basic	 remove an item from a tuple
13	Tuple	Basic	slice a tuple
14	Tuple	Basic	find the index of an item of a tuple.
15	Tuple	Basic	find the length of a tuple
16	Tuple	Basic	convert a tuple to a dictionary
17	Tuple	Basic	 unzip a list of tuples into individual lists.
18	Tuple	Basic	reverse a tuple.
19	Tuple	Basic	convert a list of tuples into a dictionary
20	Tuple	Basic	print a tuple with string formatting
21	Tuple	Basic	 replace last value of tuples in a list
22	Tuple	Basic	 to remove an empty tuple(s) from a list of tuples
23	Tuple	Basic	sort a tuple by its float element.
24	Tuple	Medium	 count the elements in a list until an element is a tuple
1	Set	Basic	Create a set.
2	Set	Basic	Iteration over sets.
3	Set	Basic	Add member(s) in a set.
4	Set	Basic	Remove item(s) from set
5	Set	Basic	Remove an item from a set if it is present in the set.
6	Set	Basic	Create an intersection of sets
7	Set	Basic	Create a union of sets
8	Set	Basic	Create set difference
9	Set	Basic	Create a symmetric difference.
10	Set	Medium	Issubset and issuperset.
11	Set	Medium	Create a shallow copy of sets.
12	Set	Basic	Clear a set.


13	Set	Medium	Use of frozensets
14	Set	Basic	Find maximum and the minimum value in a set
15	Set	Basic	Find the length of a set
1	Arrays	Basic	Create an array of 5 integers and display the array items. Access individual element through indexes.
2	Arrays	Basic	Append a new item to the end of the array.
3	Arrays	Basic	Reverse the order of the items in the array.
4	Arrays	Medium	Get the length in bytes of one array item in the internal representation.
5	Arrays	Medium	Get the current memory address and the length in elements of the buffer used to hold an arrays? contents and also find the size
6	Arrays	Medium	Get the number of occurrences of a specified element in an array
7	Arrays	Basic	Append items from inerrable to the end of the array
8	Arrays	Basic	Convert an array to an array of machine values and return the bytes representation
9	Arrays	Basic	Append items from a specified list.
10	Arrays	Medium	Insert a new item before the second element in an existing array.
11	Arrays	Basic	Remove a specified item using the index from an array.
12	Arrays	Medium	Remove the first occurrence of a specified element from an array.
13	Arrays	Basic	Convert an array to an ordinary list with the same items.

'''

# n= 5
# for i in range(n):
#     for j in range (n+1):
#         if i+j <= n :
#             print("X",end="")
#         else:
#             print(" ",end="")
#     print()

# for i in range(n):
#     for j in range (n+1):
#         if j >= i  :
#             print("X",end="")
#         else:
#             print(" ",end="")
#     print()


# def print_full_name(first, last):
#     val = ''
#     if len(first) <= 10 and len(last) <= 10:
#         val = globals()
#         # val = f"Hello {first}{last}! You just delved into python."
#         val = "Hello "+ first + " "+ last+ "! You just delved into python."
#     else:
#         print("Invalid input length")
#     return val
#
#
# if __name__ == '__main__':
#     first_name = "hemanth"
#     last_name = "kumar"
#     result = print_full_name(first_name, last_name)
#     print(result)


