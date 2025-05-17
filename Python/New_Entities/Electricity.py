
'''
-------------- Electricity-------------

1. Electricity Bill Payment Form:
1. STATE:

variable: Attributes   : billID, consumerID, userID, billAmount, dueDate, paymentMethod, transactionID, paymentDate, status  
value   : Values      : 200098765432, "EB123456789", 110012345678, 1500.75, "2025-04-15", "Credit Card", "TXN789654321", "2025-04-09", "Paid"  
type    : datatypes   : int, str, int, float, str, str, str, str, str  


2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Bill Payment   : When a user initiates an electricity bill payment (User/System)  
    - Retrieve Bill Payment : Fetch bill details using bill ID or consumer ID (User/System)  
    - Update Bill Payment   : Modify payment method before transaction confirmation  
    - Delete Bill Payment   : Cancel payment request if not yet processed  


2.New Electricity Connection Form


1. STATE:

variable: Attributes   : applicationID, applicantName, userID, address, IDProof, loadRequirement, applicationDate, status  
value   : Values      : 210098765432, "Madhu Kumar", 110012345678, "123, MG Road, Bangalore", "Aadhar_123456.pdf", "5 kW", "2025-04-09", "Pending"  
type    : datatypes   : int, str, int, str, str, str, str, str  


2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Application     : When a user applies for a new electricity connection (User/System)  
    - Retrieve Application   : Fetch application details using application ID or user ID (User/System)  
    - Update Application     : Modify applicant details, address, or load requirement before approval  
    - Delete Application     : Withdraw application request if no longer needed  

    3.Electricity Service Complaint Form

1. STATE:

variable: Attributes   : complaintID, consumerID, userID, issueType, description, complaintDate, status, resolutionDetails  
value   : Values      : 220098765432, "EB123456789", 110012345678, "Power Outage", "No electricity since 6 hours.", "2025-04-09", "Open", "Technician assigned"  
type    : datatypes   : int, str, int, str, str, str, str, str  

2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Complaint       : When a user reports an electricity service issue (User/System)  
    - Retrieve Complaint     : Fetch complaint details using complaint ID or consumer ID (User/System)  
    - Update Complaint       : Modify issue description or add resolution details  
    - Delete Complaint       : Close or withdraw complaint if resolved  


4.Meter Reading Submission Form
1. STATE:

variable: Attributes   : submissionID, consumerID, userID, meterReading, readingDate, meterPhoto, status  
value   : Values      : 230098765432, "EB123456789", 110012345678, 3567.45, "2025-04-09", "meter_photo.jpg", "Submitted"  
type    : datatypes   : int, str, int, float, str, str, str  
2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Submission     : When a user submits a new meter reading (User/System)  
    - Retrieve Submission   : Fetch meter reading details using submission ID or consumer ID (User/System)  
    - Update Submission     : Modify meter reading or upload a new meter photo before processing  
    - Delete Submission     : Withdraw reading submission if incorrect  

    
    5.Change of Name/Ownership Form

1. STATE:

variable: Attributes   : requestID, consumerID, userID, currentOwner, newOwner, IDProof, addressProof, requestDate, status  
value   : Values      : 240098765432, "EB123456789", 110012345678, "Madhu Kumar", "Rajesh Sharma", "Aadhar_123456.pdf", "AddressProof.pdf", "2025-04-09", "Pending"  
type    : datatypes   : int, str, int, str, str, str, str, str, str  


2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Request       : When a user applies for a name/ownership change (User/System)  
    - Retrieve Request     : Fetch request details using request ID or consumer ID (User/System)  
    - Update Request       : Modify new owner details or upload additional documents before approval  
    - Delete Request       : Cancel request if no longer needed  


6.Solar Panel Installation Request Form



1. STATE:

variable: Attributes   : requestID, consumerID, userID, installationAddress, panelCapacity, subsidyRequired, documents, requestDate, status  
value   : Values      : 250098765432, "EB123456789", 110012345678, "123, MG Road, Bangalore", "5 kW", "Yes", "IDProof.pdf, AddressProof.pdf", "2025-04-09", "Pending"  
type    : datatypes   : int, str, int, str, str, str, str, str, str  

2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Request       : When a user applies for a solar panel installation (User/System)  
    - Retrieve Request     : Fetch request details using request ID or consumer ID (User/System)  
    - Update Request       : Modify installation address, capacity, or documents before approval  
    - Delete Request       : Withdraw application if no longer required  

    
   7. Energy Consumption Report Form

1. STATE:

variable: Attributes   : reportID, consumerID, userID, requestDate, reportPeriod, deliveryMethod, status, reportFile  
value   : Values      : 260098765432, "EB123456789", 110012345678, "2025-04-09", "Last 6 Months", "Email", "Processed", "energy_report.pdf"  
type    : datatypes   : int, str, int, str, str, str, str, str  


2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Request       : When a user requests an energy consumption report (User/System)  
    - Retrieve Report      : Fetch report details using report ID or consumer ID (User/System)  
    - Update Request       : Modify report period or delivery method before processing  
    - Delete Request       : Cancel report request if not needed  




9.Connection Termination Form



1. STATE:

variable: Attributes   : requestID, consumerID, userID, terminationReason, terminationDate, refundDetails, requestDate, status  
value   : Values      : 270098765432, "EB123456789", 110012345678, "Shifting to new location", "2025-04-15", "Bank Transfer", "2025-04-09", "Pending"  
type    : datatypes   : int, str, int, str, str, str, str, str  

2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Request       : When a user applies for service disconnection (User/System)  
    - Retrieve Request     : Fetch termination details using request ID or consumer ID (User/System)  
    - Update Request       : Modify termination date or refund details before processing  
    - Delete Request       : Cancel termination request if service is still needed  


10.Electricity Theft Report Form


1. STATE:

variable: Attributes   : reportID, location, reporterID, theftType, description, evidence, reportDate, status  
value   : Values      : 280098765432, "MG Road, Bangalore", 110012345678, "Illegal Connection", "Unauthorized connection found in the neighborhood.", "photo_evidence.jpg", "2025-04-09", "Under Investigation"  
type    : datatypes   : int, str, int, str, str, str, str, str  


2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Report        : When a user reports electricity theft (User/System)  
    - Retrieve Report      : Fetch report details using report ID or location (User/System)  
    - Update Report        : Modify theft description or upload additional evidence before processing  
    - Delete Report        : Withdraw report if submitted incorrectly  









'''





