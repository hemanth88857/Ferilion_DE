
from ConstantData import Students_Data
from Classes.ClassObjects.School_Class import Students



students_Com_data = []
for each in Students_Data.students:
    details = Students(each["name"],each["email"])
    students_Com_data.append(details)


# for each in students_Com_data:
#     print(each.course)
#

student1 = Students("ramu","bhemanth@gmal.com")
student1.enroll(input("please enter curses: "))
student1.enroll("De")
print(student1.student_details())
student1.complete_course("De")
print(student1.student_details())

print(student1.check_valid_email("bhemanth@gamil.com"))
