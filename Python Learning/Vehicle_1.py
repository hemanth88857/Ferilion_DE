class Vehicle:
    vehicle_count  = 0
    def __init__(self, brand, engine_type, chassis_number):
        self.brand = brand                       # Public
        self._engine_type = engine_type          # Protected
        self.__chassis_number = chassis_number   # Private
        Vehicle.vehicle_count += 1

    def get_details(self):
        return f"vehicle brand is {self.brand} + vehicle engine type is {self._engine_type} and "

    def _get_protected_engine_details(self):
        return f"Engine type is :{self._engine_type} - protected"

    def __get_private_chassis(self):
        return f"chassis Number : {self.__chassis_number} - private"

    @classmethod
    def get_vehicle_count(cls):
        return cls.vehicle_count

    @property
    def chassis_number(self):
        return self.__chassis_number

    @staticmethod
    def is_electric(engine_type):
        return engine_type.lower() == "electric"

    @property
    def engine_type(self):
        return self._engine_type


class Car(Vehicle):
    def __init__(self, brand, engine_type, chassis_number, model, mileage):
        super().__init__(brand, engine_type, chassis_number)
        self.model = model
        self._mileage = mileage

    def get_details(self):
        base = super().get_details()
        return f"{base}, Model: {self.model}, Mileage: {self._mileage} kmpl"

    def get_mileage(self):
        return self._mileage

    def _get_increase_mileage(self, additional_mileage):
        self._mileage += additional_mileage


# Create objects
v1 = Vehicle("Honda", "Petrol", "CH1234")
c1 = Car("Toyota", "Electric", "CH5678", "Corolla", 30)
#
# # Inheritance + Method Overriding
print(c1.get_details())  # Car-specific details
print(v1.get_details())  # Base vehicle details

# Access protected and private info (for demo only)
print(c1.get_mileage())
c1._get_increase_mileage(5)
print(c1.get_mileage())
#
# # Class method to count vehicles
print("Total vehicles:", Vehicle.get_vehicle_count())
#
# # Static method
print("Is Electric?", Vehicle.is_electric(c1.engine_type))

 # Property usage
print("Chassis Number (Car):", c1.chassis_number)

