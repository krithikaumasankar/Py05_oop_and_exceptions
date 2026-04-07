#EB BILL CALCULATOR
class EB:
    def __init__(self):
        print("\n\tEB BILL CALCULATOR...!")
        self.units=int(input("Enter number of units: "))
    def display (self):
        amo=0
        if self.units <= 100:
            amo="No amount"
        elif self.units > 100 and self.units <= 200:
            amo += (self.units-100)*1.5
        elif self.units > 200 and self.units <= 300:
            amo += (self.units-200)*2.5 + (100*1.5)
        elif self.units > 300 and self.units <= 400:
            amo += (self.units-300)*4 + (100*1.5) + (100*2.5)
        elif self.units > 400:
            amo += (self.units-400)*5 + (100*4) + (100*2.5) + (100*1.5)
        print("\nUnits used:",self.units,"\nElectricity Bill Amount:",amo)

e=EB()
e.display()
