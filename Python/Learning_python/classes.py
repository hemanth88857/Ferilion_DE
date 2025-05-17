from typing import Any


# class student_details:
#     name = "ramu"
#
#
# Student = student_details()
# #student_details.name = "akhul"
#
# print(student_details.name)



class student_details:

    def __init__(self,name,batch):
        self.name = name
        self.batch = batch

#
# Students = student_details("","")
# Students.name = "rajun"
# Students.batch = "CSEt"
#
# print(Students.batch)


class Cooking:

    def __init__(self,foodname,type):
        self.foodname = foodname
        self.type = type

    def taste(self):
        print("its an indian food",self.foodname,self.type)






class Transport :

    def __init__(self,vechile_name:str , vechile_no:Any):
        self.vechile_name = vechile_name
        self.vechile_no = vechile_no

    def __str__(self):
        return f"{self.vechile_name},{self.vechile_no}"





