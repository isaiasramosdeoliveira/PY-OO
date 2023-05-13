class Account:
    def __init__(self, name, lastname, balance):
        self.name = name
        self.lastname = lastname
        self.balance = balance

    @property
    def dice(self):
        print("=-"*15)
        print(f"Seus dados: \nNome: {self.name} \nSobrenome: {self.lastname}\nSaldo: {self.balance}")
        print("=-"*15)


account = Account("Isaias", "Ramos", 1200)
    


