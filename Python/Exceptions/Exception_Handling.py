import  logging
# from Python.log_create.log_creation import log_creation_func,log_creation_file,get_logger
from Python.log_create.New_log_create import logger


# logger = get_logger()
# log = get_logger()
# EXE_logger = log_function()
# EXE_logger = logging.getLogger("mylogger")
# log = log_creation_func()

print(logger)
try :
    a = 10/9
except Exception as exe:
    logger.error("An exception %s", exe)
    print(exe)
else:
    logger.info(f"alog as {a}")



#
# try:
#
#     x = int(input("enter a value:"))
#     y = 10/x
# except Exception as e:
#     print(f"error is {e}")
# except ValueError as v :
#     print(f"error is :{v}")
# else:
#     print(f"resutls : {y}")
# finally:
#     print("Always runs")
#
#



# ✅ Example: Handling FileNotFoundError

#
# try:
#     file = open("data.txt", "r")
#     content = file.read()
#     print(content)
# except FileNotFoundError:
#     print("File not found. Please check the filename.")
# finally:
#     print("File operation complete.")
#
#
# # You can create your own exception class by inheriting from Exception.
#
# class AgeTooSmallError(Exception):
#     pass
#
# age = int(input("Enter your age: "))
#
# try:
#     if age < 18:
#         raise AgeTooSmallError("You must be at least 18 years old.")
#     print("Access granted.")
# except AgeTooSmallError as e:
#     print("Custom Exception:", e)
#
