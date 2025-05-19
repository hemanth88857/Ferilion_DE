class Vehicle:
    def __init__(self,brand, engine_type, chassis_number):
        self.brand = brand
        self._engine_type = engine_type
        self.__chassis_number = chassis_number

    def get_details(self):
        return "getting the car details"

    def _get_protected_engine_details(self):
        return f"return engine details"

