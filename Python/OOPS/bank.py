class Bank:
    def data(self,id,name,accno):
        self.id = id
        self.name = name
        self.accno = accno
        self.min_balance = 2000
        self.balance = self.min_balance
    def deposit(self,cash):
        self.cash = cash
        self.balance = self.balance + self.cash
    def withdraw(self,cash):
        self.cash = cash
        self.balance = self.balance - self.cash
    def print_balance(self):
        print(self.id,self.name,self.accno,self.balance)

bank = Bank()
bank.data(1, "Jake", 1001)
bank.deposit(2000)
bank.print_balance()
bank.withdraw(2000)
bank.print_balance()