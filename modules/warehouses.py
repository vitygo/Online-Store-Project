import json

class Warehouse:
    def __init__(self, id_number:int, name:str, capacity:int) -> None:
        self.id_number = id_number
        self.name = name
        self.capacity = capacity

        #автоматичне додавання нового складу в базу данних
        with open("data/warehouses.json", "r") as file:
            warehouse_data = json.load(file)
        
        cheker = False
        for warehouse in warehouse_data:
            if warehouse["id"] == self.id_number:
                cheker = True

        if not cheker:
            warehouse_data.append({"id": self.id_number, 
                            "name": self.name, 
                            "copacity": self.capacity})
            
            with open("data/warehouses.json", "w") as file:
                json.dump(warehouse_data, file, indent=4)
       


    def __str__(self) -> str:
        return (f"Werehouse id: {self.id_number}\n"
               f"Werehouse name: {self.name}\n"
               f"Werehouse capacity: {self.capacity} units\n"
               f"Werehouse products amount: {...}\n")
               

    def add_warehouse(): #реєстрація створення нового складу
        id_name = int(input("id: "))
        name = input("name: ")
        copacity = int(input("місткість: "))
        Warehouse(id_name, name, copacity)

    @staticmethod
    def product_amount():
        while True:
            try:
                user_input = int(input('Enter warehouse id: '))
            except:
                print('wrong id')
            else:
                with open("data/product.json", "r") as file:
                    product_data = json.load(file)
                cnt = 0
                for product in product_data:  
                    if product["warehouse_id"] == user_input:
                        cnt += 1
                    return 
                
    @staticmethod
    def show_products_amount():
        curent_warehouse = Warehouse.take_warehouse()
        with open('data/product.json', 'r') as file:
            product_data = json.load(file)
        cnt = 0
        for product in product_data:
            if product['warehouse_id'] == curent_warehouse.id_number:
                cnt += 1
        print(f"In warehouse id:{curent_warehouse.id_number} {cnt} products")
                

    @staticmethod
    def take_warehouse():
        while True:
            warehouse_id = int(input("enter warehouse id: "))

            with open("data/warehouses.json", "r") as file:
                warehouses = json.load(file)
                for warehouse in warehouses:
                    if warehouse['id'] == warehouse_id:
                        w_id = warehouse["id"]
                        w_name = warehouse['name']
                        w_copacity = warehouse['copacity']
                        curent_warehouse = Warehouse(w_id, w_name, w_copacity)
                        return curent_warehouse
                else:
                    print("warehouse not found")