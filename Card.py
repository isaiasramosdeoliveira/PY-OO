class Bank_Universal:
    def __init__(self, account):
        self.account = account
    
    def pay(self, value):
        if value > self.account.balance:
            print("Saldo insuficiente.")
        else:
            print("Pagamento efetuado com sucesso.")
            print(f"Seu saldo: {self.account.balance - value}")

    def deposit(self, value):
        account.balance = account.balance + value
        print("Depósito feito com sucesso.")

class Bank_Nubank(Bank_Universal):
    def __init__(self, account):
        self.account = account

class Account:
    def __init__(self, name, lastname, balance):
        self.name = name
        self.lastname = lastname
        self.balance = balance

    @property
    def dice(self):
        print("=-"*15)
        print(f"Seus dados: \nNome:{self.name} \nSobrenome:{self.lastname}")
        print("=-"*15)


    
account = Account("Isaias", "Ramos", 1200)
bank_nubank = Bank_Nubank(account)



account.balance
bank_nubank.pay(200)
