import re


class Student:
    # Class variable shared by all instances
    school_name = "Green Valley High School"

    def __init__(self, name, age):
        # Instance variables unique to each instance
        self._name = name
        self._age = age

    # Instance method: operates on the instance
    def get_details(self):
        return f"Name: {self._name}, Age: {self._age}, School: {Student.school_name}, {self.school_name}"

    # Class method: operates on the class
    @classmethod
    def set_school_name(cls, name):
        cls.school_name = name

    # Static method: utility function not dependent on class or instance
    @staticmethod
    def is_adult(age):
        return age >= 18

    # Property method: getter for 'name'
    @property
    def name(self):
        return self._name

    # Setter for 'name'
    @name.setter
    def name(self, new_name):
        self._name = new_name



class Book:

    def __init__(self,tittle,author):
        self.tittle = tittle
        self.author = author
        self.availability = True

    def book_details(self):
        return f"Tittle : {self.tittle} , Author : {self.author} , Available : {self.availability}"

    def borrow_book(self):
        if self.availability:
            self.availability = False
            print(f"You have borrowed '{self.tittle}'.")
        else:
            print(f"'{self.tittle}' is currently not available.")


    def return_book (self):
         self.availability = True
         # print(f"You have returned '{self.tittle}'.")

    @staticmethod
    def available(tittle):
        return tittle


class Students:

    student_count = 0

    def __init__(self,name,email):
        self.name = name
        self.course = []
        self.email = email
        Students.student_count += 1

    def student_details(self):

        return f"Student name : {self.name}, EmailId : {self.email} ,enroll :{self.course}, Enrolled Courses : {",".join(self.course) if self.course else None} "

    def enroll(self,course_name):
        self.course.extend(course_name.split(","))
        # self.course.append(course_name)

    def complete_course(self, course_name):

        if  course_name in self.course:
            self.course.remove(course_name)

    @classmethod
    def get_students_count(cls):
        return cls.student_count

    @staticmethod
    def check_valid_email(email):
        return re.match(r"[^@]+@[^@]+\.[^@]+",email) is not None






