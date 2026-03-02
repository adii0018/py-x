#privte capsulation 
class atm:
    def __init__(self,balance):
        self._balance=balance
    def display(self):
      print(self._balance)
a=atm(20000)
a.display()

print(".......................................")
