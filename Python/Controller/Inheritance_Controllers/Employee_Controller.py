from Classes.Inhertaince.Employee import Manager


manager1 = Manager("ravi",124000,"sis345","IT","5")
print(manager1.display_info())
print(manager1.display_manager_info())

print(manager1.apply_raise(15))

print(manager1.approve_leave("ram"))

