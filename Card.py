class Bank:
    def __init__(self,value, account):
        self.value = value
        self.account = account
    
    def pay(self):
        if self.value > self.account.balance:
            print("Saldo insuficiente.")
        else:
            print("Pagamento efetuado com sucesso.")
            print(f"Seu saldo: {self.account.balance - self.value}")

    def deposit(self, value):
        account.balance = account.balance + value
        print("Depósito feito com sucesso.")

class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    
    

account = Account("isaias", 1200)
bank = Bank(500, account)

bank.pay()



