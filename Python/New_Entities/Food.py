'''
-----------------food-------------

1.User Registration/Login Form

1. STATE:

variable: Attributes   : userID, name, email, phone, passwordHash, socialMediaLogin, accountStatus, lastLogin  
value   : Values      : 100123, "Rahul Sharma", "rahul@example.com", "+91-9876543210", "hashed_password", "Google", "Active", "2025-04-09 08:30 AM"  
type    : datatypes   : int, str, str, str, str, str, str, str  
Food Order Form


2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create User         : When a new user signs up (User/System)  
    - Retrieve User       : Fetch login details using email/phone/social media (System)  
    - Update User         : Change password, phone, or account settings  
    - Delete User         : Account deactivation due to user request or inactivity  

    
    2.Food Order Form


1. STATE:

variable: Attributes   : orderID, userID, restaurantName, dishList, quantity, deliveryAddress, paymentMethod, orderStatus, orderTime  
value   : Values      : 567890, 100123, "Tandoori Junction", ["Paneer Butter Masala", "Garlic Naan"], [1, 2], "123 Street, Bangalore", "UPI", "Preparing", "2025-04-09 07:15 PM"  
type    : datatypes   : int, int, str, list, list, str, str, str, str 



2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Order       : When a user places a food order (User/System)  
    - Retrieve Order     : Fetch order details using order ID (User/Restaurant)  
    - Update Order       : Modify quantity, address, or payment method before confirmation  
    - Delete Order       : Cancel order before it is prepared  


3.Table Reservation Form

1. STATE:

variable: Attributes   : reservationID, userID, restaurantName, date, time, numberOfGuests, specialRequests, reservationStatus  
value   : Values      : 987654, 100123, "Olive Bistro", "2025-04-15", "08:00 PM", 4, "Birthday celebration, need a corner table", "Confirmed"  
type    : datatypes   : int, int, str, str, str, int, str, str  

2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Reservation   : When a user books a table (User/System)  
    - Retrieve Reservation : Fetch reservation details using reservation ID (User/Restaurant)  
    - Update Reservation   : Modify date, time, or number of guests before confirmation  
    - Delete Reservation   : Cancel reservation before the scheduled time 


4.Order Cancellation Form

1. STATE:

variable: Attributes   : cancellationID, orderID, userID, cancellationReason, refundPreference, cancellationStatus  
value   : Values      : 789012, 567890, 100123, "Delayed delivery", "Refund to UPI", "Processed"  
type    : datatypes   : int, int, int, str, str, str  

2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Cancellation   : When a user cancels an order (User/System)  
    - Retrieve Cancellation : Fetch cancellation details using cancellation ID (User/System)  
    - Update Cancellation   : Modify refund preference before processing  
    - Delete Cancellation   : Remove cancellation request if the issue is resolved 


5.Order Tracking Form

1. STATE:

variable: Attributes   : trackingID, orderID, userID, currentStatus, estimatedDeliveryTime, deliveryPartner, trackingLink  
value   : Values      : 345678, 567890, 100123, "Out for Delivery", "2025-04-09 08:30 PM", "Zomato Rider - Rajesh", "https://tracking.example.com/345678"  
type    : datatypes   : int, int, int, str, str, str, str  

2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Tracking       : When an order is placed and assigned to a delivery partner (System)  
    - Retrieve Tracking     : Fetch real-time order status using order ID (User/System)  
    - Update Tracking       : Modify estimated time based on delays or changes in status  
    - Delete Tracking       : Remove tracking info once the order is delivered 
     
      
 6.Food Review & Rating Form

1. STATE:

variable: Attributes   : reviewID, orderID, userID, restaurantName, dishName, rating, comments, photoUpload, reviewDate  
value   : Values      : 112233, 567890, 100123, "Tandoori Junction", "Paneer Butter Masala", 5, "Delicious and well-cooked!", ["image1.jpg", "image2.jpg"], "2025-04-09"  
type    : datatypes   : int, int, int, str, str, int, str, list, str  

2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Review      : When a user submits feedback after an order (User/System)  
    - Retrieve Review    : Fetch reviews for a specific dish/restaurant (User/System)  
    - Update Review      : Modify rating or comments within a time limit  
    - Delete Review      : Remove a review if it violates guidelines  



    
    7.Chef Special Request Form

1. STATE:

variable: Attributes   : requestID, orderID, userID, restaurantName, dishName, specialInstructions, status  
value   : Values      : 554433, 678901, 100123, "Spice Haven", "Margherita Pizza", "No spice, extra cheese", "Accepted"  
type    : datatypes   : int, int, int, str, str, str, str  

2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Request       : When a user adds special instructions to an order (User/System)  
    - Retrieve Request     : Fetch special requests for an ongoing order (Restaurant/System)  
    - Update Request       : Modify special instructions before order confirmation  
    - Delete Request       : Remove request if not needed  

    8.Subscription/Meal Plan Form

1. STATE:

variable: Attributes   : subscriptionID, userID, planType, dietaryPreferences, duration, startDate, paymentStatus  
value   : Values      : 987654, 100123, "Weekly Meal Plan", "Vegetarian, High Protein", "7 Days", "2025-04-10", "Paid"  
type    : datatypes   : int, int, str, str, str, str, str  

2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Subscription   : When a user subscribes to a meal plan (User/System)  
    - Retrieve Subscription : Fetch details of an active meal plan (User/System)  
    - Update Subscription   : Modify dietary preferences or duration before renewal  
    - Delete Subscription   : Cancel plan before the next billing cycle  



9.Restaurant Registration Form

1. STATE:

variable: Attributes   : restaurantID, ownerName, restaurantName, location, contactNumber, cuisineType, menu, registrationStatus  
value   : Values      : 123456, "Rajesh Kumar", "Tandoori Flames", "Hyderabad", "9876543210", "Indian, Chinese", ["Paneer Tikka", "Butter Naan"], "Approved"  
type    : datatypes   : int, str, str, str, str, str, list, str  

2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Registration   : When a restaurant applies for listing (Owner/System)  
    - Retrieve Registration : Fetch restaurant details and menu (User/System)  
    - Update Registration   : Modify contact details, menu, or status  
    - Delete Registration   : Remove restaurant listing upon request  



10.Customer Support/Complaint Form

1. STATE:

variable: Attributes   : complaintID, userID, orderID, issueType, description, resolutionStatus  
value   : Values      : 789654, 100123, 567890, "Missing Item", "Ordered 3 items, received 2", "Pending"  
type    : datatypes   : int, int, int, str, str, str  



2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Complaint     : When a user reports an issue (User/System)  
    - Retrieve Complaint   : Fetch complaint status and details (User/System)  
    - Update Complaint     : Modify issue description or add supporting documents  
    - Delete Complaint     : Remove complaint if resolved or incorrect  











'''