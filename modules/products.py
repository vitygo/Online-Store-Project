import json 


class Product:
    def __init__(self,  product_id:int, name:str, brand:str, price:float, description:str, stock_quantity:int, product_form:str):
        self.product_id = product_id
        self.name = name
        self.category = None
        self.brand = brand
        self.price = price
        self.description = description
        self.stock_quantity = stock_quantity
        self.product_form = product_form

        def add_product(self):
            ...
        def edit_product(self):
            ...
        def delete_product(self):
            ...
        def search_product(self):
            ...
        def add_to_cart(self):
            ...
        
class FragranceProduct(Product):
    def __init__(self, product_id:int, name:str, brand:str, price:float, description:str, stock_quantity:int, volume:int, product_form:str):
        super().__init__(product_id, name, brand, price, description, stock_quantity, product_form)
        self.category: str = 'Fragrance'
        self.volume = volume
        
class SkincareProduct(Product):
    def __init__(self, product_id:int, name:str, brand:str, price:float, description:str, stock_quantity:int, volume:int, product_form:str):
        super().__init__(product_id, name, brand, price, description, stock_quantity, product_form)
        self.category: str = 'Skincare'
        self.volume = volume

class MakeupProduct(Product):
    def __init__(self, product_id:int, name:str, brand:str, price:float, description:str, stock_quantity:int, volume:int, product_form:str):
        super().__init__(product_id, name, brand, price, description, stock_quantity, product_form)
        self.category: str = 'Makeup'
        self.volume = volume

class HaircareProduct(Product):
    def __init__(self, product_id:int, name:str, brand:str, price:float, description:str, stock_quantity:int, volume:int, product_form:str):
        super().__init__(product_id, name, brand, price, description, stock_quantity, product_form)
        self.category: str = 'Haircare'
        self.volume = volume

class BodycareProduct(Product):
    def __init__(self, product_id:int, name:str, brand:str, price:float, description:str, stock_quantity:int, volume:int, product_form:str):
        super().__init__(product_id, name, brand, price, description, stock_quantity, product_form)
        self.category: str = 'Bodycare'
        self.volume = volume
