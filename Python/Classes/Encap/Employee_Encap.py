
# class Employee:
#     def __init__(self,name,age,salary):
#         print("from init")
#         self.name = name
#         self.age = age
#         self.salary = salary
#
#     def employee_details(self):
#         return f"name : {self.name},age = {self.age} , salary = {self.salary}"
#
#
#     @property
#     def name(self):
#         print("from property")
#         return self._name
#
#     @name.getter
#     def name(self):
#         print("from getter")
#         return self._name
#
#
#     @name.setter
#     def name(self,name_val):
#         print("from setter")
#         if not isinstance(name_val,str):
#             raise  TypeError("name should be string")
#         self._name = name_val


class Employee:
    def __init__(self,name,age,salary:int):
        print("from init")
        self.name = name
        self._age = age
        self.salary = salary

    def employee_details(self):
        return f"name : {self.name},age = {self.age} , salary = {self.salary}"


    @property
    def name(self):
        print("from property")
        return self.k

    @name.getter
    def name(self):
        print("from getter")
        return self.k


    @name.setter
    def name(self,name_val):
        print("from setter")
        if not isinstance(name_val,str):
            raise  TypeError("name should be string")
        self.k = name_val


    @property
    def age(self):
        print("from property")
        return self._age

    @age.getter
    def age(self):
        print("from getter")
        return self._age


    @age.setter
    def age(self,age_val):
        print("from setter")
        if not isinstance(age_val,int):
            raise  TypeError("age should be int")
        self._age = age_val


    @property
    def salary(self):
        return self._salary


    @salary.setter
    def salary(self,sal_val):
        if not isinstance(sal_val,(int,float)):
            raise TypeError("salary should be int/float")
        self._salary = sal_val

    @salary.getter
    def salary(self):

        return self._salary


class Staff:
    def __init__(self,name,age,salary):
        self.name = None
        self.age = None
        self.info = (name,age)
        self.salary = salary

    def staff_details(self):
        return f"Name : {self._name} , Age : {self._age} , Salary : {self.salary}"


    @property
    def info(self):
        return {self._name,self._age}
    @info.getter
    def info(self):
        return {self._name,self._age}

    @info.setter
    def info(self,value):
        name_val,age_val = value

        if not isinstance(name_val,str):
            raise TypeError("Name should be string")
        self._name = name_val

        if int(age_val) < 18 :
            raise TypeError("age should be above 18")
        self._age = age_val