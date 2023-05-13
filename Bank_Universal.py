from Account import account
class Bank_Universal():
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

    

bank = Bank_Universal(account)
bank.pay(200)
account.dice()
