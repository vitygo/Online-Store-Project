import random 
import json 

class Warehouse:
    def __init__(self, 
                 warehouse_name:str,
                 warehouse_opacity:int
                 ):
        
        self.warehouse_id = self.__genarete_warehouse_id()
        self.warehouse_name = warehouse_name
        self.warehouse_opacity = warehouse_opacity
         
        self.__add_to_json()
    
    @classmethod
    def add_warehouse(cls):
        warehouse_name = input("enter warehouse name: ")
        warehouse_opacity = int(input("enter warehouse opacity: "))
        cls(warehouse_name, warehouse_opacity)

    def search_product(self):
        ...
    def add_to_cart(self):
        ...
    def search_product_by_category(self):
        ...

    def __genarete_warehouse_id(self):
        genarated_id = random.randint(1000, 5000)
        return genarated_id
    
    def __add_to_json(self):
         with open("data/warehouses.json", "r") as file:
            warehouse_data = json.load(file)

            warehouse = {"warehouse_id": self.warehouse_id,
                      "warehouse_name": self.warehouse_name,
                      "warehouse_opacity": self.warehouse_opacity,
                      }
            
            warehouse_data.append(warehouse)
        
         with open("data/warehouses.json", "w") as file:
            json.dump(warehouse_data, file, indent=4)