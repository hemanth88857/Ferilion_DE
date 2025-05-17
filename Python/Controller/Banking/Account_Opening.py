from Classes.ClassObjects.Banking_class import AccountOpening
from  ConstantData.Banking_Data import customersdata



account0 = AccountOpening("Hemanth","1993-12-1","Male","hyd","8885742425","CUST1001","4441169087")


# print(account0.fetch_account_details())

customers = customersdata
for each in customers:
    # print(each["fullName"])
    AccountOpening(each["fullName"], each["dob"], each["gender"], each["address"], each["contactNumber"], each["customerId"],each["account_no"])



# print(AccountOpening.Account_details[1].)

# for each in AccountOpening.Account_details:
#     print(each.fetch_account_details())
#     # print(each.fetch_account_details())
#     # print(each.fetch_account_no())
#     # print(each.fetch_account_Data("Customerid"))
#
#     if each.fetch_account_Data("Customerid") == "CUST1002":
#         print(each.fetch_account_details())
#
#


