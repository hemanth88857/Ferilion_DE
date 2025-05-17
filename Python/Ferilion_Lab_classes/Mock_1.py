'''1.'''

# num = int(input("enter number: "))
#
# for each in range(1,num):
#
#     if each % 3 == 0 and each % 5 == 0:
#         print(f"FizzBuzz{each}")
#     elif each % 3 == 0 :
#         print(f"Fizz {each}")
#     elif each % 5 == 0:
#         print(f"Buzz {each}")
#     else:
#         pass

'''2.'''

dict1 = {"a" : 1,"b": 2}
dict2 = {"b":2,"C":4}

dict3 = []
for each in dict1.keys():
    if each  in dict2:
        dict3.append(each)
print(dict3)



'''4.'''

dict4 = {"a":1,"b":2,"c":1}
dict5 = {}

for each in dict4:
    if dict4[each] != 1:
        dict5[each] = dict4[each]

print(dict5)



'''6.'''

set1 = {1, 2, 3}
set2 = {2,3,4}

set3 = set()
print(set3)

for each in set1:
    if each in set2:
        set3.add(each)
print(set3)







