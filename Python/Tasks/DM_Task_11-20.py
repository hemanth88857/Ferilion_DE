'''
11. Telephone Bill Calculator
•	Task: Take number of calls made as input from the user and find the total telephone bill.
'''

#Calls = int(input("Enter a Valid Number: "))
#1-100  = 0.50 p
# 100 - 150 = 0.80p
# 150 - 250 = 0.90 p
# above 250 = 1 rp

# if Calls <= 0 :
#     print("NO Bill")
# elif 1 <= Calls <= 100 :
#     print("Number of calls ",Calls,"Price of each call id 0.50p : Total Bill :" ,float(Calls * 0.50))
# elif 101 <= Calls <= 150:
#     print("Number of calls ",Calls,"Price of each call id 0.80p : Total Bill :",float(Calls * 0.80))
# elif 151 <= Calls <= 250:
#     print("Number of calls ",Calls,"Price of each call id 0.90p : Total Bill :",float(Calls * 0.90))
# else:
#     print("Number of calls ",Calls,"Price of each call id 1rp : Total Bill :",float(Calls * 1))
#


'''
12. Leap Year Checker
•	Task: Take a year as input from the user and find whether it is a leap year or not.
'''

# Year = int(input("Enter a Valid Year: "))
#
# if Year <= 0 :
#     print("Enter Valid Year")
# elif (Year % 4 == 0 and Year % 100 != 0 ) or Year % 400 == 0 :
#     print("Its a leap Year")
# else :
#     print("Its a not a leap Year")

'''
13. Find the Largest of Three Numbers
•	Task: Take three numbers as input from the user and find the largest number.


'''
# First_Number = int(input("Enter valid First Number : "))
# Second_Number = int(input("Enter valid Second Number : "))
# Third_Number = int(input("Enter valid Third Number : "))
#
# largest_Number = (First_Number,Second_Number,Third_Number)
# print(max(largest_Number))

'''
14. Even or Odd Number Checker
•	Task: Take a number as input from the user and find whether it is even or odd.
'''

# Number = int(input("enter a valid Number: "))
#
# if Number <= 0 :
#     print("Please enter a valid Number")
# elif Number% 2 == 0 :
#     print("It is a even")
# else :
#     print("It is a Odd")


'''
15. Exam Eligibility Based on Attendance
•	Task: Take number of classes held and number of classes attended as input from the user and
 find the attendance percentage and whether the student is allowed to sit in the exam.


Rules
-----------
Above 70 % allow

'''
#
# Classes_Held = int(input("enter Number of Classes_Held  : "))
# Classes_Attended =  float(input("enter Number of Classes_Attended : "))
#
# percentage = (Classes_Attended / Classes_Held) * 100
# print(percentage)
#
# if ((Classes_Attended / Classes_Held) * 100) > 70 :
#     print("Allow the Student")
# else:
#     print("Student if not Suppose to Enter the Exam Hall , He/She Has Percentage of :", (Classes_Attended / Classes_Held) * 100)

'''
16. Grade Calculator
•	Task: Take marks as input from the user and find the corresponding grade based on predefined rules.


Rules
--------------------------------------------
70.00 - 100.00	First Class with Distinction/First Division with Distinction	A+
60.00 - 69.99	First Class/First Division	A
50.00 - 59.99	Second Class/Second Division	B
35.00 - 49.99	Third Class/Third Division/Pass Class	C
below 35 fail
'''

# Marks = float(input("enter a Marks: "))
#
# if   Marks < 0  or Marks > 100 :
#     print("Please enter a valid Marks")
# elif Marks > 70:
#     print("First Class ")
# elif 60 <= Marks <= 69.9:
#     print("Second Class ")
# elif 50 <= Marks <= 59.9:
#     print("Third Class ")
# elif 35 <= Marks <= 49.9:
#     print("Pass ")
# else:
#     print("Fail")


'''
17. Bonus Calculator
•	Task: Take salary and years of service as input from the user and 
find the bonus amount if service is more than 5 years.

Rule
----
bonus is  20%
'''

# Salary = int(input("Enter  Salary  : "))
# Service =  int(input("Enter Years of Service : "))
#
# if Service >= 5 :
#     print(" bonus Amount" , (Salary* 20)/100)
# else:
#     print("No Bonus,has your Service is not completed 5 yrs")

'''
18. Perfect Number Checker
•	Task: Take a number as input from the user and find whether it is a perfect number or not.

'''
# Number = int(input("enter a valid Number: "))
# Perfect_Number = 0
#
# for each in range(1,Number) :
#     if Number % each == 0  :
#         Perfect_Number += each
#
# if Perfect_Number == Number :
#     print("Its a Perfect Number")
# else:
#     print("Its Not a Perfect Number")

'''
19. Reverse a String
•	Task: Take a string as input from the user and find its reverse without using built-in functions.

'''

# Name = input("Enter your Name: ")
# Reverse = ""
# for i in Name:
#     Reverse = i + Reverse
# print(Reverse)


'''
20. Matrix Multiplication
•	Task: Take two matrices as input from the user and find their multiplication result.
'''

First_Matrix = input("Enter valid First Matrix : ")
Second_Matrix = input("Enter valid Second Matrix : ")

B = list(First_Matrix)

#A = First_Matrix * Second_Matrix
print(B)