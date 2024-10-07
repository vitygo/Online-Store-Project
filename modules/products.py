import json
import typing
import random
from modules.warehouses import Warehouse

class Product:
    def __init__(self, name: str, 
                 brand: str, 
                 price: float, 
                 description: str, 
                 stock_quantity: int, 
                 product_form: str,
                 product_warehouse_id: int,
                 volume: typing.Optional[int] = None):  
        
        self.product_id = self._generate_product_id()
        self.name = name
        self.category: typing.Optional[str] = None
        self.brand = brand
        self.price = price
        self.description = description
        self.stock_quantity = stock_quantity
        self.product_form = product_form
        self.product_warehouse_id = product_warehouse_id
        self.volume = volume  

        self._add_to_json()
        self._opacity_control()

    def _opacity_control(self):
        with open("data/warehouses.json", "r") as file:
            warehouse_data = json.load(file)
        for warehouse in warehouse_data:
            if warehouse["warehouse_id"] == self.product_warehouse_id:
                if warehouse["warehouse_opacity"] >= self.stock_quantity:
                    warehouse["warehouse_opacity"] -= self.stock_quantity
                else:
                    print("Not enough space!")
                break

        with open("data/warehouses.json", "w") as file:
            json.dump(warehouse_data, file, indent=4)

    def _add_to_json(self):
        product_data = {
            "product_id": self.product_id,
            "name": self.name,
            "category": self.category,
            "brand": self.brand,
            "price": self.price,
            "description": self.description,
            "stock_quantity": self.stock_quantity,
            "product_form": self.product_form,
            "product_warehouse_id": self.product_warehouse_id,
            "volume": self.volume  # Use self.volume directly
        }

        try:
            with open("data/product.json", "r") as file:
                products = json.load(file)
        except FileNotFoundError:
            products = []

        products.append(product_data)

        with open("data/product.json", "w") as file:
            json.dump(products, file, indent=4)

    @classmethod
    def add_product(cls):
        product_name = input("Enter product name: ")
        product_brand = input("Enter product brand: ")
        product_price = float(input("Enter product price: "))
        product_description = input("Enter product description: ")
        product_form = input("Enter product form: ")
        product_quantity = int(input("How many units of this product do you want to add?: "))
        product_warehouse_id = int(input("Enter the warehouse ID for this product: "))  
        product_volume = int(input("Enter the volume of the product: "))  
        product_category_class, _ = cls._valid_product_category()

        product_category_class(product_name,
                               product_brand, 
                               product_price, 
                               product_description, 
                               product_quantity, 
                               product_volume,  # Pass volume here
                               product_form, 
                               product_warehouse_id)

    @staticmethod
    def _valid_product_category():
        user_input = input(f"(1) Fragrance\n"
                           f"(2) Skincare\n"
                           f"(3) Makeup\n"
                           f"(4) Haircare\n"
                           f"(5) Bodycare\n")
        category_class = None
        if user_input == '1':
            category_class = FragranceProduct
        elif user_input == '2':
            category_class = SkincareProduct
        elif user_input == '3':
            category_class = MakeupProduct
        elif user_input == '4':
            category_class = HaircareProduct
        elif user_input == '5':
            category_class = BodycareProduct

        return category_class, user_input

    @staticmethod
    def _generate_product_id() -> int:
        return random.randint(1000000, 5000000)
    
    def edit_product(self):
        pass  
    
    def delete_product(self):
        pass  


class FragranceProduct(Product):
    def __init__(self, name: str, 
                 brand: str, 
                 price: float, 
                 description: str, 
                 stock_quantity: int, 
                 volume: int, 
                 product_form: str,
                 product_warehouse_id: int):
        
        super().__init__(name, brand, price, description, stock_quantity, product_form, product_warehouse_id, volume)
        self.category = 'Fragrance'


class SkincareProduct(Product):
    def __init__(self, name: str, 
                 brand: str, 
                 price: float, 
                 description: str, 
                 stock_quantity: int, 
                 volume: int, 
                 product_form: str,
                 product_warehouse_id: int):
        
        super().__init__(name, brand, price, description, stock_quantity, product_form, product_warehouse_id, volume)
        self.category = 'Skincare'


class MakeupProduct(Product):
    def __init__(self, name: str, 
                 brand: str, 
                 price: float, 
                 description: str, 
                 stock_quantity: int, 
                 volume: int, 
                 product_form: str,
                 product_warehouse_id: int):
        
        super().__init__(name, brand, price, description, stock_quantity, product_form, product_warehouse_id, volume)
        self.category = 'Makeup'


class HaircareProduct(Product):
    def __init__(self, name: str, 
                 brand: str, 
                 price: float, 
                 description: str, 
                 stock_quantity: int, 
                 volume: int, 
                 product_form: str,
                 product_warehouse_id: int):
        
        super().__init__(name, brand, price, description, stock_quantity, product_form, product_warehouse_id, volume)
        self.category = 'Haircare'


class BodycareProduct(Product):
    def __init__(self, name: str, 
                 brand: str, 
                 price: float, 
                 description: str, 
                 stock_quantity: int, 
                 volume: int,  
                 product_form: str,
                 product_warehouse_id: int):
        
        super().__init__(name, brand, price, description, stock_quantity, product_form, product_warehouse_id, volume)
        self.category = 'Bodycare'
