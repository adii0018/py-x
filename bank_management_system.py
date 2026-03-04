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
       

