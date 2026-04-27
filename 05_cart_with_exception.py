class online_cart:
    def __init__(self):
        self.cart = []

    def add_item(self):
        name = input("Name: ")

        # Quantity input with exception handling
        while True:
            try:
                qty = int(input("Quantity: "))
                if qty <= 0:
                    print("Quantity must be positive")
                    continue
                break
            except ValueError:
                print("Enter valid integer for quantity")

        # Price input with exception handling
        while True:
            try:
                price = float(input("Price: "))
                if price <= 0:
                    print("Price must be positive")
                    continue
                break
            except ValueError:
                print("Enter valid number for price")

        return (name, qty, price)

    def manage_cart(self):
        # Number of items with exception handling
        while True:
            try:
                n = int(input("Enter number of items: "))
                if n <= 0:
                    print("Enter positive number")
                    continue
                break
            except ValueError:
                print("Enter valid integer")

        for i in range(n):
            print(f"\nItem {i+1}")
            item = self.add_item()
            self.cart.append(item)

        self.cart = tuple(self.cart)

    def subtotal(self):
        return sum(r[1] * r[2] for r in self.cart)

    def discount(self):
        if self.subtotal() >= 3000:
            return self.subtotal() * 0.10
        return 0

    def gst(self):
        return self.subtotal() * 0.05

    def total(self):
        return self.subtotal() - self.discount() + self.gst()

    def bill(self):
        print(f"{'BILL':^50}")
        print("-"*50)
        print(f"{'Name':<20}{'Quantity':^15}{'Price':>15}")
        print("-"*50)

        for r in self.cart:
            print(f"{r[0]:<20}{r[1]:^15}{r[2]:>15.2f}")

        print("-"*50)
        print(f"{'Subtotal':<35}{self.subtotal():>15.2f}")
        print(f"{'Discount(10%)':<35}{-self.discount():>15.2f}")
        print(f"{'GST(5%)':<35}{self.gst():>15.2f}")
        print("-"*50)
        print(f"{'Grand Total':<35}{self.total():>15.2f}")

c = online_cart()
c.manage_cart()
c.bill()
