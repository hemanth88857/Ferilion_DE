from tkinter.font import names

class Access:

    _class_access_protected_variable = "class_Access_protected_variable"
    __class_access_private_variable = "class_Access_private_variable"
    class_variable = "class_variable"

    def __init__(self,name,age,hike,salary):
        self.name  = name
        self.age = age
        self._hike = hike
        self.__salary = salary
    def emp_details(self):
        print(f"name :{self.name}, age:{self.age} , hike :{self._hike}, salary :{self.__salary}\n")
        return (f"name :{self.name}, age:{self.age} , hike :{self._hike}, salary :{self.__salary}\n"
                f" class_access_protected_variable---> {self._class_access_protected_variable}\n"
                f" class_access_private_variable---> {self.__class_access_private_variable}\n"
                f"class variable---> {self.class_variable}")
        # return f"name :{self.name}, age:{self.age}, salary :{self.__salary} "



    @classmethod
    def __salarydetails(cls):
        return ( f" class_access_protected_variable---> {cls._class_access_protected_variable}\n"
                f" class_access_private_variable---> {cls.__class_access_private_variable}\n"
                f"class variable---> {cls.class_variable}")

    @classmethod
    def _hikedetails(cls):
        return (f" class_access_protected_variable---> {cls._class_access_protected_variable}\n"
                f" class_access_private_variable---> {cls.__class_access_private_variable}\n"
                f"class variable---> {cls.class_variable}")


    @property
    def names(self):
        return f"pavannnnnnn"


    @property
    def salary(self):
        return self.__salary  # Read-only access

    @salary.setter
    def salary(self, sal_val):
        self.__salary = sal_val  # Read & Write  access






class AccessControl(Access):

    _class_accessControl_protected_variable = "class_accessControl_protected_variable"
    __class_accessControl_private_variable = "class_accessControl_private_variable"

    def __init__(self,dept,project,leaves,complains,name,age,hike,salary,):

        Access.__init__(self,name, age, hike,salary)
        # super().__init__(self,name, age, hike)


        self.dept = dept
        self.project = project
        self._leaves = leaves
        self.__complains = complains


    # def emp_full_details(self):
    #     return f"name :{self.name}, age:{self.age}, salary :{self.__salary} , hike :{self._hike}"

    def emp_details(self):
        super().emp_details()
        return f"dept :{self.dept}, project:{self.project} , leaves :{self._leaves}, complains :{self.__complains}"



#parent
obj1 = Access("hemanth","31","45%","1500000")
# print(f"ojb1 ---{obj1._class_access_protected_variable}")
# print(f"ojb1 ---{obj1.__class_access_private_variable}")
# print(f"ojb1 ---{obj1._Access__class_access_private_variable}")
# print(obj1.emp_details())
# #

print(obj1.salary)
obj1.salary = "6786876"
print(obj1.emp_details())


# # child
# obj2 = AccessControl("mani","31","5","500000","v2","32","3","9")
# # print(f"ojb2 ---{obj2._class_access_protected_variable}")
# # print(f"ojb2 ---{obj2._AccessControl__class_access_private_variable}")
# # print(f"ojb2 ---{obj2._Access__class_access_private_variable}")
#
# obj2 = AccessControl("IT","lnt","5","4","v2","32","3","954543")
# # #
# print(obj2.emp_details())
# # print(obj2._Access__salarydetails)
# print(obj2._hikedetails())
# #
# #
# #

