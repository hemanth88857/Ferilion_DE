from Learning_python.classes import student_details
from Learning_python.classes import Cooking
from Learning_python.classes import Transport

name = 'Hema nth'
age = 31
salary = 96450.80

#print(name,age,salary)


# collage = student_details("","")
# collage.name = "ksr"
# print(collage.name)


#
# menu = Cooking("","")
# menu.foodname = "briyani"
# menu.type = "nonveg"
#
# menu.taste()








Travelling = Transport("","")
Travelling.vechile_name = "bus"
Travelling.vechile_no = "TS09 fj7642"


print(Travelling)

VechileNameData = []
VechileNoData = []

VechileNameData.append(Travelling.vechile_name)
VechileNoData.append(Travelling.vechile_no)
print(VechileNameData)
print(VechileNoData)

Travelling.vechile_name = "lorry"
Travelling.vechile_no = "HR fj7642"

VechileNameData.append(Travelling.vechile_name)
VechileNoData.append(Travelling.vechile_no)
print(VechileNameData)
print(VechileNoData)


Travelling.vechile_name = "auto"
Travelling.vechile_no = 89776

VechileNameData.append(Travelling.vechile_name)
VechileNoData.append(Travelling.vechile_no)
print(VechileNameData)
print(VechileNoData)





x,y,z = [12,12],"f",8

