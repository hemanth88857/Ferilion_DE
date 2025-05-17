'''
-------------------entertainment ------------------

1.Event Ticket Booking Form


1. STATE:

variable: Attributes   : bookingID, userID, eventName, eventDate, seatCategory, ticketQuantity, totalCost, paymentMethod, bookingDate, status  
value   : Values      : 490098765432, 110012345678, "Music Concert", "2025-05-15", "VIP", 2, 5000.00, "Credit Card", "2025-04-10", "Confirmed"  
type    : datatypes   : int, int, str, str, str, int, float, str, str, str  

2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Booking       : When a user books event tickets (User/System)  
    - Retrieve Booking     : Fetch booking details using booking ID or user ID (User/Admin)  
    - Update Booking       : Modify seat category or payment method before confirmation  
    - Delete Booking       : Cancel booking if needed before event date  

    
    2.Movie Ticket Reservation Form

    
    1. STATE:

variable: Attributes   : reservationID, userID, movieName, theaterName, showTime, ticketQuantity, seatNumbers, totalCost, paymentMethod, bookingDate, status  
value   : Values      : 500098765432, 110012345678, "Avengers: Endgame", "PVR Cinemas", "2025-04-12, 7:30 PM", 3, "A12, A13, A14", 1200.00, "UPI", "2025-04-10", "Confirmed"  
type    : datatypes   : int, int, str, str, str, int, str, float, str, str, str  


2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Reservation   : When a user books movie tickets (User/System)  
    - Retrieve Reservation : Fetch reservation details using reservation ID or user ID (User/Admin)  
    - Update Reservation   : Modify showtime or seat selection before confirmation  
    - Delete Reservation   : Cancel reservation before showtime  


3.Festival Registration Form
1. STATE:

variable: Attributes   : registrationID, userID, eventName, eventDate, attendeeName, ticketType, ticketQuantity, totalCost, paymentMethod, registrationDate, status  
value   : Values      : 510098765432, 110012345678, "Sunburn Festival", "2025-06-10", "Rahul Sharma", "VIP Pass", 2, 8000.00, "Credit Card", "2025-04-10", "Confirmed"  
type    : datatypes   : int, int, str, str, str, str, int, float, str, str, str  


2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Registration  : When a user registers for a concert/festival (User/System)  
    - Retrieve Registration: Fetch registration details using registration ID (User/Admin)  
    - Update Registration  : Modify attendee name or pass type before the event  
    - Delete Registration  : Cancel registration before the event date  

    
4.Subscription Plan Form

    1. STATE:

variable: Attributes   : subscriptionID, userID, planType, duration, startDate, endDate, totalCost, paymentMethod, autoRenewal, status  
value   : Values      : 520098765432, 110012345678, "Premium HD", "Annual", "2025-04-10", "2026-04-10", 1499.00, "Debit Card", "Enabled", "Active"  
type    : datatypes   : int, int, str, str, str, str, float, str, str, str  


2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Subscription  : When a user subscribes to a streaming plan (User/System)  
    - Retrieve Subscription: Fetch subscription details using subscription ID (User/Admin)  
    - Update Subscription  : Modify plan type, payment method, or auto-renewal setting  
    - Delete Subscription  : Cancel subscription before renewal date  

    
    5.Content Upload Form

    
1. STATE:

variable: Attributes   : uploadID, creatorID, contentType, title, description, category, fileSize, uploadDate, visibility, status  
value   : Values      : 530098765432, 220012345678, "Video", "Travel Vlog - Bali", "Exploring Bali’s hidden gems", "Travel", 500MB, "2025-04-10", "Public", "Under Review"  
type    : datatypes   : int, int, str, str, str, str, float, str, str, str  
2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Upload       : When a creator uploads new content (User/System)  
    - Retrieve Upload     : Fetch content details using upload ID (Creator/Admin)  
    - Update Upload       : Modify title, description, or visibility settings before approval  
    - Delete Upload       : Remove content if it violates guidelines or upon creator request  
6.Game Tournament Registration Form


1. STATE:

variable: Attributes   : registrationID, playerID, teamName, gameTitle, tournamentDate, skillLevel, entryFee, paymentMethod, registrationDate, status  
value   : Values      : 540098765432, 330012345678, "Shadow Warriors", "Call of Duty", "2025-05-15", "Pro", 500.00, "PayPal", "2025-04-10", "Confirmed"  
type    : datatypes   : int, int, str, str, str, str, float, str, str, str  


2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Registration  : When a player/team registers for a gaming tournament (User/System)  
    - Retrieve Registration: Fetch registration details using registration ID (User/Admin)  
    - Update Registration  : Modify team name or skill level before tournament start  
    - Delete Registration  : Cancel registration before the event  

7.Review & Rating Form


1. STATE:

variable: Attributes   : reviewID, userID, contentType, contentTitle, rating, reviewText, reviewDate, likes, status  
value   : Values      : 550098765432, 440012345678, "Movie", "Inception", 5, "Mind-blowing visuals and storytelling!", "2025-04-10", 120, "Published"  
type    : datatypes   : int, int, str, str, int, str, str, int, str  


2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Review       : When a user submits a rating and review (User/System)  
    - Retrieve Review     : Fetch reviews based on content title or user ID (User/Admin)  
    - Update Review       : Edit review text or rating before final submission  
    - Delete Review       : Remove review due to guideline violations or user request  
8.Event Feedback Form

1. STATE:

variable: Attributes   : feedbackID, userID, eventName, eventDate, rating, comments, feedbackDate, suggestions, status  
value   : Values      : 560098765432, 550012345678, "Tech Conference 2025", "2025-06-20", 4, "Great speakers, but venue was crowded.", "2025-06-21", "Bigger venue next year", "Reviewed"  
type    : datatypes   : int, int, str, str, int, str, str, str, str  


2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Feedback     : When an attendee submits event feedback (User/System)  
    - Retrieve Feedback   : Fetch feedback based on event name or user ID (Organizer/Admin)  
    - Update Feedback     : Modify comments or suggestions before final submission  
    - Delete Feedback     : Remove feedback if it violates policies or upon user request  

    
    9.Casting/Audition Application Form

    
    1. STATE:

variable: Attributes   : applicationID, applicantID, name, age, talentType, portfolioLink, experienceYears, auditionRole, submissionDate, status  
value   : Values      : 570098765432, 660012345678, "Aarav Mehta", 25, "Actor", "www.portfolio.com/aarav", 3, "Lead Role", "2025-04-10", "Under Review"  
type    : datatypes   : int, int, str, int, str, str, int, str, str, str  


2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Application  : When an artist submits an audition application (User/System)  
    - Retrieve Application: Fetch audition details based on applicant ID or role (Casting Team)  
    - Update Application  : Modify talent details or portfolio before review  
    - Delete Application  : Withdraw application if needed before selection  

    
    10.Merchandise Purchase Form

    
    1. STATE:

variable: Attributes   : orderID, userID, itemName, itemSize, quantity, price, totalCost, shippingAddress, paymentMethod, orderDate, status  
value   : Values      : 580098765432, 770012345678, "Band T-Shirt", "L", 2, 799.00, 1598.00, "123, MG Road, Mumbai", "Credit Card", "2025-04-10", "Shipped"  
type    : datatypes   : int, int, str, str, int, float, float, str, str, str, str  


2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Order       : When a user purchases merchandise (User/System)  
    - Retrieve Order     : Fetch order details using order ID (User/Admin)  
    - Update Order       : Modify size or shipping address before dispatch  
    - Delete Order       : Cancel order before shipment  


















'''