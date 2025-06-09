
class Product:

    def __int__(self,p_name,p_price):
        self.p_name = p_name
        self.p_price = p_price


    def product_details(self):
        print(f"p_name : {self.p_name}"
              f"p_type : {self.p_type}"
              f"p_price :{self.p_price}")

    def product_price(self):
        return self.p_price

class Electrical(Product):

    def __init__(self,p_name,p_price,p_type,p_dealprice,p_warranty):
        super().__init__(p_name,p_price)
        self.p_type = p_price
        self.p_dealPrice = p_price
        self.p_warranty =  p_price
        self.cart = []


    def complete_product_details(self):
        print(f"p_name : {self.p_name}\n"
              f"p_price : {self.p_price}\n "
              f",p_type : {self.p_type}\n"
              f",p_dealprice : {self.p_dealPrice}\n"
              f",p_warranty : {self.p_warranty}")



class cart(Electrical):

    def __init__(self):
        self.cart = []


