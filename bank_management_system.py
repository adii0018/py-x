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
    

        
