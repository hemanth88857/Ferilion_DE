from Python.Classes.Inhertaince.Amazon import Shopping,Amazon_Products,Price
from Python.Classes.Inhertaince.Amazon import Amazon_Products

# from Python.Classes.Inhertaince.Amazon import Amazon_Products,Price



# print(Amazon_Products.search_item("Vivo"))
#
# print(Price.price_cal("Vivo",5))
#
# # p1 = Price()
# # p1 = Price.price_cal("Vivo",5)
# print(Price.discount(45))
#
# p2 = Shopping()
# p2.add_cart("Vivo",5)
# print(p2.cart_items())
#
# p2.remove_item("Vivo",3)
# print(p2.cart_items())
#
# p2.delete_cart()
# print(p2.cart_items())


# print(Shopping.max_discount)



Shopping.add_cart("Vivo",5)
Shopping.add_cart("Oppo",5)
Shopping.remove_item("Oppo",3)

# p1 = Shopping.price_cal("Vivo",4)
# print(p1)

# print(Shopping.discount(4))
# print(Shopping.cart_items())
# print(Shopping.total_price())