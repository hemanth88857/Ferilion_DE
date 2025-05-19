class FinanceEntity:
    # Class variable
    industry = "Finance Sector"

    def __init__(self, name, sector, location):
        # Instance variables (with leading underscores to indicate 'private' variables)
        self._name = name
        self._sector = sector
        self._location = location

    # Property for name
    @property
    def name(self):
        print("Getting name...")
        return self._name

    @name.setter
    def name(self, value):
        print("Setting name...")
        self._name = value

    # Property for sector
    @property
    def sector(self):
        print("Getting sector...")
        return self._sector

    @sector.setter
    def sector(self, value):
        print("Setting sector...")
        self._sector = value

    # Property for location
    @property
    def location(self):
        print("Getting location...")
        return self._location

    @location.setter
    def location(self, value):
        print("Setting location...")
        self._location = value

    # Instance method
    def instance_method(self):
        print("Accessing instance variables:")
        print("Name:", self.name)
        print("Sector:", self.sector)
        print("Location:", self.location)
        print("Accessing class variable from instance method:", self.industry)

    # Class method
    @classmethod
    def class_method(cls):
        print("Accessing class variable from class method:", cls.industry)

    # Static method
    @staticmethod
    def static_method():
        print("This is a static method. It doesn't access instance or class variables.")

# Creating instances of the FinanceEntity class
entity1 = FinanceEntity("HDFC Bank", "Banking", "Mumbai")
entity2 = FinanceEntity("Bajaj Finance", "NBFC", "Pune")

# Accessing and modifying properties
print(entity1.name)
entity1.name = "HDFC Bank Ltd."
print(entity1.name)

# Calling instance method
entity1.instance_method()

# Calling class method
FinanceEntity.class_method()

# Calling static method
FinanceEntity.static_method()
