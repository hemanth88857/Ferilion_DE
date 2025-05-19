# class Employee:
#     def __init__(self, name, age):
#         self.name = name   # instance variables
#         self.age  = age
#
#     def DisplayDetails(self):
#         print(self.name)
#         print(self.age)
#
# # Create an object of the class
# emp = Employee("Daniel", 30)
#
# # Access and print attributes
# print(emp.name)
# print(emp.age)
#
# # Or use the method calling
# emp.DisplayDetails()
#
# class Employee:
#     company = "TCS"  # Public class variable
#     __group = "TATA"  # Private class variable
#
#     def GetDetails(self):
#         self.name = input("Name: ")
#         self.__salary = input(self.name + " salary: ")
#         self.programming = input("Programming: ")
#
#
#     def Display(self):
#         print("Name:", self.name)
#         print("Salary:", self.__salary)
#         print("Programming is:", self.programming)
#         print(Employee.__group)
#
#
#     def RevisedSalary(self):
#         print("Existing salary:", self.__salary)
#         self.__salary = 75000
#         print("Revised salary:", self.__salary)
#
#     # @classmethod
#     # def clame(cls):
#     #     return cls.__group
#
# e = Employee()
# e.GetDetails()
# e.Display()
# print("Company:", e.company)  # Correct way to access public class variable
#
# # print("Group:", e.__group)
# # print(Employee.clame())
#
# e.RevisedSalary()  # Uncommented this to call the method


class Student:
    def __init__(self, name):
        self._name = name
        self._marks = 0

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, value):
        if value < 0 or value > 100:
            raise ValueError("Marks must be between 0 and 100")
        self._marks = value

# Using the Student class
student = Student("Rahul")

# Set valid marks
student.marks = 85
print(f"{student._name}'s marks:", student.marks)

# Try to set invalid marks
try:
    student.marks = 67
except ValueError as e:
    print("Error:", e)
