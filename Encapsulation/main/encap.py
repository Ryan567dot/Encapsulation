#Encapsulation

class BkashBank:
    def __init__(self,Name,ID,Balance):
        self.Name = Name
        self.ID = ID
        self.Balance = Balance
        
class BkashLoan(BkashBank):
    pass

customer1 = BkashBank("Ryan",400,4500)
customer2 = BkashBank("Zaheen",300,3500)

print(customer1.Name)
