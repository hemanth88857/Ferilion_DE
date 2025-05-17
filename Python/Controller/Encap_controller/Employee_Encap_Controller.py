from Classes.Encap.Employee_Encap import Employee,Staff

employee1 = Employee("prmonth","25",9898)

# print(getattr(employee1,"name"))
# setattr(employee1,"name","hemanth kumar")
# print(hasattr(employee1,"name"))


# employee1.name = "mani"
# employee1.name = 100
# setattr(employee1 ,"age","56")
# print(employee1.salary)



staff1 = Staff("heanth","66","797979")

print(staff1.staff_details())
staff1._name = 100
staff1.info = ("200",78)
print(staff1._name)