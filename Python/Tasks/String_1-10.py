''' 1.Length of string '''
import random
from operator import index

# Value = input("Enter any name as Value1: ")
# print(len(Value))

''' 2.Count characters in string '''

# name = "hemanth"

# for each in set(name):
#     print(each , name.count(each))

''' 3.String slicing '''
# name = "hemanth"
# # print(name[:3])
# # print(name[3:])
# # print(name[::-1])
# print(name[1:len(name):2])

''' 4 Replace first occurance character '''
# name = "hemnggh"
# name = name.replace(name[0],"y")
# print(name)


''' 5 Swapping chars in string '''

# swap_string = "hemanth"
# swap_string = list(swap_string)
#
#
# for i in range(len(swap_string)):
#     for j in range(len(swap_string)-1,-1,-1):
#         swap_string[i],swap_string[j] = swap_string[j],swap_string[i]
#
# print(swap_string)
# random.shuffle(swap_string)
# print(swap_string)


''' 6 Append chars to string at end '''
# name  = "Hemanth"
# name = name + "q"
# print(name)

''' 7 Substring replacement '''

# gretings = "hello"
#
# gretings = gretings.replace("hello","welcome to new")
# print(gretings)

''' 8 Length of longest string in python '''

# sentence = "Python Java JavaScript C AngularScript "
#
# word1 = ""
# word2 = ""
#
# for each in sentence:
#     if each == " ":
#         word1 = ""
#     else:
#         word1 += each
#     if len(word1)>len(word2):
#         word2 = word1
# print(word2)
#
#
# word3 = ""
#
# for each in sentence.split(" "):
#
#     if len(word3) < len(each):
#         word3 = each
#
# print(word3)


# nested_list = [["hi", "hello"], ["goodbye", "welcome"], ["yes"]]
# nested_list = [("apple", "banana"), ("cherry", "fig", "grapees")]


# longest = ""
# for each in nested_list:
#     for j in each:
#         if len(longest) <= len(j):
#             longest = j
#             # print(j)
#
# print(longest)

''' 9 nth index character from string '''

# text = "programming"
# n = 3
#
# print(text[n])
# # If the index is out of bounds, print "Invalid index".
# n = 15
# if n > len(text):
#     print("invalid index")
# else:
#     print(text[n])
#
#
# try:
#     print(text[n])
# except IndexError:
#     print("invalid")
#  print characters at all specified indexes.

# text = "datascience"
# indexes = [0, 2, 5, 10]
#
# for each in indexes:
#     print(text[each])


#  remove the character at the n-th index from a string.


# text = "technology"
# n = 4
#
# text = text.replace(text[4],'')
# print(text)

# return the character at the n-th index from the end of the string.

# text = "artificial"
# n = 4
# print(text[-n])


''' 10  First last chars swapping  '''

# text = "artificial"
# fristchar = text[0]
# lastchar = text[-1]
#
# text = lastchar + text[1:-1] + fristchar

# print(text)

''' 11  Remove odd index values  '''

# text = "artificial"
# text = text[::2]
# print(text)
#
#
# new_text = ""
# for i in range(len(text)):
#     if i % 2 == 0:  # Keep only even index characters
#         new_text += text[i]

# print(new_text)

''' 12  Count words in a string  '''

# sentence = "If you have a table with duplicates"
# val = 0
#
# for each in sentence.split(" "):
#     val+= 1
#
# print(val)


''' 13 Upper lower case of a string '''

# sentence = "If you have a table with duplicates"
#
# sentence = sentence.upper()
# print(sentence)
# sentence = sentence.lower()
# print(sentence)

''' 14 Sort unique words alphanumerically '''

# # input_string = "banana apple cherry apple banana mango"
# input_string = "zebra,apple,monkey,apple,zebra,dog"
#
#
# strings = []
#
# for each in input_string.split(','):
#     if each not in strings:
#         strings.append(each)
#
# print(sorted(strings))
#
# strd = sorted(list(filter(lambda x:x ,input_string.split(','))))
# print(strd)
#
#
# set1 = set(input_string.split(','))
# print(sorted(list(set1)))


'''   16 Insert string in middle of speical chars '''

"""""
base = "[[]]"
word = "World"

base = "###*###"
word = "Test"

midlevel = len(base)//2
print(midlevel)

half1 = base[:midlevel]
half2 = base[midlevel:]
word =  half1 + word + half2

print(half1,half2)
print(word)


def insert_in_middle(base,word):

    mid_value = 0
    if len(base) % 2  == 0:
        mid_value = len(base) // 2
    else:
        mid_value = (len(base)//2 ) + 1

    return base[:mid_value] + word + base[mid_value:]

print(insert_in_middle(base = "[[]]" , word = "World"))
print(insert_in_middle(base = "###*###" , word = "World"))


"""""

