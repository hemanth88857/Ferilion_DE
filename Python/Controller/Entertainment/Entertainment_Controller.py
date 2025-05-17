from Classes.ClassObjects.Entertainment_Class import Movie

# eventpayment = Event_Booking.payment_status("Done")
#
# """# random_number = random.randint(0, 5)
# # print(random_number)
# # bookingid = Event_Booking.create_booking_id("79879")
# # print(bookingid)
# """
#
# if eventpayment.lower() == "done":
#     random_number = random.randint(0, 5)
#
#     if random_number >= 1:
#         Event_Booking.create_booking_id(str(random_number))
#         print(f"bookingid : {Event_Booking.create_booking_id(str(random_number))}")
#         b1 = Event_Booking("IPL","15/05/2025","3","3000","UPI","13/05/2025",Event_Booking.create_booking_id(str(random_number)),eventpayment)
#         print(b1.payment_message)
#
#     else:
#         print(f" payment done but booking failed")
#
# for each in Event_Booking.total_bookings:
#     print(each.booking_details())
#     print(each.ticketquantity)

# b1 = Event_Booking("IPL", "15/05/2025", "3", "3000", "UPI", "13/05/2025","","")
# b1.paymentstatus = "done"
# print(b1.eventname,b1.bookingdate,b1.paymentstatus)
# print(b1.booking_details())
# print(Event_Booking.total_bookings)
# print(Event_Booking.payment_status("Done"))
# print(Event_Booking.create_booking_id("5"))
# print(b1.paymentstatus)
#



"""----------------------------------------------------------------------------------------------------------------"""

"""Movie"""
movie1 = Movie("Dragon","Asian","Morning show","3","1500")
print(movie1.movie_details()) # instance method
print(movie1.complete_Movie_details())
print(Movie.total_booking) # class Variable
print(Movie.movie_ott("JIO")) # class method
print(Movie.movie_rating("5")) # static method
print(movie1.booking_message) # property method

