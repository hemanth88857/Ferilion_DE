"""Hospital Admission Form

variable: Attributes   : admissionID, patientID, patientName, age, gender, reasonForAdmission, insuranceProvider, roomType, paymentMethod, admissionDate, status
value   : Values      : 950098765432, 880098765432, "Ramesh Kumar", 45, "Male", "Severe Chest Pain", "HDFC Health Insurance", "Private Ward", "Credit Card", "2025-04-10", "Admitted"
type    : datatypes   : int, int, str, int, str, str, str, str, str, str, str
"""


class Hospital:
    hospital_name = "NIMS" # Class Variable

    def __init__(self,patientName, age, gender, reasonForAdmission, admissionDate,paymentMethod): # instance Variables
        self.patientName = patientName
        self.age = age
        self.gender = gender
        self.reasonForAdmission = reasonForAdmission
        self.admissionDate = admissionDate
        self.paymentMethod = paymentMethod


    def patient_details(self): # instance method
        return f"patientName : {self.patientName}, age : {self.age}, gender : {self.gender}, reasonForAdmission :{self.reasonForAdmission}, admissionDate : {self.admissionDate}, paymentMethod:{self.paymentMethod}"

    @classmethod
    def insurance_provider(cls,insuranceProvider):
        return insuranceProvider

    @staticmethod
    def patient_roomType(roomType):
        return roomType

    @property
    def patient_iddischarge(self):
        return  "Patient discharged"