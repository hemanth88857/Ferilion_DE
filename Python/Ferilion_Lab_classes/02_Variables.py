'''

 Assigning value to multiple variables. Explain
 . x = 10. Explain in detail for CRUD operations


 operator
 Subtract 2 numbers and print result program.
6. Write down all scenarios with different input values using all the operators


DM

3. Prepare Programs for below questions
	1. Prepare state and assign North South West East
	    north = []
		south = ['Andhra Prades', 'Telangana', 'Karnataka','Tamil Nadu', 'Kerala']
		west = []
		east = []
	2. Prepare dictionary with key as state name and value as "list of districts"
4. Get employee details(in dict format, empid,name,sal, exp) and update hike for employee with below
		If exp is 0 to 2 years - 10% Hike
				  2 to 5 years - 20% Hike
				  5 to 8 years - 30% Hike
				  8+           - No hike




				  loop
				  --------
- Between 1 to 100
    1. Print all numbers
    2. Print even numbers
    3. Print odd numbers
    4. Print all prime numbers
    5. Print numbers with power of 2 (1 2 4 8 16 32 64)
    6. Print all numbers which are divisible by 5 and 7
    7. Print all numbers which are divisible by 4 or 6
    8. Print first 14 odd numbers
    9. Print first 23 even numbers
   10. Print first 6 numbers which are divisible by 4 and 6
   11. Print all numbers except divisible by 9
   12. Write for loop to explain all data structures.
'''


# def count_substring(string, sub_string):
# #     count_string = []
# #     i = ""
# #     for each in string:
# #         if sub_string in i:
# #             count_string.append(sub_string)
# #         i += each
# #
# #     return len(count_string)
# #
# #
# # if __name__ == '__main__':
# #     string = "ininini"
# #     sub_string = "ini"
# #
# #     count = count_substring(string, sub_string)
# #     print(count)

# print(0.1 + 0.2)











class Animal:
    def __init__(self,password):
        self.password = password

    def get_details(self):
        return self.password

    @property
    def password(self):
        return self._password


obj1 = Animal("12345")
print(obj1.password)
print(obj1.get_details())


obj1.password = "3455"
print(obj1.password)
