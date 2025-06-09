
from Python.Classes.ClassObjects.Banking_class import  LoginForm
from  Python.ConstantData.Banking_Data import bankcustomers

customer1 = LoginForm("hemanth","Cherry2sush",biometeric= False,name="cust001")
customer1.isbiometricEnabled()

print(customer1.username,customer1.password,customer1.biometeric)

customer1.biometeric = customer1.isbiometricEnabled()
customer1.biometeric = customer1.isbiometricDisable()

customer1.account_status("Active")
print(customer1)

print(customer1.biometeric)
print(customer1.username,customer1.password,customer1.biometeric)
print(customer1.login_details())

bank_customers = bankcustomers

l=0
k=None
for each in bank_customers:

    each = LoginForm(bank_customers[each]["username"], bank_customers[each]["password"], biometeric=bank_customers[each]["biometric"],name= each)


print(k.login_details())

