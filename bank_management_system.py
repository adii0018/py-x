class Bankaccount:
    Bank_name="ASR BANK !!!🏦"
    def __init__(self,name,balance,acc_no):
        self.name=name
        self._acc_no=acc_no
        self.__balance=balance
        
#Show account details 🌿

    def show_details(self):
        print("\n>>>>>>>>>>>>>> ACCOUNT DETAILS >>>>>>>>>>>>>>>>>>>>>>>>")
        print("Bank name ",Bankaccount.Bank_name)
        print("Name ", self.name)
        print("ACCOUNT NO  ", self._acc_no)
        print("Balance ",self.__balance)

#Deposit money 🌿

    def deposit(self,amount):
        if amount >=0:
            self.__balance += amount
            print("💸",amount,"Deposit Successfully !!!!")
        else:
            print("🛑","Invalid deposit ")

#withdraw money 🌿

    def withdraw(self,amount):
        if amount <=self.__balance:
            self.__balance -= amount
            print("💸",amount,"withdraw Successfully !!!!!")
        
        else:
            print("🛑",amount,"Insufficent balance !!!!!!")

#Get balance 🌿        

    def get_balance(self):
        
        return self.__balance
    

#child class uisng inheritance 🌿
class SavingsAccount(Bankaccount):

 def __init__(self, name, acc_no, balance, interest_rate):
        super().__init__(name, acc_no, balance)
        self.interest_rate = interest_rate

def add_interest(self):
        interest = self.get_balance() * self.interest_rate / 100
        self.deposit(interest)
        print("Interest Added:", interest)
  
# ---------------- MAIN PROGRAM ----------------🌿

print("🏦 WELCOME TO ASR  BANK")

name = input("Enter Account Holder Name: ")
acc_no = int(input("Enter Account Number: "))
balance = float(input("Enter Initial Balance: "))
account = SavingsAccount(name, acc_no, balance, 5)

while True:

    print("\n------ BANK MENU ------")
    print("1. Show Account Details")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Add Interest")
    print("6. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        account.show_details()

    elif choice == 2:
        amount = float(input("Enter Deposit Amount: "))
        account.deposit(amount)

    elif choice == 3:
        amount = float(input("Enter Withdraw Amount: "))
        account.withdraw(amount)

    elif choice == 4:
        print("Current Balance:", account.get_balance())

    elif choice == 5:
        account.add_interest()

    elif choice == 6:
        print("Thank you for using Python Bank")
        break

    else:
        print("Invalid Choice")
