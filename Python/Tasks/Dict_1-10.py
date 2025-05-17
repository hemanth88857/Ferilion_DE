''' 1 Prints each item and its corresponding type from the following list. '''
from operator import itemgetter

data = {
    "name": "Alice",
    "age": 30,
    "is_employee": True,
    "skills": ["Python", "SQL"],
    "details": {"city": "New York"}
}

# for key in data:
#     print(f"key : {key}, value : {data[key]},class : {type(data[key])}")


# returns a list of tuples, where each tuple contains the key, value, and type of value.




# info = {"id": 101, "name": "Bob", "salary": 50000.0}
#
# val = []
# for key in info:
#     # dict = ({key,info[key]})
#     dict = info[key]
#     val.append((key,dict,type(dict)))
# print(val)

''' 2. To sort (ascending and descending) a dictionary by value  '''
# data = {"apple": 3, "banana": 1, "cherry": 2}
#
# # Asc
# data = sorted(data.items(),key = itemgetter(1),reverse = False)
# print(data)
# # Desc
# data = sorted(data.items(),key = itemgetter(1),reverse = True)



# scores = {
#     "Tom": 85,
#     "Jerry": 92,
#     "Spike": 85,
#     "Tyke": 90
# }
#
# scores = sorted(scores.items(),key=itemgetter(1))
# print(scores)



# students = {
#     "A": {"score": 88, "age": 20},
#     "B": {"score": 75, "age": 21},
#     "C": {"score": 92, "age": 19}
# }

# student = dict(sorted(students.items(),key = lambda item:item[1]["score"],reverse= True))
# print(student)

# students = sorted(students.items(),key=lambda  item : item[1]["score"],reverse= True)
# print(students)

# colors = {
#     "pen": "blue",
#     "pencil": "green",
#     "eraser": "black",
#     "marker": "red"
# }
#
# colors = sorted(colors.items(),key=lambda item:item[1])
# print(colors)

''' 3.Add a key to a dictionary '''

# colors = {
#     "pen": "blue",
#     "pencil": "green",
#     "eraser": "black",
#     "marker": "red"
# }

# colors.update({"crayons": "wi"})
# print(colors)
# colors.update({"crayons":""})
# colors["chart"] = "orange"
# colors.setdefault("crayons","pink")
# print(colors)

'''4. Check if a given key already exists in a dictionary'''

# colors = {
#     "pen": "blue",
#     "pencil": "green",
#     "eraser": "black",
#     "marker": "red"
# }
#
# given_key = "pen"
#
# if given_key in colors:
#     print("presnt")
# else:
#     print("not present")
#
# print(given_key  in colors)
# List All Missing Keys from a Given List
# person = {"name": "John", "city": "London"}
# keys_to_check = ["name", "age", "city","gender"]
# missing_keys = []

# for each in person:
#     for key in keys_to_check:
#         if key not in person and key not in missing_keys:
#             missing_keys.append(key)
#
# print(f"Missing keys : {missing_keys}")


# Check if Multiple Keys Exist
# data = {"id": 101, "name": "Nina", "role": "Admin"}
# required_keys = ["id", "role","age"]
#
#
# for each in required_keys:
#     if each not in data.keys():
#         print(f"found: {each}")


    # Check if At Least One Key Exists

# data = {"timeout": 30, "retry": 3}
# required_keys = ["url", "timeout", "headers","retry"]
#
#
# for each in required_keys:
#     if each  in data.keys():
#         print(f"found: {each}")
#         break
#

# profile = {
#     "user": {
#         "name": "Eva",
#         "email": "eva@example.com"
#     },
#     "active": True
# }
# key_to_check = "email"


# if key_to_check in profile["user"]:
#     print("exsits")


# for each in profile:
#     if isinstance(profile[each],dict):
#         if key_to_check in profile[each]:
#             print("yes")

'''5.Generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x)'''

# n = 5
# data = {}
#
# for each in range(1,n+1):
#     # data.setdefault(each,each*each)
#     data[each] = each*each
# print(data)


'''6	Print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys '''
# n = 15
# data = {}
#
# for each in range(1,n+1):
#     # data.setdefault(each,each**each)
#     data[each] = each**each
# print(data)



''' 7.Merge two Python dictionaries '''
# dict1 = {"a": 1, "b": 2}
# dict2 = {"c": 3, "d": 4}
#
# dict1 = {"x": 100, "y": 200}
# dict2 = {"y": 250, "z": 300}
#
#
# for each in dict2:
#     # dict1.setdefault(each,dict2[each])
#     dict1[each] = dict2[each]
# print(dict1)



''' 8. Sum all the items in a dictionary '''
# dict1 = {"a": 1, "b": 2 ,"c": 3, "d": 4}
# val = 0
#
# for each in dict1:
#     val += dict1[each]
# print(val)
#
# val2 = sum(dict1.values())
# print(val2)


'''9.Multiply all the items in a dictionary'''

# dict1 = {"a": 1, "b": 2 ,"c": 3, "d": 4}
# val = 1
#
# for each in dict1.values():
#     val *= each

'''  10.Map two lists into a dictionary'''

