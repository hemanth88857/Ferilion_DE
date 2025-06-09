import  logging
from Python.log_create.log_creation import log_creation_func,log_creation_file,get_logger
from Python.log_create.New_log_create import logger
# import log_module
# logger = log_creation_file("ecx_logs.log")



try:
    file_path = r"C:\Users\Dell\Desktop\Azure data\lo-doc.txt"

    with open(file_path,mode="r") as file6:
        context  = file6.read()
        print(context)
        logger.info("sucessful")
except FileNotFoundError as f:
    logger.info(f)
    print(f)



"""


reading,writing, deleting,creation


#actions
read - r
write - w  ----- truncate existing content and add new content
append = a ------ add content to existing context
read & write r+
write read w+ ----- truncate  exiting content and add new content

create - x

# flow
open()
Actions
Close()



"""

# file = open('sample.txt',mode='r')
# print(file.read())
# print(file.readline())
# file.close()


# file1 = open("sample.txt",mode='w')
# file1.write("i hace addde to new content ")
# file1.close()


# file3 = open("sample.txt",mode='a')
# file3.write("/n addded extra things to file")
# file3.close()

#
# file3 = open("sample.txt",mode='r+')
# print(file3.read(20))
#
# # file3.write("/n They encapsulate data (attributes) and behavior (methods) ")
# # print(file3.read())
# file3.close()


# file4 = open(r"C:\Users\Dell\Desktop\Azure data\long-doc.txt", mode='r')
# print(file4.read())
# file4.close()
#
# file4 = open("C:\\Users\Dell\Desktop\Azure data\long-doc.txt", mode='r')
# print(file4.read())
# file4.close()


# file_path = r"C:\Users\Dell\Desktop\Azure data\long-doc.txt"
# #
# with open(file_path,mode="r") as file5:
#     context = file5.read()
#     print(context)



