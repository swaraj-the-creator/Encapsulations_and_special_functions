import random

class Account:
    def __init__(self, owner, pin):
        self.owner = owner
        self.__pin = str(pin)

    def show_pin_status(self):
        print("PIN is safely stored.")

    def set_pin(self, new_pin):
        new_pin = str(new_pin)

        if len(new_pin) == 4 and new_pin.isdigit():
            self.__pin = new_pin
            print("PIN updated successfully.")
            return True

        print("Invalid PIN. PIN must be exactly 4 digits.")
        return False

    def check_pin(self):
        for attempt in range(5):
            entered_pin = input("Enter the PIN: ")

            if entered_pin == self.__pin:
                print("Access granted.")
                return True

            chances_left = 4 - attempt
            print("Access denied.")
            if chances_left:
                print(f"Number of chances left: {chances_left}")

        print("System locked.")
        return False

    def __str__(self):
        return f"Account holder: {self.owner}"

name = input("\nEnter name of account holder: ")
pin = random.randint(1000, 9999)

my_account = Account(name, pin)
print("Hint for pin: ",pin - 131)
print(my_account)
my_account.show_pin_status()

if my_account.check_pin():
    new_pin = input("Enter new PIN: ")
    my_account.set_pin(new_pin)
    my_account.check_pin()
