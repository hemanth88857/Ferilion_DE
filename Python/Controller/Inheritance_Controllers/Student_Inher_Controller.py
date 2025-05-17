from Classes.Inhertaince.Student_Inher_Class import Person,StudentInherit,TeachingAssistant

#single inheritance

# Creating a Student object
student1 = Person("Rahul", 20, "Male", "S123", 98, "maths")

# print(student1.display_student_info())
# print(student1.get_details())




# # Another example
# print(student2.display_student_info())
# student2 = Person("Priya", 16, "Female", "S124", course= "social",marks=35,)




#mutliple inheritance


ta = TeachingAssistant("Aditi", "S101", "Data Structures", 82, "T202", "Python Programming")

print(ta.display_full_info())
print(ta.teach())
print(ta.assist())


