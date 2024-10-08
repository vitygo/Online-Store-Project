from modules.warehouses import Warehouse
from modules.products import Product
from modules.clients import Client
import json

def main():
    user_input = input(f"(1)as user\n"
                       f"(2)as admin\n"
                    )
    if user_input == "1":
        user_autoristation()
    elif user_input == "2":
        if admin_autoristion():
            admin_menu()
    



def admin_autoristion():
    user_input = input(f"(1)sign in as admin\n"
                       f"(2)create admin\n"
                    )
    
    if user_input == '1':
        admin_input = int(input("enter your admin id: "))

        with open("data/autorisation_data.json", "r") as file:
            autorisation_data = json.load(file)

        for admin in autorisation_data:
            if admin['admin_id'] == admin_input:
                while True:
                    admin_password = input(f"Вввдіть паролб для {admin['admin_id']}: ")
                    if admin_password == admin['password']:
                        return True
                    else:
                        print("неправильний пароль")
    elif user_input == "2":
        with open("data/autorisation_data.json", "r") as file:
            autorisation_data = json.load(file)
        
        admin_id_create = int(input("enter id: "))
        enter_password = input("enter password: ")

        admin_dict = {"admin_id": admin_id_create,"password": enter_password}
        
        autorisation_data.append(admin_dict)

        with open("data/autorisation_data.json", "w") as file:
            json.dump(autorisation_data, file, indent=4)
        
            


def admin_menu():
    while True:
        user_input = input(f"(1)add warehouse\n"
                           f"(2)add product\n"
                           f"(3)edit product\n"
                           f"(4)Warehouse info\n"
                           f"Enter your choice:")

        if user_input == "1":
            Warehouse.add_warehouse()
        elif user_input == "2":
            Product.add_product()
        elif user_input == "3":
            Product.take_product()
        elif user_input == "4":
            Warehouse.show_products_amount()
        


def user_autoristation():
    user_input = input(f"(1)sign up\n"
                       f"(2)log in\n"
                    )
    
    if user_input == "1":
        client = Client.add_client()
        print("sucssesful registration!")
        client_menu(client)
    elif user_input == "2":
        if Client.log_in():
            client_menu()
           
    
def client_menu(client_id):
    while True:
        user_input = input(f"(1)Search by category\n"
                        f"(2)Search by name\n"
                        f"(3)Show cart\n"
                        f"(4)Show purchase history\n"
                        f"Enter your choice: ")

        if user_input == "1":
            ...
        elif user_input == "2":
            ...
        elif user_input == "3":
            ...
        elif user_input == "4":
            ...

            

                

if __name__ == "__main__":
    main()