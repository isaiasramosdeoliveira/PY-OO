class Account:
    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age
    
    def sayMyName(self):
        print(f"Seu nome: {self.name}")
    
    


account = Account("isaias", "ramos", 19)

account.sayMyName()