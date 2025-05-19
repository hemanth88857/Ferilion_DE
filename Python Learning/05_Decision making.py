#1. Check if a Rectangle is a Square

# length = int(input("Enter the length: "))
# breadth = int(input("Enter the breadth: "))
# if length == breadth:
#     print("It is a square.")
# else:
#     print("It is a not a square")

#2. Check Case of Entered Character
# Task: Take a single character as input from the user and find whether it is uppercase or lowercase.
# char = input("Enter a character: ")
# if char == char.upper():
#     print("It is a uppercase")
# elif char == char.lower():
#     print("It is a lowercase")
# else:
#     print("Enter a valid character")

# # 3. Check if Number is Positive or Negative
# # •	Task: Take a number as input from the user and  find whether it is positive or negative.
# Num = int(input("Enter a number: "))
# if Num > 0:
#     print("It is a positive number")
# elif Num < 0:
#     print("It is a negative number")
# else:
#     print("Enter a valid type numbers")

# 4. Floating Point Number Classification
# •	Task: Take a floating-point number as input from the user and find whether
# it is zero, positive, or negative. Also determine if it is small (absolute value < 1) or large (absolute value > 1,000,000).

# Num = float(input("Enter a floating point number: "))
# if Num == 0:
#     print("It is a zero")
# elif Num > 0 or Num < 1 or Num > 1000000:
#     print("It is a positive")
# elif Num < 0:
#     print("It is a negative")

# 5. Weekday from Number
# •	Task: Take a number between 1 to 7 as input from the user and find the corresponding weekday name.
#
# weekdays = int(input("Enter a weekday number: "))
# weeks = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",'Sunday']
# if weekdays > 0 and weekdays <= 7:
#     for num in range(1,len(weeks)+1):
#         if weekdays == num:
#             print(weeks[weekdays-1])
# else:
#     print('Enter a valid number from 1 to 7')

# 6. Vowel or Consonant Checker
# •	Task: Take a single alphabet character as input from the user and
# find whether it is a vowel or consonant.
#
# x =input("Enter a character: ")
# if (x == 'a' or x == 'e' or
#         x == 'i' or x == 'o' or x == 'u'):
#     print("It is a Vowel")
# elif (x == 'A' or x == 'E' or
#         x == 'I' or x == 'O' or x == 'U'):
#     print("It is a Vowel")
# elif ( x != 'A' or x != 'E' or
#         x != 'I' or x != 'O' or x != 'U'):
#     print("It is a consonants")
# elif (x != 'a' or x != 'e' or
#         x != 'i' or x != 'o' or x != 'u'):
#     print("It is a Consonants")
# else:
#     print("Enter a valid characters")

# 7. Cube Display up to a Given Number
# •	Task: Take an integer as input from the user and find the cube of all numbers up to that integer.

# num = int(input("Enter an integer: "))
#
# # Iterate from 1 to the entered number
# for i in range(1, num + 1):
#     # Check if the current number is less than or equal to the limit
#     if i <= num:
#         cube = i ** 3  # Calculate the cube
#         print(f"Number is: {i} and cube is: {cube}")
#     else:
#         print(f"{i} is beyond the specified num.")

# 8. Sum of N Odd Natural Numbers
# •	Task: Take a number n as input from the user and find the sum of first n odd natural numbers.

# num = int(input("Enter a positive integer: "))
# sum = 0
# for i in range(1, num + 1):
#     if i % 2 != 0:
#     sum += i
# print(sum)
# else:
#     print("Enter valid number");


# 9. Order of Three Numbers
# # •	Task: Take three numbers as input from the user and find whether they are in increasing, decreasing, or neither order.
#
# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# c = int(input("Enter the third number: "))
#
# # Check if the numbers are in increasing order
# if a < b < c:
#     print("The numbers are in increasing order.")
# elif a > b > c:
#     print("The numbers are in decreasing order.")
# else:
#     print("The numbers are in neither increasing nor decreasing order.")

# 10. Descending Order of Names
# •	Task: Take three names as input from the user and find their order in descending alphabetical order.

# # Prompt the user to enter three names
# name1 = input("Enter the first name: ")
# name2 = input("Enter the second name: ")
# name3 = input("Enter the third name: ")

