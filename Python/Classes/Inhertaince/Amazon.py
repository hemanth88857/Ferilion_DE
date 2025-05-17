class Amazon_Products:
    products  = {
    "Apple": 80000,
    "Samsung": 60000,
    "OnePlus": 45000,
    "Realme": 20000,
    "Xiaomi": 18000,
    "Vivo": 22000,
    "Oppo": 23000,
    "Motorola": 25000,
    "Google": 70000,
    "Nothing": 30000,
    "Lava": 10000,
    "Micromax": 9000,
    "Karbonn": 8000,
    "Intex": 7500,
    "Xolo": 8500,
    "LYF": 7000,
    "Itel": 6500,
    "iBall": 6000,
    "Celkon": 5500,
    "Spice": 5000
}


    products_quantity = {
    "Apple": 5,
    "Samsung": 6,
    "OnePlus": 8,
    "Realme": 5,
    "Xiaomi": 8,
    "Vivo": 7,
    "Oppo": 10,
    "Motorola": 9,
    "Google": 4,
    "Nothing": 3,
    "Lava": 6,
    "Micromax": 5,
    "Karbonn": 4,
    "Intex": 3,
    "Xolo": 2,
    "LYF": 3,
    "Itel": 4,
    "iBall": 2,
    "Celkon": 3,
    "Spice": 2
}

    @classmethod
    def search_item(cls,item):
        return True if item in cls.products else False
        # if item in cls.products:
        #     return  "item available"
        # return  "item not Available"

class Price(Amazon_Products):
    price_Value = 0
    max_discount = 50
    total_val = 0

    @classmethod
    def price_cal(cls, product_name, quantity):
        if product_name in Amazon_Products.products and quantity > 1:
            t_price = (Amazon_Products.products[product_name]) * quantity
            Price.price_Value = t_price
            return  t_price
        raise TypeError("Check Name/Quantity")


    @classmethod
    def discount(cls,dis:int):
        if Price.price_Value != 0:
            discount_price  = (Price.price_Value * dis)/100
            return Price.price_Value - discount_price
        return f"Please add to price_cal frist"







#
class Shopping(Price):
    cart = {}

    # def __init__(self):
    #     # super().__init__()
    #     self.cart = {}

    @classmethod
    def cart_items(cls):
        return cls.cart

    @classmethod
    def add_cart(cls,item,quantity):
        if item in Amazon_Products.products:
            Shopping.cart[item] = quantity
            # Shopping.total_price()
        else:
            raise TypeError("The given item not Available")

    @classmethod
    def remove_item(cls,item,quantity):
        if item in cls.cart:
            cls.cart[item] -= quantity
            Shopping.total_price()
        else:
            return f"Item not added"

    @classmethod
    def delete_cart(self):
        if len(self.cart) >=1:
            self.cart.clear()
            self.cart_items()

    @classmethod
    def total_price(cls):
        if len(Shopping.cart) >= 1:
            for each in Shopping.cart:
                val = Amazon_Products.products[each] * Shopping.cart[each]
                Price.total_val += val
        print(f"Cart Value is Rs{Price.total_val}")
