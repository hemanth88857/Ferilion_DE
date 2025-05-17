
class Employee:
    def __init__(self,name,salary,employee_id):
        self.name = name
        self.salary = salary
        self.employee_id = employee_id

    def display_info(self):

        return f"Name : {self.name} , Employee Id : {self.employee_id} , Salary : {self.salary}"

    def apply_raise(self,percent):

            if percent < 0 :
                return "NO hike"
            else:
                increment = self.salary * (percent / 100)
                self.salary += increment
                return f"salary hike by {percent}% , Salary incereased by {increment} and now salary is : {self.salary}"


class Manager(Employee):

    def __init__(self,name,salary,employee_id,department,team_size):

        super().__init__(name,salary,employee_id)
        self.department = department
        self.team_size = team_size

    def display_manager_info(self):
        self.display_info()
        return (f"department : {self.department},Teamsize : {self.team_size}")


    def approve_leave(self, employee_name):
        return  f"leave Applied by {employee_name} any approved by {self.name}"