class Employee:
    def __init__(self,Name,Salary):
        self.__Name = Name
        self.__Salary = Salary
        
    def GetName(self):
        print(f"Employee Name: {self.__Name}")
        
    def SetName(self,NewName):
        self.__Name = NewName
        print("Name updated successfully")
        
Ryan = Employee("Ryan",80000)

print(Ryan.GetName())

Ryan.SetName("Sarker")
