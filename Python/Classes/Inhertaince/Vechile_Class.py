

class Vehicle:
    def __init__(self,brand,year,model):
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self):

        return  f"{self.brand} {self.model} engine has started"

    def display_info(self):

         return f"brand : {self.brand}, model : {self.model}, and year:{self.year}"


class Car(Vehicle):

    def __init__(self,brand,year,fuel_type,seats,model):

        super().__init__(brand,model,year)
        self.fuel_type = fuel_type
        self.seats = seats


    def drive(self):
        return f"{self.brand} {self.model}  has started self Driving mode"

    def display_car_info(self):

        self.display_info()
        return f"fuel_type : {self.fuel_type}, seats : {self.seats}"


