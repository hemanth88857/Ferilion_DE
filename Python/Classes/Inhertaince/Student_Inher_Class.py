
#Single Inheritance -- parent
class StudentInherit:

    def __init__(self, name, age,gender):
        # Instance variables unique to each instance
        self.name = name
        self.age = age
        self.gender = gender

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, gender: {self.gender}"


    def is_adult(self):
        return self.age >= 18

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name_val):
        if not isinstance(name_val , str):
            raise TypeError("Name should be String")
        self._name = name_val


    @property
    def age(self):
        return self._age

    @age.getter
    def age(self):
        return self._age

    @age.setter
    def age(self,age_val):
        if age_val >= 100 or  not isinstance(age_val,int) :
            raise TypeError("Enter a valid age")
        self._age = age_val

    # @age.setter
    # def age(self, age_val):
    #
    #     if age_val >= 100 or not isinstance(age_val, int):
    #         raise TypeError("Enter a valid age")
    #     # elif age_val >= 100 :
    #     #     raise TypeError("Enter a  age below 100")
    #     # else:
    #     self._age = age_val

#Single Inheritance -- child
class Person(StudentInherit):

    def __init__(self,name, age,gender,student_id,marks,course):
        super().__init__(name,age,gender)
        self.student_id = student_id
        self.marks = marks
        self.course = course

    def display_student_info(self):
        general = self.get_details()
        return (f"{general} student_id: {self.student_id} "
                f"marks: {self.marks} "
                f"course: {self.course} "
                f"is_adult : {"yes" if self.is_adult() else "No" } "
                f"status : {"passed" if self.has_passed() else "Fail"}")

    def has_passed(self):
        return self.marks >= 40





# #Multiple Inheritance -- parent

class Student_Multiple_Inheritance:

    def __init__(self,student_id,marks,course):

        self.student_id = student_id
        self.marks = marks
        self.course = course



    def get_student_details(self):

        return f"Student Id : {self.student_id} , Marks : {self.marks} , Course :{self.course}"




class Teacher:

    def __int__(self,employee_id,subject):
        self.employee_id = employee_id
        self.subject = subject

    def display_teacher_info(self):
        return f"employee_id : {self.employee_id} , subject : {self.subject} "


    def teach(self):
        return f" subject : {self.subject} "


class TeachingAssistant(Student_Multiple_Inheritance,Teacher):

    def __init__(self,name,student_id,marks,course,employee_id,subject):

        Student_Multiple_Inheritance.__init__(self,student_id,marks,course)
        Teacher.__int__(self,employee_id,subject)
        self.name = name

    def display_full_info(self):
        teacher = self.display_teacher_info()
        student = self.get_student_details()

        return (f"Name : {self.name}, "
                f"{teacher}, "
                f"{student}."
                )

    def assist(self):

        return f"{self.subject} will be teach by {self.name}"