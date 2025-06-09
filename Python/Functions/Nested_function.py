

# x= 300
# def func():
#     x = 200
#
#     return x
#
# print(func())


# x = 300
#
# def outerfunc():
#     x = 200
#     def innerfunc():
#         x= 100
#         return x
#     innerfunc()
#     return x
#
# print(outerfunc()) # 200




# x = 300
#
# def out():
#     x = 100
#     # print(x)
#     def inn():
#         print(x)
#     inn()
#     # return inn
# out()


# global


# x =300
#
# def out():
#     global x
#     x = 200
#     def inn():
#         print(x)
#     inn()
#
# out()


#non local

# y = 600
# x = 500
# def out():
#     # x = 500
#     def inn():
#         nonlocal x
#         # x = 200
#         print(x,y)
#     inn()
# out()
#


# global lets you access or modify a variable defined outside all functions.
#
# nonlocal lets you access or modify a variable in the outer (enclosing) function, not in global scope.
#
#


# ✅ 1. Authentication System (Closure)

"""
Requirement:
Create a function login_system() that takes a username and password.
 Inside it, define a nested function check_credentials() that validates the input.
"""

# def login_system(username,password):
#
#     def check_credentails():
#         if username == "hemanth" and password == "123":
#             return "login Successfull"
#         return "invalid credntails"
#     check_credentails()
#     return check_credentails()
#
# print(login_system("hemanth","123"))
#
#
# def login_system2(username,password):
#
#     def check_credentails():
#         if username == "hemanth" and password == "123":
#             return "login Successfull"
#         return "invalid credntails"
#     check_credentails()
#     return check_credentails()
#
# print(login_system2(input("Username:"),input("password:")))



"""

 1. Calculator with Custom Operations
Requirement:

Create a function calculator() that takes two numbers.
Inside it, define nested functions for add(), subtract(), multiply(), and divide().
Based on a string input (e.g., "add"), return the result from the appropriate nested function.
"""

#
# def calculator(type,x,y):
#     def add(x, y):
#         return x + y
#
#     def sub(x, y):
#         return x - y
#
#     def mul(x, y):
#         return x * y
#
#     def div(x, y):
#         return x / y
#
#     if type.lower() == "add":
#         return add(x,y)
#
#     if type.lower() == "sub":
#         return sub(x,y)
#     if type.lower() == "mul":
#         return  mul(x,y)
#
#     if type.lower() == "div":
#         return div(x,y)
#
#
# print(calculator("add",5,10))



"""
User Greeting with Access Level
Requirement:
Define a function user_profile(name, access_level) that returns a greeting() function.
The nested function should greet the user differently based on access level (admin, editor, viewer).
"""


#
# def user_profile(name,access_level):
#
#     def admin():
#         return f"hi {name} , please change the admin password"
#     def editor():
#         return f"hi {name} , please change the editor password"
#     def viewer():
#         return f"hi {name} , please change the login password"
#
#
#     if access_level.lower() == "admin":
#         return admin()
#     if access_level.lower() == "editor":
#         return editor()
#     if access_level.lower() == "viewer":
#         return viewer()
#
#
#
# print(user_profile("hemanth","admin"))


"""
Password Validation System
Requirement:

Write a function password_checker(password) that contains:
A nested function to check length.
A nested function to check for digits and special characters.
A nested function to check for uppercase and lowercase letters.
Return True only if all conditions are met.

"""

# def password_checker(password):
#
#     def password_lenth():
#         return len(password)  == 8
#
#     def digits_specialchar():
#         spl = ["!","@"]
#         digit = any(char.isdigit() for char in password)
#         spl_char = any(char in spl for char in password)
#
#         return digit and spl_char
#
#     def upper_lower():
#
#         upper = any (char.isupper() for char in password )
#         lower = any (char.lower() for char in password)
#         val = upper and lower
#         return val
#
#
#     return password_lenth() and digits_specialchar() and upper_lower()
#
# print(password_checker("@Bs!2345"))


"""
✅ 4. Discount Generator
Requirement:

Create a function discount_generator(discount_percent) that returns a nested function.
The nested function should take an original price and apply the discount.
Use the outer function to configure the discount rate and reuse the inner one.

"""

def discount_generator(discount_percent):

    def apply_discount(original_price):
            price = (original_price*discount_percent)/100
            return price

    return apply_discount

# Create a 10% discount function
ten_percent_discount = discount_generator(10)

print(ten_percent_discount)

# # Apply it to a price
# print(ten_percent_discount(200))  # Output: 180.0
#
# # Create a 25% discount function
# twentyfive_discount = discount_generator(25)
# print(twentyfive_discount(400))  # Output: 300.0
