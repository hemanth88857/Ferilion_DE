'''
--------Trading --------------


1.Trading Account Opening Form

1. STATE:

variable: Attributes   : applicationID, userID, fullName, dob, panNumber, aadharNumber, bankAccount, ifscCode, address, tradingExperience, accountType, submissionDate, status  
value   : Values      : 590098765432, 880012345678, "Rajesh Sharma", "1990-06-15", "ABCDE1234F", "123456789012", "9876543210", "HDFC0001234", "Mumbai, India", 2, "Demat & Trading", "2025-04-10", "Under Verification"  
type    : datatypes   : int, int, str, str, str, str, str, str, str, int, str, str, str  


2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Application  : When a user applies for a trading account (User/System)  
    - Retrieve Application: Fetch application details using application ID (User/Admin)  
    - Update Application  : Modify personal or bank details before approval  
    - Delete Application  : Withdraw application if not needed  

    

    2.Buy Order Form
1. STATE:

variable: Attributes   : orderID, userID, stockSymbol, stockExchange, quantity, priceType, orderPrice, orderValidity, orderDate, status  
value   : Values      : 600098765432, 990012345678, "TCS", "NSE", 10, "Limit", 3850.00, "Day", "2025-04-10", "Executed"  
type    : datatypes   : int, int, str, str, int, str, float, str, str, str  


2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Order       : When a user places a buy order (User/System)  
    - Retrieve Order     : Fetch order details based on order ID (User/Admin)  
    - Update Order       : Modify quantity or price type before execution  
    - Delete Order       : Cancel pending orders before execution  

    
    3.Sell Order Form
1. STATE:

variable: Attributes   : orderID, userID, stockSymbol, stockExchange, quantity, priceType, orderPrice, orderValidity, orderDate, status  
value   : Values      : 610098765432, 990012345678, "INFY", "NSE", 20, "Limit", 1525.00, "Day", "2025-04-10", "Pending"  
type    : datatypes   : int, int, str, str, int, str, float, str, str, str  


2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Order       : When a user places a sell order (User/System)  
    - Retrieve Order     : Fetch order details based on order ID (User/Admin)  
    - Update Order       : Modify quantity or price type before execution  
    - Delete Order       : Cancel pending orders before execution  

    

    4.IPO Application Form
    1. STATE:

variable: Attributes   : applicationID, userID, ipoName, companyName, lotSize, investmentAmount, upiID, applicationDate, status  
value   : Values      : 620098765432, 880012345678, "XYZ IPO", "XYZ Technologies Ltd.", 1, 15000.00, "user@upi", "2025-04-10", "Applied"  
type    : datatypes   : int, int, str, str, int, float, str, str, str  

2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Application  : When a user applies for an IPO (User/System)  
    - Retrieve Application: Fetch IPO application details using application ID (User/Admin)  
    - Update Application  : Modify investment amount or UPI details before submission  
    - Delete Application  : Withdraw IPO application before allotment  

   5.Margin Trading Request Form

   1. STATE:

variable: Attributes   : requestID, userID, collateralType, collateralValue, requestedMargin, riskConsent, submissionDate, status  
value   : Values      : 630098765432, 990012345678, "Stocks", 500000.00, 250000.00, "Agreed", "2025-04-10", "Pending Approval"  
type    : datatypes   : int, int, str, float, float, str, str, str  
     

2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Request      : When a user applies for margin trading (User/System)  
    - Retrieve Request    : Fetch margin request details using request ID (User/Admin)  
    - Update Request      : Modify collateral details before approval  
    - Delete Request      : Cancel request before processing  

    
    6.Funds Deposit Form

    1. STATE:

variable: Attributes   : depositID, userID, amount, paymentMethod, transactionID, depositDate, status  
value   : Values      : 640098765432, 990012345678, 50000.00, "Net Banking", "TXN987654321", "2025-04-10", "Successful"  
type    : datatypes   : int, int, float, str, str, str, str  


2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Deposit     : When a user adds funds to the trading account (User/System)  
    - Retrieve Deposit   : Fetch deposit details using deposit ID (User/Admin)  
    - Update Deposit     : Modify payment method before confirmation  
    - Delete Deposit     : Cancel deposit request if not yet processed  

    

    7.Funds Withdrawal Form

    1. STATE:

variable: Attributes   : withdrawalID, userID, amount, bankAccount, ifscCode, withdrawalMethod, requestDate, status  
value   : Values      : 650098765432, 990012345678, 25000.00, "XXXXXXXX1234", "HDFC0001234", "NEFT", "2025-04-10", "Processing"  
type    : datatypes   : int, int, float, str, str, str, str, str  


2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Request     : When a user requests a fund withdrawal (User/System)  
    - Retrieve Request   : Fetch withdrawal details using withdrawal ID (User/Admin)  
    - Update Request     : Modify bank details before processing  
    - Delete Request     : Cancel withdrawal before processing  

    
    9.Portfolio Management Request Form

    1. STATE:

variable: Attributes   : requestID, userID, investmentAmount, riskPreference, portfolioType, submissionDate, status  
value   : Values      : 660098765432, 990012345678, 500000.00, "Moderate", "Equity-Focused", "2025-04-10", "Under Review"  
type    : datatypes   : int, int, float, str, str, str, str  


2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Request      : When a user applies for portfolio management services (User/System)  
    - Retrieve Request    : Fetch portfolio request details using request ID (User/Admin)  
    - Update Request      : Modify investment amount or risk preference before approval  
    - Delete Request      : Cancel request before processing  


    10.Trading Account Closure Form

1. STATE:

variable: Attributes   : closureID, userID, accountNumber, closureReason, refundPreference, submissionDate, status  
value   : Values      : 670098765432, 990012345678, "TRD123456789", "Switching to another broker", "Transfer to Bank", "2025-04-10", "Pending Approval"  
type    : datatypes   : int, int, str, str, str, str, str  


2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Request      : When a user requests account closure (User/System)  
    - Retrieve Request    : Fetch closure request details using closure ID (User/Admin)  
    - Update Request      : Modify closure reason or refund preference before approval  
    - Delete Request      : Cancel request before processing  










'''