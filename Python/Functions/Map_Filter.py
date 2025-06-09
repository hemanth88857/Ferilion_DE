"""
1. Square Numbers in a List
"""

# numbers = [1, 2, 3, 4, 5]
#
# square = list(map(lambda x:x*x,numbers))
# print(square)

"""
2. Convert Strings to Uppercase
"""
# fruits = ['apple', 'banana', 'cherry']
# uper = list(map(lambda x:x.upper(),fruits))
# print(uper)


"""
3. Add Corresponding Elements of Two Lists

"""

# a = [1, 2, 3]
# b = [4, 5, 6]
#
# cors = list(map(lambda x,y:x+y,a,b))
# print(cors)


"""
5. Remove Leading and Trailing Whitespaces from Strings

"""

# strings = ['  hello  ', '  world ', ' python  ']
# new_str = list(map(str.strip,strings))
# print(new_str)



"""
6. Extract First Character from Each String

"""
#
# words = ['apple', 'banana', 'cherry']
#
# num = list(map(lambda x:x[0],words))
# print(num)


"7. Convert List of Integers to Strings"
numbers = [1, 2, 3, 4]
string_numbers = list(map(lambda x:str(x),numbers))
print(string_numbers)