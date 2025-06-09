

"""
1.Event Ticket Booking Form

variable: Attributes   : bookingID, userID, eventname, eventdate, seatCategory, ticketquantity, totalcost, paymentmethod, bookingdate, status  

"""


class Event_Booking: # class

    total_bookings = ["DRagaon"] # class variable
    
    def __init__(self,eventname, eventdate, ticketquantity, totalcost, paymentmethod, bookingdate,bookingid,paymentstatus): # instance variables
        self.eventname = eventname
        self.eventdate = eventdate
        self.ticketquantity = ticketquantity
        self.totalcost = totalcost
        self.paymentmethod = paymentmethod
        self.bookingdate = bookingdate
        self.bookingid = bookingid
        self.paymentstatus = paymentstatus
        Event_Booking.total_bookings.append(self)

    def booking_details(self):  # instance method
        return f"eventname : {self.eventname}, eventdate:{self.eventdate}, ticketquantity :{self.ticketquantity}, totalcost : {self.totalcost}, paymentmethod :{self.paymentmethod}, bookingdate :{self.bookingdate} , bookingid : {self.bookingid} , paymentstatus : {self.paymentstatus}"

    @classmethod  # class method
    def payment_status(cls, status):
        return status

    @staticmethod # static method
    def create_booking_id(booking_id):
        # t1 = Event_Booking.total_bookings
        return booking_id #,t1

    @property # property method
    def payment_message(self):
        # return "Booking Confirmed"
        return f"Payment status: {self.paymentstatus}"


 # def complete_details(self):
    #      return (f"instance variable :{self.eventname} \n"
    #              f"instance method    :{self.booking_details()}"
    #              f"class variable     :{Event_Booking.total_bookings}"
    #              f"class method       :{Event_Booking.payment_status("done")}"
    #              f"static method      :{self.create_booking_id(4)}"
    #              f"property method    :{self.paymentstatus}")


"""variable: Attributes   : reservationID, userID, movieName, theaterName, showTime, ticketQuantity, seatNumbers, totalCost, paymentMethod, bookingDate, status  
"""

class Movie:

    total_booking = 0 #class Variable

    def __init__(self,movieName, theaterName, showTime, ticketQuantity, totalCost,rating = "0"): #instant Variable

        self.movieName = movieName
        self.theaterName = theaterName
        self.showTime = showTime
        self.ticketQuantity = ticketQuantity
        self.totalCost = totalCost
        self.rating = rating
        Movie.total_booking += 1

    def movie_details(self): #instant method
        return f"movieName : {self.movieName}, theaterName : {self.theaterName}, showTime :{self.showTime}, ticketQuantity :{self.ticketQuantity}, totalCost : {self.totalCost} , rating : {self.rating}"

    @classmethod
    def movie_ott(cls,ott):
        return ott

    @staticmethod
    def movie_rating(rating):
        return rating

    @property
    def booking_message(self):
        return "Booking Successfully"

    def complete_Movie_details(self):
         return (f"instance variable :{self.movieName} \n"
                 f"instance method    :{self.movie_details()} \n"
                 f"class variable     :{Movie.total_booking} \n"
                 f"class method       :{Movie.movie_ott("AHA")}\n"
                 f"static method      :{self.movie_rating("5")}\n"
                 f"property method    :{self.booking_message}")