from Classes.ClassObjects.Banking_class import  Login
from ConstantData.Banking_Data import customersdata
from  ConstantData.Banking_Data import login_credentials


logincredentials = []

for each in login_credentials:

    each  = Login(each["username"],each["password"],each["customerid"])
    logincredentials.append(each)

customer_id = ""
for each in logincredentials:
    # "username": "alice01", "password":
    if each.username == "alice01" and each.password == "pass123":
        print(Login.Grettings())
        print(each.customerid)
        customer_id = each.customerid


for each in customersdata:
    if each["customerId"] == customer_id:
        print(each)
