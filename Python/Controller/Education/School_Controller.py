from Classes.ClassObjects.School_Class import Student

# Creating an instance of Student
student1 = Student("Alice", 17)

"""
# Accessing instance method
print(student1.get_details())  # Output: Name: Alice, Age: 17, School: Green Valley High School

# Using class method to change class variable
Student.set_school_name("Sunrise Public School")
print(student1.get_details())  # Output: Name: Alice, Age: 17, School: Sunrise Public School

# Using static method
print(Student.is_adult(20))  # Output: True

# Accessing property
print(student1.name)  # Output: Alice

# Modifying property
student1.name = "Alicia"
print(student1.name)  # Output: Alicia

Student.school_name = "gotham"
print(Student.school_name)

"""


# getattr()
# setattr()
# hasattr()
# delattr()


res = getattr(student1,"name")
print(res)

res1 = getattr(student1,"_age")
print(res1)


setattr(student1,"_name","mani")
print(student1.name)

if hasattr(student1,"name"):
    print(student1.name)

# res1 = s