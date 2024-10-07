import json
from modules.products import Product

class Order:
    def __init__(self, client_id:int, date:str):
        self.client_id = client_id
        self.date = date
        self.products = []
        self.total_price:int = 0

    def edit_order(self):
        ...
    
    def add_to_order_list(self):
        ...
        
        #функція яка бере товар і змінює місткість складу а також кількість конкретного товару
    def __take_from_warehouse(self, product_id, how_many):
        with open("data/product.json") as file:
              product_data = json.load(file)

        for product in product_data:
            if product["product_id"] == product_id:
                product["stock_quantity"] -= how_many
                with open("data/product.json") as file:
                    product.dump(product_data, file, indent=4)
                with open("data/warehouses.json") as file:
                    warehouse_data = json.load(file)
                
                for warehouse in warehouse_data:
                    if warehouse["id"] == product["product_warehouse_id"]:
                        warehouse["copacity"] += how_many
                
                with open("data/warehouses.json") as file:
                    json.dump(warehouse_data, file, indent=4)