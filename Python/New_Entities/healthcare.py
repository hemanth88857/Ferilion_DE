'''
--------------healthcare --------------------------

1.Patient Registration Form

1. STATE:

variable: Attributes   : patientID, name, age, gender, contactNumber, address, medicalHistory, insuranceProvider, policyNumber, registrationDate  
value   : Values      : 880098765432, "Ravi Kumar", 45, "Male", "9876543210", "Hyderabad, India", "Diabetes, Hypertension", "Max Bupa", "POL123456789", "2025-04-10"  
type    : datatypes   : int, str, int, str, str, str, str, str, str, str  


2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Patient      : When a new patient registers (Hospital/System)  
    - Retrieve Patient    : Fetch patient details using patient ID (Hospital/Doctor)  
    - Update Patient      : Modify contact details, insurance, or medical history  
    - Delete Patient      : Remove patient record upon request or inactivity  


   2. Doctor Appointment Booking Form

   1. STATE:

variable: Attributes   : appointmentID, patientID, doctorID, department, appointmentDate, appointmentTime, reasonForVisit, status  
value   : Values      : 890098765432, 880098765432, 770012345678, "Cardiology", "2025-04-12", "10:30 AM", "Chest Pain", "Confirmed"  
type    : datatypes   : int, int, int, str, str, str, str, str  


2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Appointment  : When a patient books a doctor consultation (Patient/System)  
    - Retrieve Appointment: Fetch details using appointment ID (Patient/Hospital)  
    - Update Appointment  : Modify date, time, or doctor before confirmation  
    - Delete Appointment  : Cancel booking before the scheduled time  

    
    3.Medical History Form

    1. STATE:

variable: Attributes   : historyID, patientID, pastIllnesses, allergies, surgeries, medications, familyHistory, lastUpdated  
value   : Values      : 900098765432, 880098765432, "Diabetes, Hypertension", "Penicillin", "Appendectomy (2015)", "Metformin, Amlodipine", "Heart Disease", "2025-04-10"  
type    : datatypes   : int, int, str, str, str, str, str, str  


2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Record       : When a new patient registers (Hospital/System)  
    - Retrieve Record     : Fetch medical history using patient ID (Doctor/Hospital)  
    - Update Record       : Modify illnesses, allergies, surgeries, or medications  
    - Delete Record       : Remove history upon patient request or data retention policy  

    
    4.Prescription Refill Request Form

1. STATE:

variable: Attributes   : refillID, patientID, medicationName, dosage, quantity, pharmacy, requestDate, status  
value   : Values      : 910098765432, 880098765432, "Metformin", "500mg", "30 Tablets", "Apollo Pharmacy", "2025-04-10", "Pending Approval"  
type    : datatypes   : int, int, str, str, str, str, str, str  

2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Request      : When a patient requests a refill (Patient/System)  
    - Retrieve Request    : Fetch refill details using refill ID (Pharmacy/Doctor)  
    - Update Request      : Modify medication or pharmacy before approval  
    - Delete Request      : Cancel refill before processing  

5.Lab Test Booking Form

1. STATE:

variable: Attributes   : bookingID, patientID, selectedTests, appointmentDate, sampleCollection, labName, status  
value   : Values      : 920098765432, 880098765432, "CBC, Lipid Profile", "2025-04-12", "Home Collection", "Thyrocare", "Confirmed"  
type    : datatypes   : int, int, str, str, str, str, str  


2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Booking       : When a patient schedules lab tests (Patient/System)  
    - Retrieve Booking     : Fetch test details using booking ID (Patient/Lab)  
    - Update Booking       : Modify tests, date, or collection method before confirmation  
    - Delete Booking       : Cancel appointment before sample collection  

6.Health Insurance Claim Form

1. STATE:

variable: Attributes   : claimID, policyNumber, patientID, hospitalName, treatmentDetails, billAmount, claimDocuments, submissionDate, status  
value   : Values      : 930098765432, "POL123456789", 880098765432, "Apollo Hospitals", "Cardiac Surgery", "₹3,50,000", "Discharge Summary, Bills", "2025-04-10", "Under Review"  
type    : datatypes   : int, str, int, str, str, str, str, str, str  



2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Claim        : When a patient submits an insurance claim (Patient/System)  
    - Retrieve Claim      : Fetch claim details using claim ID (Patient/Insurance Provider)  
    - Update Claim        : Modify details or add documents before approval  
    - Delete Claim        : Withdraw claim before processing  


7.Telemedicine Consultation Form

1. STATE:

variable: Attributes   : consultationID, patientID, doctorID, symptoms, preferredDateTime, consultationMode, status  
value   : Values      : 940098765432, 880098765432, 770098765432, "Fever, Cough, Fatigue", "2025-04-12 10:30 AM", "Video Call", "Scheduled"  
type    : datatypes   : int, int, int, str, str, str, str

2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Consultation   : When a patient requests a telemedicine session (Patient/System)  
    - Retrieve Consultation : Fetch consultation details using consultation ID (Patient/Doctor)  
    - Update Consultation   : Modify symptoms or reschedule appointment before confirmation  
    - Delete Consultation   : Cancel request before session starts  
8.Emergency Contact & Consent Form

1. STATE:

variable: Attributes   : patientID, emergencyContactName, emergencyContactNumber, relationship, consentGiven, consentDate  
value   : Values      : 880098765432, "Rahul Sharma", "+91-9876543210", "Brother", True, "2025-04-10"  
type    : datatypes   : int, str, str, str, bool, str 


2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Record      : When a patient provides emergency contact details (Patient/Hospital)  
    - Retrieve Record    : Fetch emergency contact and consent details (Hospital/Doctor)  
    - Update Record      : Modify contact details or revoke consent  
    - Delete Record      : Remove data if patient no longer consents  


9.Hospital Admission Form

1. STATE:

variable: Attributes   : admissionID, patientID, patientName, age, gender, reasonForAdmission, insuranceProvider, roomType, paymentMethod, admissionDate, status  
value   : Values      : 950098765432, 880098765432, "Ramesh Kumar", 45, "Male", "Severe Chest Pain", "HDFC Health Insurance", "Private Ward", "Credit Card", "2025-04-10", "Admitted"  
type    : datatypes   : int, int, str, int, str, str, str, str, str, str, str 

2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Admission    : When a patient is admitted to the hospital (Patient/Hospital)  
    - Retrieve Admission  : Fetch admission details using admission ID (Hospital/Admin)  
    - Update Admission    : Modify room type, insurance provider, or payment details  
    - Delete Admission    : Remove record if admission is canceled  

    
    10.Discharge Summary & Feedback Form

1. STATE:

variable: Attributes   : dischargeID, patientID, admissionID, treatmentSummary, doctorNotes, dischargeDate, feedback, rating  
value   : Values      : 960098765432, 880098765432, 950098765432, "Treated for cardiac arrest, stable now", "Continue medications, follow-up in 2 weeks", "2025-04-15", "Good care, excellent service", 5  
type    : datatypes   : int, int, int, str, str, str, str, int 

2. BEHAVIOR:
--------------
CRUD : CREATE / RETRIEVE / UPDATE / DELETE  

    - Create Summary     : When a patient is discharged (Hospital/System)  
    - Retrieve Summary   : Fetch discharge details using discharge ID (Hospital/Patient)  
    - Update Summary     : Modify treatment summary or doctor notes before finalizing  
    - Delete Summary     : Remove record if discharge is reversed  

















'''