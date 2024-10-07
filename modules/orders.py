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
        
    


