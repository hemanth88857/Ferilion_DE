from Classes.ClassObjects.Hospital_Class import Hospital



"""Hospital"""
# patient = Movie("Dragon","Asian","Morning show","3","1500")
# print(movie1.movie_details()) # instance method
# print(movie1.complete_Movie_details())
# print(Movie.total_booking) # class Variable
# print(Movie.movie_ott("JIO")) # class method
# print(Movie.movie_rating("5")) # static method
# print(movie1.booking_message) # property method



patient = Hospital("Raju","25","M","Fever","13/05/2025","cash")
print(patient.patientName)# instance variables
print(patient.patient_details()) # instance method
print(Hospital.hospital_name) # class variables
print(Hospital.insurance_provider("Yes")) # class method
print(patient.patient_roomType("General")) # static
print(patient.patient_iddischarge)

if (Hospital.insurance_provider("Yes")).lower() == "yes":
    patient.paymentMethod = "Insurance"

print(patient.patient_details())


