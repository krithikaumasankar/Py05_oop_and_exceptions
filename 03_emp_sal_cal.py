#EMPLOYEE SALARY CALCULATION
class employee:
    def __init__(self):
        print("\n\tEMPLOYEE SALARY CALCULATOR....\n")
        self.id = int(input("Enter employee ID: "))
        self.name = input("Enter employee name: ")
        self.basic = int (input("Enter employee basic salary: "))
    def display(self):
        da = 0.10 * self.basic
        hra = 0.20 * self.basic
        gp = da + hra + self.basic
        print("\nEmployee Details..")
        print("\nEmployee ID: ", self.id,"\nEmployee Name: ", self.name,"\nAllowance: ",da,"\nHouse rent allowance: ",hra,"\nGross pay: ",gp)
e = employee()
e.display()
