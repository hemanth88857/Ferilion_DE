

from pkg1.file1 import username






# with out parameters



# def decorator_name(func):
#     def wrapper():
#         print("hellow")
#         func()
#         print("have a nice day")
#
#     return wrapper
#
#
# @decorator_name
# def name():
#     print(f"Hi , how are you today ")
#


# name()

# with  parameters


# def decorator_add(func):
#     def wrapper(*args):
#         print("before")
#         result = func(*args)
#         print("after")
#         return  result
#     return wrapper
#
# @decorator_add
# def additn(x,y):
#     z = x+y
#     return z
#
#
# print(additn(5,8))
#


def decorator_mul(func):
    def wrapper(*args):
        print("before")
        result = func(*args)
        print("after")
        return result
    return wrapper

@decorator_mul
def mul(x,y):
    return x*y

print(mul(2,10))


# Higher-Order Functions

# pass a function as an arugiment to another function and retunns the result


def greet():
    return " ferilion"

def whis(f):
    return f"ypu have jined in {f}"

print(whis(greet()))



def func(x,y):
    return x(y)


def mul(x):
    return x*x

print(func(mul,5))
