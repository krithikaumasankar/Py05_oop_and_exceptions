#ATM
class InvalidPINError(Exception):
    pass

class AccountBlockedError(Exception):
    pass

class ATM:
    def __init__(self, pin, balance):
        self.pin = pin
        self.balance = balance
        self.attempts = 0

    def verify_pin(self):
        while True:
            try:
                if self.attempts >= 3:
                    raise AccountBlockedError("Account Blocked")

                entered_pin = int(input("\nEnter PIN: "))

                if entered_pin != self.pin:
                    self.attempts += 1
                    raise InvalidPINError("Wrong PIN...!")

                print("PIN Verified...!")
                self.attempts = 0
                return True

            except InvalidPINError as e:
                print(e)

            except AccountBlockedError as e:
                print(e)
                return False

    def withdraw(self):
        try:
            amount = float(input("\nEnter amount: "))

            if amount <= 0:
                raise ValueError("Amount must be positive")

            if amount > self.balance:
                raise Exception("Insufficient Balance")

            self.balance -= amount
            print("\nWithdrawn:", amount)
            print("Balance:", self.balance)

        except Exception as e:
            print(e)


# Input validation for PIN and balance
while True:
    try:
        print("\n\tWELCOME TO ATM ......!")
        pin = int(input("\nSet your PIN: "))
        if pin <= 0:
            raise ValueError("PIN must be positive")
        break
    except ValueError as e:
        print("Error:", e)

while True:
    try:
        balance = float(input("\nEnter initial balance: "))
        if balance < 0:
            raise ValueError("Balance cannot be negative")
        break
    except ValueError as e:
        print("Error:", e)

atm = ATM(pin, balance)

if atm.verify_pin():
    atm.withdraw()
