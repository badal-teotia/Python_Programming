# Creating account.

class Account:
    def __init__(self, name:str, acc_no:int, acc_bal:float):
        self.name=name
        self.acc_no=acc_no
        self.acc_bal=acc_bal

    def deb(self, R:float):
        self.acc_bal-=R
        
    def crd(self, T:float):
        self.acc_bal+=T
        
    def bal(self):
        return self.acc_bal

credit=float(input("Amount to credit:"))
debit=float(input("Amount to debit:"))

A1=Account("Person", 1234567890, 2000)
A1.deb(debit)
A1.crd(credit)

print(A1.name, "has", A1.bal(), "in his", A1.acc_no,"account.")
