

'''

---Transport-----

1.Vehicle Booking Form

1. STATE:

variable: Attributes   : bookingID, userID, vehicleType, pickupLocation, dropoffLocation, pickupDate, pickupTime, fareEstimate, paymentMethod, status  
value   : Values      : 390098765432, 110012345678, "Cab", "Hyderabad, India", "Bangalore, India", "2025-04-15", "10:30 AM", 4500, "Credit Card", "Confirmed"  
type    : datatypes   : int, int, str, str, str, str, str, float, str, str  

2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Booking       : When a user books a vehicle for travel (User/System)  
    - Retrieve Booking     : Fetch booking details using booking ID or user ID (User/System)  
    - Update Booking       : Modify pickup/drop-off location, time, or payment method before confirmation  
    - Delete Booking       : Cancel booking if no longer needed  

    2.Ride Cancellation Form

    
    1. STATE:

variable: Attributes   : cancellationID, bookingID, userID, cancellationReason, refundAmount, refundMethod, cancellationDate, status  
value   : Values      : 400098765432, 390098765432, 110012345678, "Change of Plans", 4500, "Wallet Refund", "2025-04-10", "Processed"  
type    : datatypes   : int, int, int, str, float, str, str, str  


2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Cancellation    : When a user cancels a booked ride (User/System)  
    - Retrieve Cancellation  : Fetch cancellation details using cancellation ID or booking ID (User/System)  
    - Update Cancellation    : Modify refund method or reason before processing  
    - Delete Cancellation    : Withdraw cancellation request if the user decides to proceed with the ride  

    
    3.Logistics Booking Form
    1. STATE:

variable: Attributes   : bookingID, userID, cargoType, cargoWeight, vehicleType, pickupAddress, destinationAddress, pickupDate, deliveryDate, fareEstimate, paymentMethod, status  
value   : Values      : 410098765432, 110012345678, "Electronics", 1200, "Truck", "Hyderabad, India", "Mumbai, India", "2025-04-12", "2025-04-14", 15000, "Bank Transfer", "Confirmed"  
type    : datatypes   : int, int, str, float, str, str, str, str, str, float, str, str  


2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Booking       : When a user books a logistics service (User/System)  
    - Retrieve Booking     : Fetch logistics booking details using booking ID or user ID (User/System)  
    - Update Booking       : Modify pickup/drop-off location, cargo details, or payment method before confirmation  
    - Delete Booking       : Cancel booking if no longer needed  

    
    4.Driver Registration Form

    
    1. STATE:

variable: Attributes   : driverID, name, licenseNumber, vehicleType, insuranceNumber, contactNumber, address, registrationDate, status  
value   : Values      : 420098765432, "Rajesh Kumar", "DL-12345-XYZ", "Truck", "INS-789654321", "+91-9876543210", "Bangalore, India", "2025-04-10", "Active"  
type    : datatypes   : int, str, str, str, str, str, str, str, str  

2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Registration     : When a driver applies for registration (Driver/System)  
    - Retrieve Registration   : Fetch driver details using driver ID or license number (Admin/System)  
    - Update Registration     : Modify contact details, insurance info, or vehicle type before approval  
    - Delete Registration     : Remove driver record if found ineligible or inactive  

    
    5.Passenger Feedback Form

1. STATE:

variable: Attributes   : feedbackID, rideID, userID, driverID, rating, driverBehavior, rideQuality, comments, submissionDate  
value   : Values      : 430098765432, 390098765432, 110012345678, 210056789012, 4.5, "Polite", "Smooth and comfortable", "Great ride, but slight delay.", "2025-04-10"  
type    : datatypes   : int, int, int, int, float, str, str, str, str  


2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Feedback       : When a passenger submits a review after a ride (User/System)  
    - Retrieve Feedback     : Fetch feedback using feedback ID or ride ID (Admin/System)  
    - Update Feedback       : Modify review or rating within a limited time frame  
    - Delete Feedback       : Remove feedback if flagged for inappropriate content  


6.Accident/Incident Report Form



1. STATE:

variable: Attributes   : reportID, rideID, userID, driverID, incidentType, incidentDetails, policeReport, witnesses, submissionDate, status  
value   : Values      : 440098765432, 390098765432, 110012345678, 210056789012, "Accident", "Minor collision at traffic signal", "FIR56789.pdf", "Ravi Sharma, Anil Mehta", "2025-04-10", "Under Review"  
type    : datatypes   : int, int, int, int, str, str, str, str, str, str  


2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Report        : When a passenger/driver submits an incident report (User/Driver/System)  
    - Retrieve Report      : Fetch incident details using report ID or ride ID (Admin/System)  
    - Update Report        : Modify incident details or attach supporting documents before review  
    - Delete Report        : Withdraw report if the issue is resolved  


7.Transport Permit Application Form
1. STATE:

variable: Attributes   : applicationID, applicantName, businessName, vehicleType, permitType, routeDetails, validityPeriod, applicationDate, status  
value   : Values      : 450098765432, "Amit Verma", "Verma Logistics", "Truck", "Commercial", "Delhi to Mumbai", "2025-04-15 to 2026-04-14", "2025-04-10", "Pending"  
type    : datatypes   : int, str, str, str, str, str, str, str, str  


2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Application     : When a business applies for a transport permit (User/System)  
    - Retrieve Application   : Fetch permit details using application ID (Admin/System)  
    - Update Application     : Modify route details, vehicle info, or business details before approval  
    - Delete Application     : Withdraw application if no longer needed  

    
    8.Lost & Found Form

    1. STATE:

variable: Attributes   : reportID, userID, rideID, lostItem, description, lastSeenLocation, contactInfo, submissionDate, status  
value   : Values      : 460098765432, 110012345678, 390098765432, "Wallet", "Brown leather wallet with ID card", "Back seat of cab", "+91-9876543210", "2025-04-10", "Under Investigation"  
type    : datatypes   : int, int, int, str, str, str, str, str, str  


2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Report        : When a user reports a lost item (User/System)  
    - Retrieve Report      : Fetch lost item details using report ID or ride ID (Admin/System)  
    - Update Report        : Modify item description or contact details before processing  
    - Delete Report        : Withdraw report if the item is found  


9.Fuel Reimbursement Form
1. STATE:

variable: Attributes   : claimID, employeeID, vehicleID, fuelAmount, totalCost, receiptImage, fillDate, submissionDate, approvalStatus  
value   : Values      : 470098765432, "EMP123456", "VEH789012", 20.5, 2500.75, "receipt123.jpg", "2025-04-08", "2025-04-10", "Pending"  
type    : datatypes   : int, str, str, float, float, str, str, str, str  

2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Claim        : When an employee submits a fuel reimbursement request (User/System)  
    - Retrieve Claim      : Fetch reimbursement details using claim ID or employee ID (Admin/System)  
    - Update Claim        : Modify claim details or attach missing documents before processing  
    - Delete Claim        : Cancel request if incorrect or unnecessary  

    
    10.Transport Complaint Form

    1. STATE:

variable: Attributes   : complaintID, userID, transportMode, issueType, description, incidentDate, submissionDate, status  
value   : Values      : 480098765432, 110012345678, "Cab", "Overcharging", "Driver charged extra beyond meter fare", "2025-04-09", "2025-04-10", "Under Review"  
type    : datatypes   : int, int, str, str, str, str, str, str  

2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Complaint    : When a user reports a transport issue (User/System)  
    - Retrieve Complaint  : Fetch complaint details using complaint ID (Admin/System)  
    - Update Complaint    : Modify issue details or attach supporting evidence before processing  
    - Delete Complaint    : Withdraw complaint if resolved  
































'''