# Compare and determine the descending order using conditional statements
# if name1 >= name2 and name1 >= name3:
#     if name2 >= name3:
#         print("Names in descending order:")
#         print(name1)
#         print(name2)
#         print(name3)
#     else:
#         print("Names in descending order:")
#         print(name1)
#         print(name3)
#         print(name2)
# elif name2 >= name1 and name2 >= name3:
#     if name1 >= name3:
#         print("Names in descending order:")
#         print(name2)
#         print(name1)
#         print(name3)
#     else:
#         print("Names in descending order:")
#         print(name2)
#         print(name3)
#         print(name1)
# else:
#     if name1 >= name2:
#         print("Names in descending order:")
#         print(name3)
#         print(name1)
#         print(name2)
#     else:
#         print("Names in descending order:")
#         print(name3)
#         print(name2)
#         print(name1)

# 11. Telephone Bill Calculator
# •	Task: Take number of calls made as input from the user and find the total telephone bill.
#
# calls = int(input("Enter the total number of calls made: "))
#
# call_charges = 0
#
# if calls <= 50:
#     call_charges = 0
# elif calls <= 150:
#     call_charges = (calls - 50) * 2
# elif calls <= 350:
#     call_charges = (100 * 2) + (calls - 150) * 1.5
# else:
#     call_charges = (100 * 2) + (200 * 1.5) + (calls - 350) * 1
#
# print(f"Total Calls Made: {calls}")
# print(f"Call Charges: ₹{call_charges:.2f}")

# 12. Leap Year Checker
# •	Task: Take a year as input from the user and find whether it is a leap year or not.
#
# year = int(input("Enter a year: "))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(" It is a Leap year")
# else:
#     print("Not a leap year")

# 13. Find the Largest of Three Numbers
# •	Task: Take three numbers as input from the user and find the largest number.
#
#
# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter a number: "))
# num3 = int(input("Enter a number: "))
#
# if (num1 >= num2) and (num1 >= num3):
#    largest = num1
# elif (num2 >= num1) and (num2 >= num3):
#    largest = num2
# else:
#    largest = num3
# print("The largest number is", largest)

# Python program to check if the input number is odd or even.
# A number is even if division by 2 gives a remainder of 0.
# If the remainder is 1, it is an odd number.

# num = int(input("Enter a number: "))
# if (num % 2) == 0:
#    print("{0} is a Even".format(num))
# else:
#    print("{0} is s Odd".format(num))

# 15. Exam Eligibility Based on Attendance
# Task: Take number of classes held and number of classes attended as input from the
# user and find the attendance percentage and whether the student is allowed to sit in the exam.

# Classes_held = int(input("Enter a number of classes held: "))
# Classes_attended = int(input("Enter a number of classes attended: "))
#
# if Classes_held <= 50:
#     print("Student is not allowed to sit in the Exam Hall")
# else:
#     # Calculate attendance percentage
#     attendance_percentage = (Classes_attended / Classes_held) * 100
#     print(attendance_percentage)
#     if attendance_percentage >= 50:
#         print("Student is allowed to sit in the Exam Hall")
#     else:
#         print("Student is not allowed to sit in the Exam Hall")

# 16. Grade Calculator
# •	Task: Take marks as input from the user and find the corresponding grade based on predefined rules.

# Marks = int(input("Enter the marks: "))
# if Marks <= 35:
#     print("Student grade is D")
# elif Marks <=60:
#     print("Student grade is C")
# elif Marks <=80:
#     print("Student grade is B")
# elif Marks <=100:
#     print("Student grade is A")
# else:
#     print(" Please enter the valid marks")
#
# 17. Bonus Calculator
# •	Task: Take salary and years of service as input from the user and
# find the bonus amount if service is more than 5 years.

# salary = float(input("Enter your salary: "))
# years_of_service = int(input("Enter your years of service: "))
#
# if years_of_service > 5:
#     bonus = 0.05 * salary
#     print("Bonus Amount is",bonus)
# else:
#     print("No bonus awarded for this employee.")


"""18. Perfect Number Checker
# •	Task: Take a number as input from the user and find whether it is a perfect number or not."""

# num = int(input("Enter a number: "))
# sum_of_divisors = 0
# for i in range(1, num):
#     if num % i == 0:
#         sum_of_divisors += i
# if sum_of_divisors == num:
#     print("It is a Perfect Number.")
# else:
#     print("It is not a Perfect Number.")

# 19. Reverse a String
# •	Task: Take a string as input from the user and find its reverse without using built-in functions.
# name = input("Enter a name: ")
# s = "GeeksforGeeks"
# rev = ""
# for ch in name:
#     rev = ch + rev
# print(rev)

