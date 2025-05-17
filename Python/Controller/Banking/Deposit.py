from Classes.ClassObjects.Banking_class import Deposit



transfer1 = Deposit("","676394873943","Hemanth","imps","5988","")

print(transfer1.Deposit_Details())

transfer1.depositID = transfer1.Deposit_ID("97")
print(transfer1.Deposit_ID("97"))
print(transfer1.Deposit_Details())


if len(transfer1.depositID) >= 1:
    transfer1.status = transfer1.Deposit_status("Done")
else:
    transfer1.status = transfer1.Deposit_status("Fail")


print(transfer1.Deposit_Details())


Deposited = Deposit.Deposit_status("done")

if Deposited.lower() == "done":
    pass

