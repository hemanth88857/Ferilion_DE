

#Login
class LoginForm:
    login_type = "Internet Banking"
    def __init__(self,username, password,biometeric,name):

        self.username = username
        self.password = password
        self.biometeric = biometeric
        self.name = name

    def login_details(self):
        return f" name = {self.name}, username :{self.username}, password :{self.password},biomertic :{self.biometeric}, status :{self.account_status("Active")}"

    def account_status(self,accountstatus):
        return accountstatus

    @classmethod
    def login_type(cls):
        return cls.login_type

    @staticmethod
    def isbiometricenabled():
        return True
    @staticmethod
    def isbiometriceisable():
        return False

#New Account Opening


class AccountOpening:

    Account_details = []

    def __init__(self,fullName,dob,gender,address,contactNumber,customerId,account_no):
        self.fullName = fullName
        self.dob = dob
        self.gender = gender
        self.address = address
        self.contactNumber = contactNumber
        self.customerId = customerId
        self.account_no = account_no
        AccountOpening.Account_details.append(self)

    def fetch_account_details(self):
        return f"fullName: {self.fullName},dob : {self.dob},gender : {self.gender},address :{self.address},contactNumber:{self.contactNumber},customerId:{self.customerId},account_no:{self.account_no}"


    def fetch_account_no(self):
        return self.account_no

    def fetch_account_Data(self,details:str):

        if details.lower() == "accountNumber":
            return self.account_no
        elif details.lower() == "customerid":
            return  self.customerId
        else:
            return f"fullName: {self.fullName},dob : {self.dob},gender : {self.gender},address :{self.address},contactNumber:{self.contactNumber},customerId:{self.customerId},account_no:{self.account_no}"



#Deposit

class Deposit:

    deposit_type = "Atm Deposit"

    def __init__(self,depositID,accountNumber,depositorName,depositType,depositAmount,status):
        self.depositID = depositID
        self.accountNumber = accountNumber
        self.depositorName = depositorName
        self.depositType = depositType
        self.depositAmount = depositAmount
        self.status = status


    def Deposit_Details(self):
        return f"depositID :{self.depositID},accountNumber:{self.accountNumber},depositorName:{self.depositorName},depositType:{self.depositType},depositAmount:{self.depositAmount},status:{self.status}"

    @staticmethod
    def Deposit_status(status):
        return status


    def Deposit_ID(self, depositid):
        return depositid




class Login:

    logintype = "Internet Banking"

    def __init__(self,username,password,customerid):
        self.username = username
        self.password = password
        self.customerid = customerid


    def login_details(self):
        return f"username :{self.username} , password : {self.password} ,customerid :{self.customer_id} "

    @staticmethod
    def Grettings():
       return "Login Successful"


    @classmethod
    def login_type(cls):
        return cls.logintype


class AmountWithdraw:

    account_count  = 0

    def __init__(self,account_holder ,account_number,balance = float):

        self.balance  = balance
        self.account_number = account_number
        self.account_holder = account_holder
        AmountWithdraw.account_count += 1

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Current Bal : {self.balance}"
        else:
            return f"Add amount Grater than 0"


    def withdraw(self, amount):
        if self.balance >= amount and amount > 0:
            self.balance -= amount
            return f"Amount withdrawn : {amount} and Balance amount is : {self.balance}"
        elif amount < 0 :
            return f"give valid funds"
        else:
            return f"No Sufficient Funds"

    def display_account_info(self):
        return (f"Account Holder : {self.account_holder} "
                f", Account number : {self.account_number} "
                f"and Balance amount is : {self.balance}")


    # def account_number(self,accountnumber):
    #     return accountnumber

    @classmethod
    def get_total_accounts(cls):
        return cls.account_count

    @staticmethod
    def is_valid_account_number(account_num):
        if len(account_num) == 10 and account_num.isdigit():
            return  account_num
        return f"Invalid Account Number"
        # return  len(account_number) == 10 and account_number.isdigit()