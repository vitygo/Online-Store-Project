import json
import random
import re

class Client:
    def __init__(self, first_name:str, second_name:str, email:str):
        self.client_id:int = self.generate_client_id()
        self.first_name = first_name
        self.second_name = second_name
        self.email = email
        
        self.add_to_json() #додавання до json під час ініціалізації


    @classmethod
    def add_client(cls):
        first_name = input()
        second_name = input()
        email = cls.valid_email()
        cls(first_name, second_name, email)
    

    def add_to_json(self):
        with open("../data/clients.json", "r") as file:
            client_data = json.load(file)

            client = {"client_id": self.client_id,
                      "first_name": self.first_name,
                      "second_name": self.second_name,
                      "email": self.email}
            
            client_data.append(client)
        
        with open("../data/clients.json", "w") as file:
            json.dump(client_data, file, indent=4)

    @staticmethod
    def valid_email() ->str:
        while True:
            user_email = input()

            email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

            if re.match(email_regex, user_email):
                return user_email
            else:
                print("Wrong email!")

    @staticmethod
    def generate_client_id() ->int:
        genarated_id = random.randint(100000, 500000)
        return genarated_id
    

    



Client.add_client()