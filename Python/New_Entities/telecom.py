'''
----------------telecom ------------------------

1.New SIM Card Application Form

1. STATE:

variable: Attributes   : applicationID, userName, userDOB, addressProof, idProof, mobilePlan, status  
value   : Values      : 10123456789, "Amit Sharma", "1995-08-22", "Aadhar Card", "PAN Card", "Unlimited 5G Plan", "Pending Approval"  
type    : datatypes   : int, str, str, str, str, str, str  

2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Application   : When a user applies for a new SIM card (User/System)  
    - Retrieve Application : Fetch SIM application details and status (User/System)  
    - Update Application   : Modify plan selection or upload missing documents  
    - Delete Application   : Cancel request before processing  

    
    
    2.Mobile Number Portability (MNP) Form

1. STATE:

variable: Attributes   : portRequestID, currentOperator, newOperator, mobileNumber, uniquePortingCode, status  
value   : Values      : 50067891011, "Airtel", "Jio", "9876543210", "XYZ123", "Processing"  
type    : datatypes   : int, str, str, str, str, str  

2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Request      : When a user requests number porting (User/System)  
    - Retrieve Request    : Check status using port request ID (User/System)  
    - Update Request      : Modify details before approval  
    - Delete Request      : Cancel porting before processing  




3.Recharge & Bill Payment Form

1. STATE:

variable: Attributes   : transactionID, mobileNumber, planType, amount, paymentMethod, transactionStatus  
value   : Values      : 9876543210123, "9876543210", "Prepaid - 28 Days 2GB/Day", "299", "Credit Card", "Successful"  
type    : datatypes   : int, str, str, float, str, str  

2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Payment      : When a user completes a recharge/bill payment (User/System)  
    - Retrieve Payment    : Fetch transaction history (User/System)  
    - Update Payment      : Modify payment method before transaction processing  
    - Delete Payment      : Cancel transaction if failed or incorrect  


4.Customer Support/Complaint Form

1. STATE:

variable: Attributes   : complaintID, customerName, mobileNumber, issueType, description, status  
value   : Values      : 1200456, "Rajesh Kumar", "9876543210", "Network Issue", "Frequent call drops in my area", "Pending"  
type    : datatypes   : int, str, str, str, str, str  

2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Complaint    : When a user reports an issue (User/System)  
    - Retrieve Complaint  : Check complaint status (User/System)  
    - Update Complaint    : Modify details before resolution  
    - Delete Complaint    : Cancel complaint if resolved or incorrect  



5.Plan Upgrade/Downgrade Form

1. STATE:

variable: Attributes   : requestID, customerName, mobileNumber, currentPlan, newPlan, status  
value   : Values      : 300789, "Sneha Gupta", "8765432109", "299 Unlimited 2GB/Day", "499 Unlimited 3GB/Day + OTT", "Processing"  
type    : datatypes   : int, str, str, str, str, str  

2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Request      : When a user requests a plan change (User/System)  
    - Retrieve Request    : Check status of plan change request (User/System)  
    - Update Request      : Modify plan before approval  
    - Delete Request      : Cancel request before processing  



6.International Roaming Activation Form

1. STATE:

variable: Attributes   : requestID, customerName, mobileNumber, destinationCountry, roamingPlan, activationDate, status  
value   : Values      : 450123, "Pooja Verma", "9123456789", "USA", "International Roaming Pack - 10GB + Calls", "2025-05-10", "Active"  
type    : datatypes   : int, str, str, str, str, str, str  

2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Request      : When a user applies for international roaming (User/System)  
    - Retrieve Request    : Fetch roaming activation details (User/System)  
    - Update Request      : Modify plan before activation  
    - Delete Request      : Cancel request before processing 



7.SIM Replacement Form

1. STATE:

variable: Attributes   : requestID, customerName, mobileNumber, reason, SIMType, status  
value   : Values      : 550789, "Anil Mehta", "9876543210", "Lost SIM", "eSIM", "Processing"  
type    : datatypes   : int, str, str, str, str, str  

2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Request      : User submits request for SIM replacement  
    - Retrieve Request    : Check status of SIM replacement  
    - Update Request      : Modify details before approval  
    - Delete Request      : Cancel request before processing  



8.KYC (Know Your Customer) Verification Form

1. STATE:

variable: Attributes   : verificationID, customerName, mobileNumber, IDProof, AddressProof, status  
value   : Values      : 650321, "Ramesh Patel", "8765432109", "Aadhaar Card", "Electricity Bill", "Pending"  
type    : datatypes   : int, str, str, str, str, str  

2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Verification : User uploads KYC documents  
    - Retrieve Verification : Check KYC verification status  
    - Update Verification : Modify KYC details if needed  
    - Delete Verification : Cancel KYC request before approval  



9.Telecom Service Termination Form

1. STATE:

variable: Attributes   : requestID, customerName, serviceType, mobileNumber, reason, status  
value   : Values      : 780654, "Suresh Reddy", "Broadband", "NA", "Relocating to a new city", "Processing"  
type    : datatypes   : int, str, str, str, str, str  

2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Request      : User submits request for service termination  
    - Retrieve Request    : Check termination request status  
    - Update Request      : Modify termination details before approval  
    - Delete Request      : Cancel termination request before processing  






10.Family or Business Plan Enrollment Form

1. STATE:

variable: Attributes   : requestID, primaryAccountHolder, planType, addedUsers, billingCycle, status  
value   : Values      : 905432, "Amit Sharma", "Family Plan - 4 Members", "3 Additional Users", "Monthly", "Active"  
type    : datatypes   : int, str, str, str, str, str  

2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Enrollment  : User adds family or business members  
    - Retrieve Enrollment : Check enrollment details and billing cycle  
    - Update Enrollment  : Modify plan or added users  
    - Delete Enrollment  : Remove users or cancel plan 












'''