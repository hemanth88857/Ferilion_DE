"""
Author : GOVIND
Date   : 16-04-2025
"""
"""
req:
----
state   : dt/ds input output
behavior: BL - CRUD - DM LOOPS OPERATORS

mutable   : list set dict
immutable : int float complex bool None str tuple

iterables : str list tuple set dict range
sequence  : str list tuple range
unordered : set

operators:
----------
AC L MA IB

Decision Making:
----------------

if elif else


if i have money greater than 500            i will go to movie
--------------------------------            ------------------
    situation                                    decision

if condition1:
    execute this block of code if  condition1 is True
elif condition2:
    execute this block of code if condition1 - False and condition2 - True
elif condition3:
    execute this block of code - condition1, condition2 - False - condition3 - True
else:
    execute this block of code - above all conditions - False 

500 go to movie
1000 go for shopping
5000 go for trip    

35 - 
50 -
75 -      
"""
# money = int(input("enter money: "))
#
# if money >= 500:
#     print("I will go to movie")
# else:
#     print("study python")
""
# money = int(input("enter money: "))
#
# if money >= 5000:
#     print("go to trip")
# elif money >= 1000:
#     print("go for shopping")
# elif money >= 500:
#     print("go to movie")
# else:
#     print("study python")
""
# money = int(input("enter money: "))
#
# if money >= 5000:
#     print("go to trip")
# if money >= 1000:
#     print("go for shopping")
# if money >= 500:
#     print("go to movie")
# else:
#     print("study python")
""
"logical operators - and or not"

# day_type = input("enter the day type weekday/weekend: ")
# money  = int(input("enter the money: "))
#
# if day_type == "weekend" or money >= 500:
#     print("go to movie")
#
# s = None
#
# if not s:
#     print("no data present")
# else:
#     print("data is present")

""""""

# money = int(input("enter money: "))
#
# if 500 <= money < 1000:
#     print("go to movie")
# elif 1000 <= money < 5000:
#     print("go to shopping")
# elif money >= 5000:
#     print("go to trip")
#
# if 500 <= money < 1000:
#     print("go to movie")
# if 1000 <= money < 5000:
#     print("go to shopping")
# if money >= 5000:
#     print("go to trip")

""
# num = int(input("enter a number: "))
#
# if num > 0:
#     print("positive")
# elif num < 0:
#     print("negative")
# else:
#     print("zero")
""""""
# marks = int(input("enter marks: "))
#
# if 35 > marks > 0:
#     print("fail")
# elif 35 <= marks < 50:
#     print("just pass")
# elif 50 <= marks < 75:
#     print("second class")
# elif 75 <= marks <= 100:
#     print("first class")
# else:
#     print("enter valid marks")

#
# day_type = input("enter day type weekday/weekend: ")

# if day_type == "weekday":
#     print("go to office")
# elif day_type == "weekend":
#     activity_type = input("enter activity type movie/trip/party: ")
#     if activity_type == "movie":
#         movie_type = input("enter movie type ott/theatre: ")
#         if movie_type == 'ott':
#             print("watch the movie in ott")
#         elif movie_type == "theatre":
#             print("watch the movie in theatre")
#         else:
#             print("please provide valid movie type ott/theatre")
#     elif activity_type == "trip":
#         trip_type = input("enter trip type local/outstation: ")
#
#         if trip_type == 'local':
#             print("go to local trip")
#         elif trip_type == "outstation":
#             print("go to outstation trip")
#         else:
#             print("please provide valid trip type local/outstation")
#     elif activity_type == "party":
#         party_type = input("enter party type house/outside: ")
#         if party_type == "house":
#             print("enjoy house party")
#         elif party_type == "outside":
#             print("enjoy outside party")
#         else:
#             print("please provide valid party type house/outside")
#     else:
#         print("please provide activity type movie/trip/party")
# else:
#     print("please provide valid day type weekday/weekend")

# day = input("enter the daytype of the week - weekday/weekend- ")
# # print(day)
#
# if not day == "weekday" or not day == "weekend":
#     print("provide valid day type")

"""
day = weekday
weekday != weekday or weekday != weekend
weekday

day = weekend
weekend != weekday or weekend != weekend
weekend

day = sunday
sunday != "weekday" or sunday != "weekend"
sunday


"""