# keyss = ['id', 'name', 'age']
# values = [101, 'Alice', 25]
#
# keys = ['a', 'b', 'c']
# values = [10, 20]
#
# list_dict = {}
#
# for key,value in zip(keyss,values):
#     list_dict[key] = value
#
#
# print(values)
# map_lists_to_dict(['x', 'y'], [5, 6])


# def map_lists_to_dict(key,val):
#     return dict(zip(key,val))
#
# newval = map_lists_to_dict(['x', 'y'], [5, 6])
# print(newval)



# keys = ['id', 'name', 'role']
# values = [1001, 'Bob']
# dict = {}
#
# for i in range(len(keys)):
#     if i < len(values):
#         dict[keys[i]]= values[i]
#     else:
#         dict[keys[i]] = None
#
# print(dict)

''' 11. Sort a dictionary by key '''


# scores = {
#     "Tom": 85,
#     "Jerry": 92,
#     "Spike": 85,
#     "Myke": 90
# }
#
#
# scores = sorted(scores.items(),reverse= True)
# print(scores)



''' Get the maximum and minimum value in a dictionary. '''


# scores = {
#     "Tom": 85,
#     "Jerry": 92,
#     "Spike": 83,
#     "Myke": 90
# }
#
# max_score = max(scores.values())
# min_score = min(scores.values())
# print(f" max_score : {max_score} , min_score:{min_score}")
#
#
# max_score = max(scores,key=scores.get),max(scores.values())
# min_score = min(scores ,key= scores.get),min(scores.values())
# print(f" max_score : {max_score} , min_score:{min_score}")
#
# item_prices = {"item1": 120, "item2": 250, "item3": 90}
# #
#
# def prices(price):
#     max_price = max(price, key=price.get), max(price.values())
#     min_price = min(price, key=price.get), min(price.values())
#
#     return (max_price,min_price)
#
# resuilts = prices(item_prices)
# print(f"max : {resuilts[0]}, min : {resuilts[1]}")



# points = {"A": 100, "B": 85, "C": 100, "D": 70}
# max_points = []
# min_points = []
#
# for each in points:
#     if points[each] == max(points.values()):
#         max_points.append(each)
#     if points[each] == min(points.values()):
#         min_points.append(each)
# print(max_points)
# print(min_points)

''' 13.Remove duplicates from Dictionary  '''


# points = {"a": 1, "b": 2, "c": 1, "d": 3}
#
# uniqu_dict = {}
#
# for val in points:
#     if points[val] not in uniqu_dict.values():
#         uniqu_dict[val] = points[val]
#
# points = uniqu_dict
# print(points)

""" 14 Combine two dictionary adding values for common keys."""
dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 5, 'c': 15, 'd': 25}


# for each in dict2:
#     if each in dict1:
#         dict1[each] = dict1[each]+ dict2[each]
#     else:
#         dict1.setdefault(each,dict2[each])
#
# print(dict1)
#
#
# def com_keys(dict1=dict,dict2=dict)-> dict[str:int]:
#     for each in dict2:
#         if each in dict1:
#             dict1[each] = dict1[each]+ dict2[each]
#         else:
#             dict1.setdefault(each,dict2[each])
#
#     return dict1
#
# print(com_keys(dict1,dict2))


"""15 Print all unique values in a dictionary """

# data1 = {"a": 100, "b": 200, "c": 100, "d": 300, "e": 200 }
# data = { "x": "apple", "y": "banana", "z": "apple", "w": "cherry" }
#
#
# def unique_values(uni_val) :
#
#     data2 ={}
#     for each in uni_val:
#         if uni_val[each] not in data2.values():
#             data2[each] = uni_val[each]
#     return data2
#
# print(unique_values(data1))
# print(unique_values(data))

"""17 Find the highest 3 values in a dictionary"""
data = {
    "a": 100,
    "b": 250,
    "c": 175,
    "d": 300,
    "e": 50,
    "f":275
}

new_dict_values= sorted(data.values(),reverse=True)[:3]

print(new_dict_values)
new_dict_keys= sorted(data.items(),key= lambda  x:x[1], reverse=True)[:3]
print(new_dict_keys)

'''



16	Dictionary	Medium	Create and display all combinations of letters, selecting each letter from a different key in a dictionary
17	Dictionary	Difficult	Find the highest 3 values in a dictionary.
18	Dictionary	Medium	Combine values in python list of dictionaries.
19	Dictionary	Basic	Create a dictionary from a string.
20	Dictionary	Basic	Print a dictionary in table format.
21	Dictionary	Medium	Count the values associated with key in a dictionary
22	Dictionary	Medium	Convert a list into a nested dictionary of keys.
23	Dictionary	Medium	Sort a list alphabetically in a dictionary.
24	Dictionary	Medium	Remove spaces from dictionary keys.
25	Dictionary	Difficult	Get the top three items in a shop.
26	Dictionary	Basic	To get the key, value and item in a dictionary.
27	Dictionary	Basic	print a dictionary line by line.
28	Dictionary	Basic	Check multiple keys exists in a dictionary.
29	Dictionary	Medium	Count number of items in a dictionary value that is a list
30	Dictionary	Medium	Sort Counter by value.
31	Dictionary	Medium	create a dictionary from two lists without losing duplicate values.
32	Dictionary	Medium	Replace dictionary values with their sum.
33	Dictionary	Medium	Match key values in two dictionaries.

'''