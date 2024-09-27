import json

class Product:
    def __init__(self, id_product, name, description, category, price, warehouse_id):
        self.id_product = id_product
        self.name = name
        self.description = description
        self.category = category
        self.price = price
        self.warehouse_id = warehouse_id

        #автоматичне додавання нового складу в базу данних
        with open("data/product.json", "r") as file:
            warehouse_data = json.load(file)
            
        cheker = False
        for product in warehouse_data: #перевірка чи такий продукт є
            if product["id_product"] == self.id_product:
                cheker = True
                
        if not cheker:
            warehouse_data.append({"id_product": self.id_product, 
                            "name": self.name, 
                            "description": self.description,
                            "category": self.category,
                            "price": self.price,
                            "warehouse_id": self.warehouse_id}
                            )
                
            with open("data/product.json", "w") as file:
                json.dump(warehouse_data, file, indent=4)

 
    def __str__(self):
         return (f"product id: {self.id_product}\n"
               f"product name: {self.name}\n"
               f"product description: {self.description} units\n"
               f"prduct catrgory: {self.category}\n"
               f"product price: {self.price}\n"
               f"warehouse id: {self.warehouse_id}\n")
               
    @staticmethod
    def take_product():
        while True:
            product_id = int(input("enter product id: "))

            with open("data/product.json", "r") as file:
                products = json.load(file)
                for product in products:
                    if product_id == product['id_product']:
                        p_id = product["id_product"]
                        p_name = product['name']
                        p_descr = product['description']
                        p_cat = product['category']
                        p_price = product['price']
                        p_ware_id = product['warehouse_id']
                        product = Product(p_id, p_name, p_descr, p_cat, p_price, p_ware_id)
                        print(product)
                        product.change_product(product_id)
                    else:
                        print("product not found")
    
    def change_product(self, product_id):
        print(f"1 change id"
              f"2 change name"
              f"3 chanege description"
              f"4 change category"
              f"5 change warehouse id"

        )
        parameter = None
        obj_parameter = None

        while True:
            user_choice = input("enter your choice: ")
            if user_choice == "1":
                self.id_product = Product.availiable_id()
                parameter = 'id_product' # те що буде змінюватись
                obj_parameter = self.id_product 
            elif user_choice == "2":
                self.id_product = input("new name: ")
                parameter = 'name' # те що буде змінюватись
                obj_parameter = self.name 
            elif user_choice == "3":
                self.id_product = input("new description: ")
                parameter = 'description' # те що буде змінюватись
                obj_parameter = self.description 
            elif user_choice == "4":
                self.id_product = input("new description: ")
                parameter = 'description' # те що буде змінюватись
                obj_parameter = self.description 
            elif user_choice == "5":
                self.id_product = input("new category: ")
                parameter = 'category' # те що буде змінюватись
                obj_parameter = self.category
            elif user_choice == "6":
                break

            with open("data/product.json", 'r') as file:
                products = json.load(file)

            for product in products:
                if product["id_product"] == product_id:
                    product[parameter] = obj_parameter

            with open("data/product.json", 'w') as file:
                json.dump(products, file, indent=4)
    
    @staticmethod
    def add_product(): #добавлення нового продукту
        id_product:int = Product.availiable_id()
        name:str = input("enter product name: ")
        description:str = input("enter product description: ")
        category:str = Product.chose_category(name)
        price: float = float(input("enter price: "))
        warehouse_id:int = Product.chose_warehouse_by_id()
        Product(id_product, name, description, category, price, warehouse_id)

    @staticmethod
    def chose_category(name): #функція вибору категорії продукту
        availiable_categoris = ["fragrances", 'skincare', 'makeup', 'haircare', 'body Care']
        print('Avaliable caregory')
        for category in availiable_categoris:
            print(category, end="\n")
        while True:
            input_category = input(f'Enter category for {name}: ')
            if input_category in availiable_categoris:
                return input_category
            
    @staticmethod
    def chose_warehouse_by_id(): #перевірка айді чи такий склад є
        with open("data/warehouses.json", "r") as file:
            warehouse_data = json.load(file)
            
            print('AVALIABLE WAREHOUSES')
            for warehouse in warehouse_data:
                print(f"Id: {warehouse['id']}\nName: {warehouse['name']}")

            while True:
                input_id = int(input("enter warehouse id: "))
                for warehouse in warehouse_data:
                    if warehouse['id'] == input_id:
                        return input_id
                    else:
                        print('Wrong warehouse id')
    @staticmethod
    def availiable_id(): #перевірка чи такий айді не занятий
        while True:
            user_input = int(input("new id: "))
            with open("data/product.json", "r") as file:
                warehouse_data = json.load(file)
            cheker = False
            for product in warehouse_data: #перевірка чи такий продукт є
                if product["id_product"] == user_input:
                    cheker = True
            if not cheker:
                return user_input
            else:
                print("this id is not abaliable")