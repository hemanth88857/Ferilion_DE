'''
------------Insurance--------------

1.Insurance Policy Application Form

1. STATE:

variable: Attributes   : applicationID, userID, applicantName, insuranceType, coverageAmount, policyTerm, nomineeName, documents, applicationDate, status  
value   : Values      : 290098765432, 110012345678, "Madhu Kumar", "Health Insurance", 500000, "10 Years", "Rajesh Sharma", "IDProof.pdf, MedicalReport.pdf", "2025-04-09", "Pending"  
type    : datatypes   : int, int, str, str, float, str, str, str, str, str  


2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Application    : When a user applies for an insurance policy (User/System)  
    - Retrieve Application  : Fetch policy application details using application ID or user ID (User/System)  
    - Update Application    : Modify coverage, nominee details, or documents before approval  
    - Delete Application    : Withdraw policy application if not required  

2.Premium Payment Form

1. STATE:

variable: Attributes   : paymentID, policyNumber, userID, premiumAmount, dueDate, paymentMethod, transactionID, paymentDate, status  
value   : Values      : 300098765432, "POL123456789", 110012345678, 15000, "2025-04-15", "Credit Card", "TXN987654321", "2025-04-09", "Paid"  
type    : datatypes   : int, str, int, float, str, str, str, str, str  


2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Payment       : When a user makes an insurance premium payment (User/System)  
    - Retrieve Payment     : Fetch payment details using payment ID or policy number (User/System)  
    - Update Payment       : Modify payment method before processing  
    - Delete Payment       : Cancel payment request if not yet processed  


3.Claim Request Form

1. STATE:

variable: Attributes   : claimID, policyNumber, userID, policyholderName, claimReason, claimAmount, documents, claimDate, status  
value   : Values      : 310098765432, "POL123456789", 110012345678, "Madhu Kumar", "Hospitalization", 200000, "MedicalBills.pdf, DoctorReport.pdf", "2025-04-09", "Under Review"  
type    : datatypes   : int, str, int, str, str, float, str, str, str  


2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Claim         : When a user submits a claim request (User/System)  
    - Retrieve Claim       : Fetch claim details using claim ID or policy number (User/System)  
    - Update Claim         : Modify claim details or upload additional documents before processing  
    - Delete Claim         : Withdraw claim request if not required  

    
    4.Claim Status Inquiry Form

1. STATE:

variable: Attributes   : inquiryID, claimID, policyNumber, userID, inquiryDate, status, responseDetails  
value   : Values      : 320098765432, 310098765432, "POL123456789", 110012345678, "2025-04-10", "Processing", "Claim under assessment, expected resolution in 7 days"  
type    : datatypes   : int, int, str, int, str, str, str  

2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Inquiry       : When a user checks the status of an existing claim (User/System)  
    - Retrieve Inquiry     : Fetch inquiry details using inquiry ID or claim ID (User/System)  
    - Update Inquiry       : Modify inquiry request before response is generated  
    - Delete Inquiry       : Cancel status inquiry if no longer needed  

    
    5,Policy Renewal Form

    
    1. STATE:

variable: Attributes   : renewalID, policyNumber, userID, policyholderName, renewalOption, newCoverage, renewalAmount, renewalDate, status  
value   : Values      : 330098765432, "POL123456789", 110012345678, "Madhu Kumar", "Same Coverage", 500000, 15000, "2025-04-10", "Pending"  
type    : datatypes   : int, str, int, str, str, float, float, str, str  


2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Renewal Request : When a user submits a policy renewal application (User/System)  
    - Retrieve Renewal       : Fetch renewal details using renewal ID or policy number (User/System)  
    - Update Renewal         : Modify coverage or renewal amount before processing  
    - Delete Renewal         : Cancel renewal request if policyholder chooses not to renew  

    
    6.Beneficiary Nomination Form


1. STATE:

variable: Attributes   : nominationID, policyNumber, userID, policyholderName, beneficiaryName, relationship, beneficiaryShare, nomineeDocuments, nominationDate, status  
value   : Values      : 340098765432, "POL123456789", 110012345678, "Madhu Kumar", "Rajesh Sharma", "Brother", 100%, "IDProof.pdf", "2025-04-09", "Approved"  
type    : datatypes   : int, str, int, str, str, str, float, str, str, str  


2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Nomination     : When a user adds a beneficiary (User/System)  
    - Retrieve Nomination   : Fetch nomination details using nomination ID or policy number (User/System)  
    - Update Nomination     : Modify beneficiary details or percentage share before approval  
    - Delete Nomination     : Remove beneficiary if policyholder changes nomination  

    
    7.Policy Cancellation Form

    1. STATE:

variable: Attributes   : cancellationID, policyNumber, userID, policyholderName, cancellationReason, refundAmount, refundMethod, cancellationDate, status  
value   : Values      : 350098765432, "POL123456789", 110012345678, "Madhu Kumar", "No longer needed", 12000, "Bank Transfer", "2025-04-10", "Pending"  
type    : datatypes   : int, str, int, str, str, float, str, str, str  


2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Cancellation    : When a user submits a policy cancellation request (User/System)  
    - Retrieve Cancellation  : Fetch cancellation details using cancellation ID or policy number (User/System)  
    - Update Cancellation    : Modify refund method or reason before processing  
    - Delete Cancellation    : Withdraw cancellation request if policyholder changes their mind  

    
    8.Policy Transfer Form

    
    1. STATE:

variable: Attributes   : transferID, policyNumber, oldUserID, newUserID, oldPolicyholderName, newPolicyholderName, transferReason, transferDocuments, transferDate, status  
value   : Values      : 360098765432, "POL123456789", 110012345678, 110098765432, "Madhu Kumar", "Rajesh Sharma", "Legal Heir Transfer", "OwnershipProof.pdf", "2025-04-10", "Under Review"  
type    : datatypes   : int, str, int, int, str, str, str, str, str, str  


2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Transfer Request : When a user submits a policy transfer application (User/System)  
    - Retrieve Transfer       : Fetch transfer details using transfer ID or policy number (User/System)  
    - Update Transfer         : Modify transfer documents or new owner details before approval  
    - Delete Transfer         : Cancel transfer request if ownership change is not needed  

9.Accident Report Form

1. STATE:

variable: Attributes   : reportID, policyNumber, userID, policyholderName, accidentDate, accidentLocation, accidentDetails, policeReport, witnesses, claimAmount, reportDate, status  
value   : Values      : 370098765432, "POL123456789", 110012345678, "Madhu Kumar", "2025-04-08", "Hyderabad, India", "Rear-end collision at signal", "FIR12345.pdf", "Rajesh Sharma, Amit Verma", 50000, "2025-04-09", "Under Review"  
type    : datatypes   : int, str, int, str, str, str, str, str, str, float, str, str  

2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Report        : When a user submits an accident report for an insurance claim (User/System)  
    - Retrieve Report      : Fetch report details using report ID or policy number (User/System)  
    - Update Report        : Modify accident details or attach additional documents before processing  
    - Delete Report        : Withdraw report if no claim is required  

    
    10.Complaint Form

1. STATE:

variable: Attributes   : complaintID, userID, policyNumber, complaintType, complaintDetails, supportingDocuments, submissionDate, resolutionStatus, resolutionDetails  
value   : Values      : 380098765432, 110012345678, "POL123456789", "Claim Rejection", "My health claim was rejected without valid reason.", "ClaimRejectionLetter.pdf", "2025-04-09", "Pending", "Under Review by Insurance Team"  
type    : datatypes   : int, int, str, str, str, str, str, str, str  


2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Complaint     : When a user submits a grievance regarding an insurance issue (User/System)  
    - Retrieve Complaint   : Fetch complaint details using complaint ID or policy number (User/System)  
    - Update Complaint     : Modify complaint details or attach additional evidence before resolution  
    - Delete Complaint     : Withdraw complaint if resolved outside the system  
























'''