



'''
--------------Banking ------------

1.Entity: Login Form 

1.State

variable: Attributes   : username, password, biometricEnabled, loginAttempts, isLocked, lastLogin, otpEnabled, role, status
value   : Values      : "madhu@gmail.com", "1234r5hj", True, 2, False, "2025-04-08 10:30:00", True, "Customer", "Active"
type    : datatypes   : str, str, bool, int, bool, str, bool, str, str

 2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE 

    - Create Login        : When a new user registers (User/Bank)  
    - Retrieve Login Info : User attempts login using username/password/biometric  
    - Update Login        : Change password, enable/disable biometric, update OTP settings  
    - Delete Login        : Account deactivation due to user request or bank policy 

2. Entity: New Account Opening
    
    
    1. STATE:

variable: Attributes   : accountNumber, fullName, dob, gender, address, contactNumber, email, idProof, idProofNumber, addressProof, initialDeposit, accountType, nominee, branch, status
value   : Values      : 100123456789, "Madhu Kumar", "14-Jun-1992", "Male", "Bangalore, India", 9876543210, "madhu@gmail.com", "Aadhar", "1234-5678-9012", "Electricity Bill", 5000.00, "Savings", "Rajesh Kumar", "DPS Branch", "Pending"
type    : datatypes   : int, str, str, str, str, int, str, str, str, str, float, str, str, str, str

 2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE 

    - Create Account       : When a new user applies for a bank account (User/Bank)  
    - Retrieve Account Info: Fetch account details using account number or user ID (User/Bank)  
    - Update Account       : Modify address, contact details, nominee, or KYC details  
    - Delete Account       : Account closure upon user request or bank policy  


3.Credit/Debit Card Application Form   
    
    1. STATE:

variable: Attributes   : applicationID, fullName, dob, gender, address, contactNumber, email, employmentStatus, annualIncome, incomeProof, cardType, cardLimit, bankAccountNumber, branch, status
value   : Values      : 200987654321, "Madhu Kumar", "14-Jun-1992", "Male", "Bangalore, India", 9876543210, "madhu@gmail.com", "Salaried", 600000.00, "Salary Slip", "Credit Card - Platinum", 200000.00, 100123456789, "DPS Branch", "Pending"
type    : datatypes   : int, str, str, str, str, int, str, str, float, str, str, float, int, str, str

    
    2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE 

    - Create Application     : When a user applies for a credit/debit card (User/Bank)  
    - Retrieve Application   : Fetch application details using application ID or account number (User/Bank)  
    - Update Application     : Modify address, income proof, or card preference before approval  
    - Delete Application     : Cancel application due to user request or bank policy  

4.Loan Application Form

1. STATE:

variable: Attributes   : applicationID, fullName, dob, gender, address, contactNumber, email, loanType, loanAmount, annualIncome, incomeProof, employmentStatus, bankAccountNumber, branch, status  
value   : Values      : 300456789012, "Madhu Kumar", "14-Jun-1992", "Male", "Bangalore, India", 9876543210, "madhu@gmail.com", "Home Loan", 2500000.00, 600000.00, "Salary Slip", "Salaried", 100123456789, "DPS Branch", "Pending"  
type    : datatypes   : int, str, str, str, str, int, str, str, float, float, str, str, int, str, str  


2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Loan Application : When a user applies for a loan (User/Bank)  
    - Retrieve Loan Application : Fetch loan details using application ID or account number (User/Bank)  
    - Update Loan Application : Modify income proof, loan amount, or contact details before approval  
    - Delete Loan Application : Cancel application due to user request or bank policy  

5.Fund Transfer Form
    
    1. STATE:

variable: Attributes   : transactionID, senderAccount, senderName, receiverAccount, receiverName, amount, transactionMode, transactionDate, status  
value   : Values      : 500987654321, 100123456789, "Madhu Kumar", 200987654321, "Rajesh Kumar", 25000.00, "IMPS", "2025-04-09 12:30:00", "Successful"  
type    : datatypes   : int, int, str, int, str, float, str, str, str  


2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Fund Transfer : When a user initiates a money transfer (User/Bank)  
    - Retrieve Transaction : Fetch transaction details using transaction ID or account number (User/Bank)  
    - Update Transaction   : Modify receiver details or amount before processing (if allowed)  
    - Delete Transaction   : Cancel transaction if not yet processed (User/Bank)  

6.Deposit Form
    
    1. STATE:

variable: Attributes   : depositID, accountNumber, depositorName, depositType, depositAmount, interestRate, maturityPeriod, startDate, maturityDate, payoutPreference, status  
value   : Values      : 600123456789, 100123456789, "Madhu Kumar", "Fixed Deposit", 500000.00, 6.5, "5 Years", "2025-04-09", "2030-04-09", "Quarterly", "Active"  
type    : datatypes   : int, int, str, str, float, float, str, str, str, str, str  

2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Deposit      : When a user opens a Fixed Deposit (FD) or Recurring Deposit (RD) (User/Bank)  
    - Retrieve Deposit    : Fetch deposit details using deposit ID or account number (User/Bank)  
    - Update Deposit      : Modify payout preference, nominee details, or auto-renewal settings before maturity  
    - Delete Deposit      : Close deposit on maturity or pre-close upon user request (User/Bank)  

   7. KYC Update Form: 
 1. STATE:

variable: Attributes   : kycID, userID, fullName, dob, oldAddress, newAddress, oldContactNumber, newContactNumber, idProof, idProofNumber, addressProof, updateDate, status  
value   : Values      : 700456789012, 100123456789, "Madhu Kumar", "14-Jun-1992", "Bangalore, India", "Mumbai, India", 9876543210, 9123456789, "Aadhar", "1234-5678-9012", "Electricity Bill", "2025-04-09", "Pending"  
type    : datatypes   : int, int, str, str, str, str, int, int, str, str, str, str, str  
   
    2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create KYC Update    : When a user submits a KYC update request (User/Bank)  
    - Retrieve KYC Info    : Fetch KYC details using KYC ID or user ID (User/Bank)  
    - Update KYC Info      : Modify address, contact details, or proof documents before approval  
    - Delete KYC Request   : Cancel KYC update request (User/Bank)  

    
  8.Account Closure Form 

  1. STATE:

variable: Attributes   : closureID, accountNumber, accountHolderName, closureReason, refundAccount, refundMode, closureDate, status  
value   : Values      : 800987654321, 100123456789, "Madhu Kumar", "Relocating to another country", 200987654321, "NEFT", "2025-04-09", "Pending"  
type    : datatypes   : int, int, str, str, int, str, str, str  
 
  2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Closure Request : When a user submits an account closure request (User/Bank)  
    - Retrieve Closure Status: Fetch account closure details using closure ID or account number (User/Bank)  
    - Update Closure Request : Modify refund account details or reason before processing (User/Bank)  
    - Delete Closure Request : Cancel closure request if the user decides to retain the account  
  
9. Cheque Book Request Form 
    
    1. STATE:

variable: Attributes   : requestID, accountNumber, accountHolderName, leavesRequired, deliveryAddress, requestDate, status  
value   : Values      : 900123456789, 100123456789, "Madhu Kumar", 25, "Bangalore, India", "2025-04-09", "Processing"  
type    : datatypes   : int, int, str, int, str, str, str  

    
    2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Request      : When a user requests a new cheque book (User/Bank)  
    - Retrieve Request    : Fetch cheque book request status using request ID or account number (User/Bank)  
    - Update Request      : Modify delivery address or number of leaves before processing  
    - Delete Request      : Cancel cheque book request before it is dispatched  

    
    
10.Dispute/Chargeback Form
    
    1. STATE:

variable: Attributes   : disputeID, transactionID, accountNumber, accountHolderName, transactionDate, transactionAmount, disputeReason, supportingDocuments, disputeDate, status  
value   : Values      : 100012345678, 500987654321, 100123456789, "Madhu Kumar", "2025-04-08 14:45:00", 15000.00, "Unauthorized Transaction", "screenshot.pdf", "2025-04-09", "Under Review"  
type    : datatypes   : int, int, int, str, str, float, str, str, str, str  

   2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Dispute       : When a user files a dispute for a transaction (User/Bank)  
    - Retrieve Dispute     : Fetch dispute details using dispute ID or transaction ID (User/Bank)  
    - Update Dispute       : Modify dispute reason or add supporting documents before resolution  
    - Delete Dispute       : Withdraw dispute request if the issue is resolved externally  
 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    '''