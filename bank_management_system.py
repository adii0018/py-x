class bankaccount:
    bank_name="adii bank "
    def __init__(self,name,acc_no,balance):
        self.name=name
        self.__acc_no=acc_no
        self._balance=balance
    #show 
    def show_detail(self):
       print("Bank name ❄️",bankaccount.bank_name)
       print("name ❄️",self.name)
       print("Account NO ❄️",self.__acc_no) 
       print("Balance ❄️",self._balance)
       # Deposit Money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("₹", amount, "Deposited Successfully❤️")
        else:
            print("Invalid Deposit Amount😂")

    # Withdraw Money
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("₹", amount, "Withdrawn Successfully")
        else:
            print("Insufficient Balance")
    # Get Balance (Private variable access)
    def get_balance(self):
        return self.__balance
    # Withdraw Money
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("₹", amount, "Withdrawn Successfully")
        else:
            print("Insufficient Balance")

# Get Balance (Private variable access)
    def get_balance(self):
        return self.__balance


# Child Class using Inheritance
class SavingsAccount(BankAccount):

    def __init__(self, name, acc_no, balance, interest_rate):
        super().__init__(name, acc_no, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.get_balance() * self.interest_rate / 100
        self.deposit(interest)
        print("Interest Added:", interest)