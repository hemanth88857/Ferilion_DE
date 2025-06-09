from Python.Classes.ClassObjects.Banking_class import AmountWithdraw
from Python.ConstantData.Banking_Data import customersdetails
from Python.log_create.New_log_create import logger





print(logger)
try :
    a = 10/9
except Exception as exe:
    logger.error("An exception %s", exe)
    print(exe)
else:
    logger.info(f"alog as {a}")








# Checking if an account number is valid
print(AmountWithdraw.is_valid_account_number("1234567890"))  # True
print(AmountWithdraw.is_valid_account_number("12345ABC90"))  # False

res  = AmountWithdraw.is_valid_account_number("1234567899")
print(res)

# Creating Bank Account instances
account1 = AmountWithdraw("Alice", "1234567890", 1000.0)
account2 = AmountWithdraw("Bob", "0987654321", 500.0)

# Display account details
account1.display_account_info()
account2.display_account_info()

# Depositing money into accounts
account1.deposit(200)
account2.deposit(150)

# Withdrawing money from accounts
account1.withdraw(300)
account2.withdraw(700)

# Display updated account details
account1.display_account_info()
account2.display_account_info()

# Total accounts created
print("\nTotal Accounts:", AmountWithdraw.get_total_accounts())



# Objects Creation
Accounts = []
for each in customersdetails:
    Account = AmountWithdraw(each["fullName"],each["contactNumber"],each["balance"])
    Accounts.append(Account)


acc = AmountWithdraw.is_valid_account_number("9123456789")
def transaction(acct):
    for each in Accounts:
        if each.account_number == acc :
           transaction_type =  input("you want withdraw/deposit : ")
           if transaction_type.lower() == "withdraw":
               withdraw = each.withdraw(float(input("enter amount: ")))
               print(withdraw)
               break
           elif transaction_type.lower() == "deposit":
               deposit = each.deposit(float(input("enter amount: ")))
               print(deposit)
               break
           else:
               print("select withdraw/deposit")
               transaction(acc)
               break
    else:
        print(acc)


transaction(acc)