''' 17 	4 Copies of last 2 chars '''

# def string_copies(text,copies,chars):
#
#     text_char = text[-(chars):]
#     return copies*text_char
#
# print(string_copies("n",1,2))


''' 18 Length of first 3 chars '''

# def length_of_chars(text,char):
#
#     return text[:char]
# print(length_of_chars("python",3))

''' 20  reverses a string if it's length is a multiple of 4'''


# def reverse_string_multiple(text,multiple):
#
#     if len(text) % multiple == 0 :
#         return  text[::-1]
#     return text
#
# print(reverse_string_multiple("thatshow99",5))


''' Convert a given string to all uppercase'''


# def case_manipulation(text):
#
#     return text.upper()
#
# print(case_manipulation("heman"))



''' program to check whether a string starts with specified characters'''


# def check_spec_char(text,spec_char):
#
#     if text.startswith(spec_char):
#         return True
#     return False
#
#
# print(check_spec_char("python is a interpreter language","python"))


'''program to sort a string lexicographically'''

name = 'banana apple Orange grape'
new_str = ""

print(sorted(name.split(' ')))
# for each in sorted(name):
#     new_str += each
#
# print(new_str)

def lexicographically_sent(sentence):
    new_str = ""
    if " " in sentence:
        for each in sorted(sentence.split(' ')):
            new_str += each + " "
        new_str = new_str.removesuffix(" ")
    else:
        for each in sorted(sentence):
            new_str += each


    return new_str

print(lexicographically_sent("banana apple Orange grape"))
print(lexicographically_sent("banana apple orange grape"))



def lexicographically(word):
    word = word.replace(" ","")
    new_str = ""
    for each in sorted(word):
        new_str += each

    return new_str
print(lexicographically("pPthOonN"))
print(lexicographically("open ai"))





'''


15	String	Difficult	Create html from string
19	String	Basic	Last part of string
22	String	Medium	program to sort a string lexicographically
23	String	Basic	program to remove a newline in Python
25	String	Medium	program to create a Caesar encryption
26	String	Medium	display formatted text (width=50) as output
27	String	Medium	remove existing indentation from all of the lines in a given text
28	String	Medium	to add a prefix text to all of the lines in a string
29	String	Basic	to set the indentation of the first line
30	String	Basic	to print the following floating numbers upto 2 decimal places
31	String	Basic	print the following floating numbers upto 2 decimal places with a sign
32	String	Medium	print the following floating numbers with no decimal places
33	String	Medium	print the following integers with zeros on the left of specified width
34	String	Medium	print the following integers with '*' on the right of specified width
35	String	Basic	to display a number with a comma separator
36	String	Basic	to format a number with a percentage
37	String	Medium	to display a number in left, right and center aligned of width 10
38	String	Basic	to count occurrences of a substring in a string
39	String	Medium	reverse a string
40	String	Medium	reverse words in a string
41	String	Medium	strip a set of characters from a string
42	String	Basic	count repeated characters in a string
43	String	Medium	 square and cube symbol in the area of a rectangle and volume of a cylinder
44	String	Basic	print the index of the character in a string
45	String	Medium	check if a string contains all letters of the alphabet
46	String	Basic	convert a string in a list
47	String	Medium	lowercase first n characters in a string
48	String	Basic	swap comma and dot in a string
49	String	Basic	count and display the vowels of a given text
50	String	Medium	split a string on the last occurrence of the delimiter
51	String	Medium	find the first non-repeating character in given string
52	String	Difficult	print all permutations with given repetition number of given string
53	String	Medium	find the first repeated character in a given string
54	String	Difficult	find the first repeated character of a given string where the index of first occurrence is smallest
55	String	Medium	find the first repeated word in a given string
56	String	Medium	find the second most repeated word in a given string
57	String	Basic	remove spaces from a given string
58	String	Basic	move spaces to the front of a given string
59	String	Medium	 find the maximum occurring character in a given string
60	String	Basic	capitalize first and last letters of each word of a given string
61	String	Medium	remove duplicate characters of a given string
62	String	Medium	compute sum of digits of a given string
63	String	Basic	remove leading zeros from an IP address
64	String	Medium	Reverse a given string  Input : "Python"   Output : "nohtyP"
65	String	Medium	Reverse each word in given string Input 
66	String	Medium	Reverse each word and reverse word again. Input
67	String	Medium	that accepts a string and calculate the number of digits and letters



'''