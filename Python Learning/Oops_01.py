class Car:
    def __init__(self, make, model):  # Reference to the object/instance
        self.make = make              # Instance variables
        self.model = model

    def get_car_details(self):        # instance method
        return f"Car Make is {self.make}, Model is {self.model}"

    def __str__(self):
        return f"{self.make} {self.model}"

    def top_speed(self, speed):
        return f" for make {self.make} model is {self.model} the top speed is {self.speed}"

# Creating instances/object of the Car class
obj1 = Car(make="TATA", model="NEXON")
print(obj1)                             # This will use the __str__ method (called by object)

obj2 = Car(make="HONDA", model="CITY")
print(obj2)                             # This will use the __str__ method (Called by object)
obj1.speed = 100
obj2.speed = 120
# Calling the get_car_details method
# print(obj1.get_car_details())
# print(obj2.get_car_details())
# print(obj1.top_speed(speed= 100))
# print(obj2.top_speed(speed = 120))

