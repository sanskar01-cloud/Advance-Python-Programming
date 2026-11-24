
# Payment Processing System using Strategy Pattern

class CreditCard:
    def pay(self, amount):
        print("Paid Rs.", amount, "using Credit Card")


class UPI:
    def pay(self, amount):
        print("Paid Rs.", amount, "using UPI")


class PayPal:
    def pay(self, amount):
        print("Paid Rs.", amount, "using PayPal")


# Payment Context
class Payment:
    def __init__(self, strategy):
        self.strategy = strategy

    def make_payment(self, amount):
        self.strategy.pay(amount)


# Main Program
print("Select Payment Method")
print("1. Credit Card")
print("2. UPI")
print("3. PayPal")

choice = int(input("Enter your choice: "))
amount = float(input("Enter payment amount: "))

if choice == 1:
    payment_method = CreditCard()
elif choice == 2:
    payment_method = UPI()
elif choice == 3:
    payment_method = PayPal()
else:
    print("Invalid choice")
    exit()

payment = Payment(payment_method)
payment.make_payment(amount)
