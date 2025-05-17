
class Ride:
    total_rides = 0
    Price_per_km = 10

    def __init__(self,rider_name,pickup_loc,drop_loc,distance_km):
        self.rider_name = rider_name
        self.pickup_loc = pickup_loc
        self.drop_loc =  drop_loc
        self.distance_km = distance_km
        self.fare = 0.0
        self.isCompleted = False
        Ride.total_rides += 1

        def display_ride_details(self):
            return  f"{self.rider_name},{self.pickup_loc},{self.drop_loc},{self.distance_km} , {self.fare},{self.iscompleted}"

        def calculate_fare(self,distance):
            if distance > 0 :
                self.fare = self.distance_km * Ride.Price_per_km
            else:
                return f"Distance must be greater than 0."

        def complete_ride(self):
            if not self.isCompleted:
              self.isCompleted = True
            else:
                return f"Ride in Progress"